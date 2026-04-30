# Checklist Maestro TAMV / MD‑X4/X5 / RDM Digital

> Documento maestro para seguimiento en GitHub Projects/Issues.

## 1. Organización y Repositorios
- [ ] Crear la organización `tamv-online-network` en GitHub.
- [ ] Asignar mínimo dos owners/admins y documentarlos.
- [ ] Definir estrategia monorepo/polyrepo en `tamv-docs/architecture/repository-strategy.md`.
- [ ] Crear/confirmar repos clave:
  - [ ] `mdx4-kernel`
  - [ ] `mdx5-kernel`
  - [ ] `tamv-online-platform`
  - [ ] `tamv-services-*`
  - [ ] `tamv-infra`
  - [ ] `tamv-docs`
  - [ ] `tamv-examples`
  - [ ] `tamv-ai`
  - [ ] `tamv-governance`
  - [ ] `tamv-academia`
  - [ ] `rdm-digital-os`

## 2. Archivos estándar por repositorio
- [ ] `README.md`
- [ ] `LICENSE`
- [ ] `CONTRIBUTING.md`
- [ ] `CODE_OF_CONDUCT.md`
- [ ] `SECURITY.md`
- [ ] `CHANGELOG.md`
- [ ] `ROADMAP.md`
- [ ] `AWAKENING.md`
- [ ] `GOVERNANCE.md`
- [ ] `CODEOWNERS` (raíz o `.github/`)
- [ ] `.github/ISSUE_TEMPLATE/*`
- [ ] `.github/PULL_REQUEST_TEMPLATE.md`
- [ ] `.editorconfig`, `.gitignore`, `.gitattributes`

## 3. Código y capas
### 3.1 Kernel MD‑X4 / MD‑X5
- [ ] Arquitectura hexagonal (`/core`, `/federation`, `/protocols`, `/security`, `/integration`).
- [ ] Bounded contexts DDD con lenguaje ubicuo.
- [ ] Puertos (repos, colas, notificaciones) + adaptadores intercambiables.
- [ ] Implementaciones referencia (Postgres/Redis/eventos).
- [ ] Mecanismo de federación de nodos (registro, reconciliación, propagación).
- [ ] SDK cliente `mdx4-sdk`.

### 3.2 TAMV Online Platform
- [ ] `/backend` con auth (JWT/OAuth2) y orquestación hacia kernel.
- [ ] `/frontend` con flujos de usuario y paneles.
- [ ] `/services` para notificaciones y métricas.
- [ ] Arquitectura documentada en `tamv-docs`.

### 3.3 TAMV Services
- [ ] Estructura por servicio: `/domain`, `/app`, `/infra`, `/api`, `/tests`.
- [ ] CRUD completo por entidad.
- [ ] Eventos de dominio (ej. `CitizenRegistered`, `NodeJoined`).
- [ ] Integración a bus de eventos (Kafka/NATS).
- [ ] Base de datos propia por servicio.

### 3.4 Infraestructura (`tamv-infra`)
- [ ] `/docker`, `/compose`, `/k8s`, `/terraform`.
- [ ] `make dev`, `make test`, `make deploy`.
- [ ] CI/CD con build y test por PR.

## 4. Documentación Técnica Profunda (`tamv-docs`)
- [ ] `overview.md`
- [ ] `architecture/01-context-view.md`
- [ ] `architecture/02-container-view.md`
- [ ] `architecture/03-component-view.md`
- [ ] `architecture/04-deployment-view.md`
- [ ] `architecture/05-runtime-view.md`
- [ ] `architecture/06-domain-model.md`
- [ ] `architecture/07-security-view.md`
- [ ] `architecture/08-governance-view.md`
- [ ] `api/` (OpenAPI/GraphQL versionados)
- [ ] `ops/` (deploy, monitoreo, backup/DR)
- [ ] `tests/` (estrategia y criterios)
- [ ] Diagramas como código + generación en CI.

## 5. Narrativa y Filosofía
- [ ] `manifesto/sovereign-origin.md`
- [ ] `manifesto/latam-sovereignty.md`
- [ ] `manifesto/civilizational-stack.md`
- [ ] `philosophy/design-principles.md`
- [ ] `philosophy/governance-philosophy.md`
- [ ] `philosophy/ethics-ai-tamv.md`
- [ ] `narratives/stories-from-the-future.md`
- [ ] `narratives/anubis-villasenor-mythos.md`

## 6. Academia y DOIs (`tamv-academia`)
- [ ] `papers/paper-mdx4-kernel.pdf`
- [ ] `papers/paper-tamv-platform.pdf`
- [ ] `papers/paper-rdm-digital-os.pdf`
- [ ] `whitepapers/whitepaper-sovereign-tech-latam.pdf`
- [ ] `whitepapers/whitepaper-mdx5-evolution.pdf`
- [ ] Publicar/registrar DOIs y enlazar cruzado en repos/docs.

## 7. Kits de adopción
- [ ] `kits/city-kit/`
- [ ] `kits/university-kit/`
- [ ] `kits/community-kit/`
- [ ] Plantillas de convenios/MoU.

## 8. Comunidad y contribución (`tamv-governance`)
- [ ] `CONTRIBUTING.md` extendido.
- [ ] `COMMUNITY.md` con canales/calendario.
- [ ] Carpeta `RFCs/` + plantilla `TAMV-RFC-XXXX.md`.
- [ ] Modelo de gobernanza híbrida documentado.
- [ ] Minutas de reuniones periódicas.

## 9. Go-to-Market
- [ ] `positioning/value-proposition.md`
- [ ] `positioning/comparisons.md`
- [ ] `marketing/one-pager.pdf`
- [ ] `marketing/deck-slides/` (ES/EN)
- [ ] Blog posts clave (ES/EN).

## 10. Release público v1.0.0
- [ ] Verificación documental integral.
- [ ] CI en verde para repos críticos.
- [ ] Tags `v1.0.0` en repos principales.
- [ ] `CHANGELOG.md` actualizado.
- [ ] Release notes en GitHub.
- [ ] Publicación de DOIs en Zenodo.

## 11. Seguimiento maestro
- [x] Almacenar este checklist como `CHECKLIST_TAMV_MDX4_RDM.md` en repo central.
- [ ] Replicar como epics/issues en GitHub Projects.
- [ ] Revisión mensual de avance.

## 12. Expansión MD‑X5
- [ ] Documento de diseño `mdx5-kernel` (capacidades antifrágiles).
- [ ] Plan de migración MD‑X4 → MD‑X5.
- [ ] Evaluación metamonorepo opcional.

## 13. RDM Digital OS
- [ ] Módulos: dashboards, IA regulatoria, gamificación pública.
- [ ] Integración con MDX kernel y TAMV Platform (API/eventos).
- [ ] Documento marco: OS territorial vs MIS tradicional.

## 14. Sistemas funcionales y plataformas clave
- [ ] Alamexa
- [ ] Anubis Centinel
- [ ] Horus
- [ ] EOCT
- [ ] BookPI
- [ ] Isabella Villaseñor AI
- [ ] Para cada sistema: repo/módulo, API docs y casos de uso.

## 15. Integración de sistemas funcionales
- [ ] Crear `architecture/system-integration.md`.
- [ ] Definir APIs/protocolos entre sistemas.
- [ ] Documentar sync vs async/eventos y dependencias.
- [ ] Casos de uso end-to-end de integración.

## 16. Recursos de referencia
- [ ] Crear/actualizar `tamv-docs/references.md` con:
  - [ ] templates de repos open source,
  - [ ] guías CODEOWNERS,
  - [ ] checklists de auditoría,
  - [ ] artículos microservicios/EDA,
  - [ ] guías C4,
  - [ ] prácticas de gobernanza open source,
  - [ ] políticas OSS para gobiernos.

---

## Estado operativo actual en este repo (`OsoPanda1/OsoPanda1`)
- [x] Bootstrap de unificación documentado (`README.md`, `docs/UNIFICACION.md`).
- [x] Núcleo SQL base (`db/tamv_nexus_schema.sql`, `db/init.sql`).
- [x] Servicio ejecutable inicial `tamv-pdos-core` (Node + Postgres + Docker).
- [ ] Normalización completa de archivos estándar OSS en todos los repos del ecosistema.
- [ ] Migración faseada de repos críticos al monorepo operativo.
