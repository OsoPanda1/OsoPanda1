# TAMV-PDOS Core v0.1

Planetary Dev Operating System — Core ejecutable.

Integra: grafo de conocimiento + Isabella IA (RAG) + orquestador + UI JSON dinámica + catálogo de repos.

## Quick start

```bash
cp .env.example .env
docker compose up --build
# en otra terminal
docker compose exec api npm run seed
```

## Endpoints

- `GET /` — info
- `GET /health` — DB ping
- `GET /nodes` — grafo
- `GET /repos` — catálogo PDOS
- `POST /dashboard` — orquestador (body: telemetría JSON)

## Probar

```bash
curl -X POST localhost:3000/dashboard \
  -H "Content-Type: application/json" \
  -d '{"cpu":1.5,"memory":60}'
```

## Bridge con Lovable

Las mismas tablas (`pdos_repos`, `pdos_executions`, `pdos_decisions`) viven también en el proyecto Supabase de Lovable. Puedes apuntar este core al Postgres de Supabase usando `DB=postgresql://...supabase.co:5432/postgres` y compartir estado con `/pdos-core` en la app web.

## Estructura

```text
src/
├── api/dashboard.js
├── kernel/orchestrator.js
├── ai/{isabella-core,embeddings}.js
├── knowledge/{retrieval,repo-loader}.js
├── ui/generator.js
├── db/{db,seed}.js
└── config/env.js
```

## Roadmap v0.2

- pgvector + embeddings reales
- LLM real (OpenAI / Ollama / Lovable AI Gateway)
- Agentes especializados (seguridad, economía)
- Scraper GitHub para auto-poblar `pdos_repos`
- Frontend React (ya existe en Lovable bajo `/pdos-core`)
