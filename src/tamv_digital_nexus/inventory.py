from __future__ import annotations

import json
from pathlib import Path

from .models import RepoArtifact


def load_inventory(path: Path) -> list[RepoArtifact]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    repos = payload.get("repositories", [])
    artifacts: list[RepoArtifact] = []

    for repo in repos:
        artifacts.append(
            RepoArtifact(
                name=repo["name"],
                default_branch=repo.get("default_branch", "main"),
                source_url=repo.get("clone_url", ""),
                tags=repo.get("tags", []),
                local_path=Path(repo["local_path"]) if repo.get("local_path") else None,
            )
        )

    return artifacts


def save_inventory(path: Path, artifacts: list[RepoArtifact]) -> None:
    payload = {
        "schema": "tamv-digital-nexus/repo-manifest@v1",
        "repositories": [
            {
                "name": a.name,
                "default_branch": a.default_branch,
                "clone_url": a.source_url,
                "tags": a.tags,
                "local_path": str(a.local_path) if a.local_path else None,
            }
            for a in artifacts
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
