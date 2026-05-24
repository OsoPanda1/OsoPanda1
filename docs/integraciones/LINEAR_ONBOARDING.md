# Conexión y arranque con Linear (TAMV Digital Nexus)

## 1) Preparar acceso a Linear

1. En Linear, crea un **API Key personal** desde `Settings > API > Personal API keys`.
2. Exporta la variable en tu terminal:

```bash
export LINEAR_API_KEY="<tu_token>"
```

3. (Opcional) Define IDs de team/proyecto para automatizar creación de issues.

## 2) Construir plan de integración repo por repo

Desde la raíz del repositorio:

```bash
python -m tamv_digital_nexus.cli linear-plan \
  --inventory config/repos_seed.json \
  --out-json cache/linear_plan.json \
  --out-md docs/integraciones/LINEAR_PLAN.md
```

Esto genera un plan secuencial para interconectar repositorios uno por uno con campos:
- `depends_on`: issue/repositorio previo requerido.
- `blocks`: siguiente repositorio a destrabar.

## 3) Ejecutar la integración técnica local

```bash
python -m tamv_digital_nexus.cli integrate --inventory config/repos_seed.json
```

## 4) Ciclo recomendado en Linear

Para cada repositorio en `LINEAR_PLAN.md`:

1. Crear issue "[NEXUS] Integrar <repo>".
2. Registrar dependencia contra `depends_on`.
3. Ejecutar integración local y pruebas.
4. Mover issue a `Done` y desbloquear `blocks`.

## 5) Escalar a todos los repositorios

1. Actualiza `config/repos_seed.json` con el listado completo de repositorios.
2. Vuelve a ejecutar `linear-plan`.
3. Crea issues en lote respetando el orden del plan.
