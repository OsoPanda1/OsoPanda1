# TAMV Agent (diseño unificado 1→206→1)

Este repositorio ahora incluye un esqueleto funcional de `tamv-agent` en Rust para estandarizar la capa de gossip/estado distribuido en los 206 repos TAMV.

## Qué quedó integrado

- Binario único: `tamv-agent/` (Rust + Tokio + Serde + HMAC SHA-256).
- Formato de configuración por nodo: `config.toml` (ver ejemplo).
- Estado persistente local: `state.json` con escritura atómica (`tmp + rename`).
- Bucle asíncrono base con tick de gossip y firma de mensajes `STATE_SYNC`.

## Uso local

```bash
cd tamv-agent
cp examples/config.toml config.toml
cargo run
```

## Despliegue a 206 repos

1. Publicar binario estático `tamv-agent`.
2. En cada repo:
   - copiar `tamv-agent`;
   - generar `config.toml` con `id/next_id/prev_id`;
   - crear supervisor (systemd, sidecar Docker o script CI/CD) para mantener el proceso vivo.
3. Persistir `state.json` junto al binario o en volumen dedicado.

## Siguientes pasos recomendados

- Agregar transporte real BLE/Wi‑Fi mesh en módulo `transport`.
- Implementar tipos de mensaje completos: `HELLO`, `CHAIN_STEP`, `CHAIN_REPORT`.
- Añadir verificación anti-replay (ventana de nonces + timestamp skew).
- Integrar selección adaptativa de peers por fiabilidad.
