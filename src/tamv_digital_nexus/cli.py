from __future__ import annotations

import argparse
from pathlib import Path

from .inventory import load_inventory
from .orchestrator import NexusIntegrator
from .server import serve_index


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CLI TAMV Digital Nexus")
    sub = parser.add_subparsers(dest="command", required=True)

    integrate = sub.add_parser("integrate", help="Integra repos del manifiesto en sources/")
    integrate.add_argument("--inventory", default="config/repos_seed.json")
    integrate.add_argument("--cache-root", default="cache/repos")
    integrate.add_argument("--workspace-root", default="sources")
    integrate.add_argument("--index-db", default="cache/nexus_index.db")
    integrate.add_argument("--index-json", default="cache/nexus_index.json")

    serve = sub.add_parser("serve", help="Sirve API local sobre el índice sqlite")
    serve.add_argument("--index-db", default="cache/nexus_index.db")
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8080)

    return parser


def main() -> int:
    args = build_parser().parse_args()

    if args.command == "integrate":
        artifacts = load_inventory(Path(args.inventory))
        integrator = NexusIntegrator(
            cache_root=Path(args.cache_root),
            workspace_root=Path(args.workspace_root),
            index_db=Path(args.index_db),
        )
        report = integrator.integrate(artifacts)
        integrator.export_json_index(Path(args.index_json), artifacts)

        print(f"Integrados: {report.integrated}/{report.total}")
        if report.failures:
            print("Fallos:")
            for failure in report.failures:
                print(f" - {failure}")
        return 0 if report.failed == 0 else 2

    if args.command == "serve":
        serve_index(Path(args.index_db), host=args.host, port=args.port)
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
