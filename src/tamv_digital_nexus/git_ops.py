from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def run_git(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True)


def ensure_clone(source_url: str, cache_dir: Path, name: str) -> Path:
    target = cache_dir / name
    cache_dir.mkdir(parents=True, exist_ok=True)

    if (target / ".git").exists():
        run_git(["fetch", "--all", "--prune"], cwd=target)
        return target

    run_git(["clone", "--depth", "1", source_url, str(target)])
    return target


def copy_worktree(repo_path: Path, destination: Path) -> int:
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True, exist_ok=True)

    copied = 0
    for item in repo_path.iterdir():
        if item.name == ".git":
            continue
        target = destination / item.name
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)
        copied += 1
    return copied
