from __future__ import annotations

import argparse
from pathlib import Path

from .inventory import load_inventory
from .linear_plan import build_repo_sequence, export_linear_plan, render_markdown
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

    linear = sub.add_parser("linear-plan", help="Genera plan secuencial para cargar issues en Linear")
    linear.add_argument("--inventory", default="config/repos_seed.json")
    linear.add_argument("--out-json", default="cache/linear_plan.json")
    linear.add_argument("--out-md", default="docs/integraciones/LINEAR_PLAN.md")

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

    if args.command == "linear-plan":
        artifacts = load_inventory(Path(args.inventory))
        export_linear_plan(Path(args.out_json), artifacts)
        sequence = build_repo_sequence(artifacts)
        Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out_md).write_text(render_markdown(sequence), encoding="utf-8")
        print(f"Plan Linear generado: {args.out_json} y {args.out_md}")
        return 0

    if args.command == "serve":
        serve_index(Path(args.index_db), host=args.host, port=args.port)
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
