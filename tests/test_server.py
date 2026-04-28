from __future__ import annotations

import json
import socket
import sqlite3
import threading
import time
from pathlib import Path
from urllib.request import urlopen

from tamv_digital_nexus.server import serve_index


def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


def _seed_db(db: Path) -> None:
    conn = sqlite3.connect(db)
    try:
        conn.execute(
            "CREATE TABLE repo_index (name TEXT PRIMARY KEY, default_branch TEXT, source_url TEXT, tags TEXT, copied_entries INTEGER)"
        )
        conn.execute(
            "INSERT INTO repo_index(name, default_branch, source_url, tags, copied_entries) VALUES ('OsoPanda1','main','local','tamv',1)"
        )
        conn.commit()
    finally:
        conn.close()


def test_http_server_exposes_repos(tmp_path: Path) -> None:
    db = tmp_path / "idx.db"
    _seed_db(db)
    port = _free_port()

    t = threading.Thread(target=serve_index, args=(db, "127.0.0.1", port), daemon=True)
    t.start()
    time.sleep(0.2)

    with urlopen(f"http://127.0.0.1:{port}/repos", timeout=3) as r:
        data = json.loads(r.read().decode("utf-8"))

    assert len(data) == 1
    assert data[0]["name"] == "OsoPanda1"
