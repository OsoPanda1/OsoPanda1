#!/usr/bin/env python3
"""Unifica múltiples repositorios de GitHub en un monorepo funcional.

Uso rápido:
  python scripts/unify_repos.py \
      --owner OsoPanda1 \
      --target-root sources \
      --manifest-out config/repos.json \
      --max-repos 177
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

GITHUB_API = "https://api.github.com"
DEFAULT_BRANCHES = ("main", "master")


@dataclass
class Repo:
    name: str
    clone_url: str
    default_branch: str
    archived: bool
    private: bool


def github_get(path: str, token: str | None = None, query: dict[str, str | int] | None = None) -> tuple[dict | list, dict]:
    q = f"?{urlencode(query)}" if query else ""
    url = f"{GITHUB_API}{path}{q}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "tamv-digital-nexus-bootstrap",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = Request(url, headers=headers)
    with urlopen(req, timeout=30) as response:
        body = response.read().decode("utf-8")
        payload = json.loads(body)
        response_headers = dict(response.headers.items())
    return payload, response_headers


def list_repositories(owner: str, token: str | None = None, max_repos: int | None = None) -> list[Repo]:
    page = 1
    repos: list[Repo] = []

    while True:
        payload, _ = github_get(
            f"/users/{owner}/repos",
            token=token,
            query={"per_page": 100, "page": page, "type": "owner", "sort": "updated"},
        )

        if not isinstance(payload, list) or not payload:
            break

        for item in payload:
            repos.append(
                Repo(
                    name=item["name"],
                    clone_url=item["clone_url"],
                    default_branch=item.get("default_branch") or "main",
                    archived=bool(item.get("archived", False)),
                    private=bool(item.get("private", False)),
                )
            )
            if max_repos and len(repos) >= max_repos:
                return repos

        page += 1

    return repos


def run(cmd: list[str], cwd: Path | None = None) -> None:
    print("$", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def clone_or_update(repo: Repo, target_root: Path) -> None:
    destination = target_root / repo.name
    if destination.exists() and (destination / ".git").exists():
        run(["git", "-C", str(destination), "fetch", "--all", "--prune"])
        branch = repo.default_branch if repo.default_branch else "main"
        run(["git", "-C", str(destination), "checkout", branch])
        run(["git", "-C", str(destination), "pull", "--ff-only", "origin", branch])
        return

    run(["git", "clone", repo.clone_url, str(destination)])


def write_manifest(repos: Iterable[Repo], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc = {
        "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "schema": "tamv-digital-nexus/repo-manifest@v1",
        "repositories": [
            {
                "name": repo.name,
                "clone_url": repo.clone_url,
                "default_branch": repo.default_branch,
                "archived": repo.archived,
                "private": repo.private,
            }
            for repo in repos
        ],
    }
    output_path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Unifica repositorios de un perfil de GitHub en un workspace local")
    parser.add_argument("--owner", required=True, help="Usuario/owner de GitHub")
    parser.add_argument("--token-env", default="GITHUB_TOKEN", help="Nombre de variable de entorno con token de GitHub")
    parser.add_argument("--target-root", default="sources", help="Directorio donde se clonan los repos")
    parser.add_argument("--manifest-out", default="config/repos.json", help="Archivo de salida del manifiesto")
    parser.add_argument("--max-repos", type=int, default=None, help="Máximo de repos a sincronizar")
    parser.add_argument("--include-archived", action="store_true", help="Incluye repos archivados")
    parser.add_argument("--dry-run", action="store_true", help="No clona, solo genera manifiesto")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    token = os.getenv(args.token_env)

    try:
        repos = list_repositories(args.owner, token=token, max_repos=args.max_repos)
    except (HTTPError, URLError) as exc:
        print(f"Error consultando GitHub API: {exc}", file=sys.stderr)
        return 1

    if not args.include_archived:
        repos = [r for r in repos if not r.archived]

    write_manifest(repos, Path(args.manifest_out))
    print(f"Manifest generado en {args.manifest_out} con {len(repos)} repositorios")

    if args.dry_run:
        return 0

    target_root = Path(args.target_root)
    target_root.mkdir(parents=True, exist_ok=True)

    failures: list[tuple[str, str]] = []
    for repo in repos:
        try:
            clone_or_update(repo, target_root)
        except subprocess.CalledProcessError as exc:
            failures.append((repo.name, str(exc)))

    if failures:
        print("Repos con error:", file=sys.stderr)
        for name, reason in failures:
            print(f"  - {name}: {reason}", file=sys.stderr)
        return 2

    print(f"Sincronización completada: {len(repos)} repos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
