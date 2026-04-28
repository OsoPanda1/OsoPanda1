from __future__ import annotations

import json
import sqlite3
from dataclasses import asdict
from pathlib import Path

from .git_ops import copy_worktree, ensure_clone
from .models import IntegrationReport, RepoArtifact


class NexusIntegrator:
    """Integra repositorios en `sources/<repo>` y genera un índice consultable."""

    def __init__(self, cache_root: Path, workspace_root: Path, index_db: Path) -> None:
        self.cache_root = cache_root
        self.workspace_root = workspace_root
        self.index_db = index_db

    def integrate(self, artifacts: list[RepoArtifact]) -> IntegrationReport:
        failures: list[str] = []
        integrated = 0
        self.workspace_root.mkdir(parents=True, exist_ok=True)

        rows: list[dict] = []
        for artifact in artifacts:
            try:
                source = artifact.source_url if artifact.source_url else str((artifact.local_path or Path(".")).resolve())
                cloned = ensure_clone(source, self.cache_root, artifact.name)
                copied_files = copy_worktree(cloned, self.workspace_root / artifact.name)
                rows.append(
                    {
                        "name": artifact.name,
                        "default_branch": artifact.default_branch,
                        "source_url": artifact.source_url,
                        "tags": ",".join(artifact.tags),
                        "copied_entries": copied_files,
                    }
                )
                integrated += 1
            except Exception as exc:  # intentionally broad to continue batch integration
                failures.append(f"{artifact.name}: {exc}")

        self._write_index(rows)
        return IntegrationReport(
            total=len(artifacts), integrated=integrated, failed=len(failures), failures=failures
        )

    def _write_index(self, rows: list[dict]) -> None:
        self.index_db.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(self.index_db)
        try:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS repo_index (
                    name TEXT PRIMARY KEY,
                    default_branch TEXT,
                    source_url TEXT,
                    tags TEXT,
                    copied_entries INTEGER
                )
                """
            )
            conn.execute("DELETE FROM repo_index")
            conn.executemany(
                "INSERT INTO repo_index(name, default_branch, source_url, tags, copied_entries) VALUES (:name, :default_branch, :source_url, :tags, :copied_entries)",
                rows,
            )
            conn.commit()
        finally:
            conn.close()

    def export_json_index(self, output: Path, artifacts: list[RepoArtifact]) -> None:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(
                {
                    "schema": "tamv-digital-nexus/integration-index@v1",
                    "repositories": [asdict(a) for a in artifacts],
                },
                indent=2,
                ensure_ascii=False,
                default=str,
            )
            + "\n",
            encoding="utf-8",
        )
