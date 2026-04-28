from __future__ import annotations

import json
import sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


class NexusRequestHandler(BaseHTTPRequestHandler):
    db_path: Path

    def _json(self, payload: dict | list, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)

        if parsed.path == "/health":
            self._json({"status": "ok"})
            return

        if parsed.path == "/repos":
            self._json(self._list_repos())
            return

        if parsed.path.startswith("/repos/"):
            name = parsed.path.split("/", 2)[2]
            repo = self._repo_detail(name)
            if repo is None:
                self._json({"error": "not_found", "repo": name}, status=404)
                return
            self._json(repo)
            return

        self._json({"error": "route_not_found", "path": parsed.path}, status=404)

    def log_message(self, format: str, *args: object) -> None:  # silence default logs
        return

    def _list_repos(self) -> list[dict]:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            rows = conn.execute("SELECT name, default_branch, source_url, tags, copied_entries FROM repo_index ORDER BY name").fetchall()
            return [dict(r) for r in rows]
        finally:
            conn.close()

    def _repo_detail(self, name: str) -> dict | None:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            row = conn.execute(
                "SELECT name, default_branch, source_url, tags, copied_entries FROM repo_index WHERE name = ?",
                (name,),
            ).fetchone()
            return dict(row) if row else None
        finally:
            conn.close()


def serve_index(db_path: Path, host: str = "127.0.0.1", port: int = 8080) -> None:
    handler = type("ConfiguredNexusHandler", (NexusRequestHandler,), {"db_path": db_path})
    server = ThreadingHTTPServer((host, port), handler)
    print(f"Nexus API listening on http://{host}:{port}")
    server.serve_forever()
