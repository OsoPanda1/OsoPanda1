# Plan de unificación TAMV Digital Nexus

Este repositorio ahora incluye una base operativa para consolidar los repos de `OsoPanda1` en una sola plataforma.

## Qué integra

1. **Descubrimiento automático de repositorios** por API de GitHub.
2. **Manifiesto trazable** en `config/repos.json` con metadata de cada repositorio.
3. **Sincronización local** en `sources/<repo>` con `git clone` / `git fetch`.
4. **Límite configurable** (`--max-repos`) para avanzar por fases hasta cubrir los 177 repos.

## Flujo recomendado

```bash
# 1) Crear/actualizar el manifiesto de todos los repos
make dry-run

# 2) Ejecutar bootstrap completo (clona/sincroniza)
make bootstrap

# 3) Revisar repos integrados
ls sources
```

## Notas

- Para repos privados, exporta `GITHUB_TOKEN` con permisos de lectura.
- Puedes repetir el proceso diariamente; el script hace `fetch + pull` si el repo ya existe.
- Esta base permite extender una fase 2 con:
  - indexado semántico,
  - catálogo de servicios por repo,
  - pipeline CI para pruebas agregadas.
