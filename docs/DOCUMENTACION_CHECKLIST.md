# Plan de documentación inicial conforme al checklist maestro

Este documento inicia la trazabilidad para documentar de forma sistemática los cambios integrados en el perfil/repositorio y alinearlos al `CHECKLIST_TAMV_MDX4_RDM.md`.

## 1) Objetivo

Establecer un proceso repetible para:

1. levantar inventario de cambios por repositorio,
2. mapear evidencia documental por rubro del checklist,
3. registrar brechas y acciones con responsable/fecha,
4. mantener un tablero de avance auditable.

## 2) Estado base detectado en este repositorio

### Evidencia ya presente
- Checklist maestro en raíz (`CHECKLIST_TAMV_MDX4_RDM.md`).
- Documentación de bootstrap/unificación en `README.md` y `docs/UNIFICACION.md`.
- Núcleo de esquema SQL en `db/tamv_nexus_schema.sql` y `db/init.sql`.
- Servicio inicial ejecutable (`src/`, `Dockerfile`, `docker-compose.yml`, `Makefile`).

### Brechas prioritarias para estandarización documental
- Faltan varios archivos estándar OSS definidos en el punto 2 del checklist (`LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CHANGELOG.md`, `ROADMAP.md`, `GOVERNANCE.md`, `CODEOWNERS`, plantillas de issue/PR).
- Falta una bitácora formal por lote de integración (por ejemplo, lotes de >300 archivos/cambios).
- Falta matriz de cumplimiento por secciones (1..16) con porcentaje y evidencias.

## 3) Flujo mínimo obligatorio por cada integración de cambios

> Aplicar este flujo para cada lote de cambios (incluyendo integraciones masivas).

1. **Inventario técnico del lote**
   - número de archivos modificados/altas/bajas,
   - rutas críticas afectadas,
   - módulos impactados.
2. **Resumen funcional**
   - qué capacidades nuevas se agregaron,
   - qué deuda técnica/documental se introduce.
3. **Mapeo al checklist**
   - sección/subsección impactada,
   - evidencia concreta (archivo + líneas o issue/PR).
4. **Acciones de cierre**
   - tareas pendientes con dueño y fecha objetivo.
5. **Publicación**
   - actualizar este documento y el tablero de seguimiento.

## 4) Matriz de seguimiento (plantilla inicial)

| Sección checklist | Estado | Evidencia | Pendientes inmediatos |
|---|---|---|---|
| 1. Organización y repositorios | En progreso | `CHECKLIST_TAMV_MDX4_RDM.md` | Definir/confirmar estrategia repo y owners |
| 2. Archivos estándar por repo | En progreso | `README.md`, `.gitignore` | Crear los archivos OSS faltantes |
| 3. Código y capas | En progreso | `src/`, `db/`, `docker-compose.yml` | Documentar arquitectura por capas actual |
| 4. Documentación técnica profunda | Pendiente parcial | `docs/UNIFICACION.md`, `docs/PDOS_CORE.md` | Crear estructura `docs/architecture/*` mínima |
| 11. Seguimiento maestro | En progreso | `CHECKLIST_TAMV_MDX4_RDM.md` | Replicar epics/issues y revisión mensual |

## 5) Convención de bitácora de integración

A partir de ahora, cada integración deberá crear un archivo en:

`docs/integraciones/YYYY-MM-DD_<tema>.md`

Contenido mínimo:
- contexto del merge/integración,
- métricas de cambio (archivos/LOC),
- riesgos,
- mapeo a checklist,
- tareas de documentación derivadas.

## 6) Próximos pasos recomendados (fase 0)

1. Crear los documentos base faltantes del punto 2 del checklist en la raíz del repo.
2. Abrir un epic de “Normalización documental” y desglosarlo por archivo estándar.
3. Crear la primera bitácora histórica para el lote masivo (>300 archivos/cambios).
4. Generar un corte semanal de cumplimiento (% por sección 1..16).

---

**Resultado esperado:** que ningún lote de código vuelva a entrar sin su trazabilidad documental explícita y su mapeo al checklist maestro.
