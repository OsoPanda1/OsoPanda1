from pathlib import Path
import sqlite3
import subprocess

from tamv_digital_nexus.models import RepoArtifact
from tamv_digital_nexus.orchestrator import NexusIntegrator


def _init_git_repo(path: Path) -> None:
    path.mkdir(parents=True)
    subprocess.run(["git", "init"], cwd=path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "bot@example.com"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.name", "Bot"], cwd=path, check=True)
    (path / "app.py").write_text("print('hola')\n", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=path, check=True)
    subprocess.run(["git", "commit", "-m", "init"], cwd=path, check=True, capture_output=True)


def test_integrate_git_repo_and_create_index(tmp_path: Path) -> None:
    remote_repo = tmp_path / "remote_repo"
    _init_git_repo(remote_repo)

    integrator = NexusIntegrator(
        cache_root=tmp_path / "cache",
        workspace_root=tmp_path / "sources",
        index_db=tmp_path / "cache" / "index.db",
    )

    report = integrator.integrate(
        [
            RepoArtifact(
                name="OsoPanda1",
                source_url=str(remote_repo),
                tags=["tamv"],
            )
        ]
    )

    assert report.failed == 0
    assert (tmp_path / "sources" / "OsoPanda1" / "app.py").exists()

    conn = sqlite3.connect(tmp_path / "cache" / "index.db")
    try:
        row = conn.execute("SELECT name, copied_entries FROM repo_index WHERE name = 'OsoPanda1'").fetchone()
    finally:
        conn.close()

    assert row[0] == "OsoPanda1"
    assert row[1] >= 1
