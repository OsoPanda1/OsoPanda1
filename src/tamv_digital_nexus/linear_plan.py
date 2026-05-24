from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from .models import RepoArtifact


def build_repo_sequence(artifacts: list[RepoArtifact]) -> list[dict]:
    """Construye una secuencia de integración repositorio a repositorio.

    Se usa el orden del inventario como fuente de verdad para conectar
    cada repositorio con su siguiente dependencia operativa.
    """

    sequence: list[dict] = []
    for index, artifact in enumerate(artifacts):
        depends_on = artifacts[index - 1].name if index > 0 else None
        blocks = artifacts[index + 1].name if index < len(artifacts) - 1 else None
        sequence.append(
            {
                "repo": artifact.name,
                "depends_on": depends_on,
                "blocks": blocks,
                "default_branch": artifact.default_branch,
                "source_url": artifact.source_url,
                "tags": artifact.tags,
                "linear_title": f"[NEXUS] Integrar {artifact.name}",
                "linear_description": (
                    "Sincronizar este repositorio en el workspace federado y "
                    "validar contratos de integración con el núcleo MD-X4."
                ),
            }
        )
    return sequence


def export_linear_plan(output_path: Path, artifacts: list[RepoArtifact]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sequence = build_repo_sequence(artifacts)
    payload = {
        "schema": "tamv-digital-nexus/linear-plan@v1",
        "integration_strategy": "sequential-one-by-one",
        "repositories": sequence,
    }
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def render_markdown(sequence: list[dict]) -> str:
    lines = [
        "# Plan de integración para Linear",
        "",
        "Estrategia: interconectar repositorios uno por uno con dependencias explícitas.",
        "",
        "| Orden | Repositorio | Depende de | Bloquea |",
        "| --- | --- | --- | --- |",
    ]

    for index, item in enumerate(sequence, start=1):
        lines.append(
            f"| {index} | {item['repo']} | {item['depends_on'] or '-'} | {item['blocks'] or '-'} |"
        )

    lines.extend(["", "## Plantilla sugerida para issue en Linear", ""])

    if sequence:
        sample = sequence[0]
        lines.extend(
            [
                f"**Título:** {sample['linear_title']}",
                "",
                "**Descripción:**",
                sample["linear_description"],
                "",
                "**Checklist:**",
                "- [ ] Clonar/sincronizar el repositorio",
                "- [ ] Ejecutar pruebas locales",
                "- [ ] Actualizar inventario de integración",
                "- [ ] Vincular issue siguiente en `blocks`",
            ]
        )

    return "\n".join(lines) + "\n"
