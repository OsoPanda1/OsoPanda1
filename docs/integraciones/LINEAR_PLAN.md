# Plan de integración para Linear

Estrategia: interconectar repositorios uno por uno con dependencias explícitas.

| Orden | Repositorio | Depende de | Bloquea |
| --- | --- | --- | --- |
| 1 | OsoPanda1 | - | - |

## Plantilla sugerida para issue en Linear

**Título:** [NEXUS] Integrar OsoPanda1

**Descripción:**
Sincronizar este repositorio en el workspace federado y validar contratos de integración con el núcleo MD-X4.

**Checklist:**
- [ ] Clonar/sincronizar el repositorio
- [ ] Ejecutar pruebas locales
- [ ] Actualizar inventario de integración
- [ ] Vincular issue siguiente en `blocks`
