# Plan de unificación TAMV Digital Nexus

Este repositorio incluye una base operativa para consolidar los repos de `OsoPanda1` en una sola plataforma.

## Posicionamiento estratégico

- `OsoPanda1/OsoPanda1`: **spec civilizatorio** (visión, narrativa, gobernanza, academia, blindaje legal).
- `tamv-digital-nexus`: **núcleo operativo** para sincronizar repos, materializar estructura monorepo y ejecutar integraciones técnicas.

## Qué integra hoy

1. **Descubrimiento automático de repositorios** por API de GitHub.
2. **Manifiesto trazable** en `config/repos.json` con metadata de cada repositorio.
3. **Sincronización local** en `sources/<repo>` con `git clone` / `git fetch`.
4. **Límite configurable** (`--max-repos`) para avanzar por fases hasta cubrir 177 repos.
5. **Núcleo SQL** del nexus en `db/tamv_nexus_schema.sql`.

## Flujo recomendado

```bash
# 1) Crear/actualizar el manifiesto de todos los repos
make dry-run

# 2) Ejecutar bootstrap completo (clona/sincroniza)
make bootstrap

# 3) Inicializar esquema SQL del nexus
psql "$DATABASE_URL" -f db/tamv_nexus_schema.sql

# 4) Revisar repos integrados
ls sources
```

## Estructura objetivo del monorepo

```text
code/
  mdx4-kernel/
  rdm-tos-frontend/
  isabella-kernel-demo/
  xr-runtime/
  bookpi-msr/
data/
models/
docs/
ethics/
```

## Plan por fases

### Fase 1 · Fundación (0–30 días)

- Consolidar manifiesto completo de repos.
- Activar esquema SQL y seeds del nexus.
- Etiquetar repos críticos por dominio: MD‑X4, RDM‑TOS, XR, Isabella, BookPI/MSR.

### Fase 2 · Integración (30–90 días)

- Mapear repos críticos a `code/*`.
- Crear contratos de integración (README técnico por módulo + dependencias + runbooks).
- Incorporar telemetría de ejecuciones y decisiones en `pdos_executions`/`pdos_decisions`.

### Fase 3 · Operación civilizatoria (90+ días)

- Endurecer CI/CD para pruebas agregadas.
- Integrar catálogo de modelos/datasets en `models/` y `data/`.
- Publicar releases del monorepo con trazabilidad spec (`OsoPanda1`) ↔ operación (`tamv-digital-nexus`).

## Notas

- Para repos privados, exporta `GITHUB_TOKEN` con permisos de lectura.
- Puedes repetir el proceso diariamente; el script hace `fetch + pull` si el repo ya existe.
