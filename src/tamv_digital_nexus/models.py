from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class RepoArtifact:
    name: str
    default_branch: str = "main"
    source_url: str = ""
    tags: list[str] = field(default_factory=list)
    local_path: Path | None = None


@dataclass(slots=True)
class IntegrationReport:
    total: int
    integrated: int
    failed: int
    failures: list[str] = field(default_factory=list)
