-- TAMV Digital Nexus: núcleo de conocimiento para el repo principal.

CREATE TABLE IF NOT EXISTS nodes (
  id SERIAL PRIMARY KEY,
  slug TEXT UNIQUE NOT NULL,
  type TEXT NOT NULL DEFAULT 'concept',
  title TEXT NOT NULL,
  importance INT DEFAULT 50,
  metadata JSONB DEFAULT '{}'::jsonb
);

CREATE TABLE IF NOT EXISTS edges (
  id SERIAL PRIMARY KEY,
  from_node_id INT REFERENCES nodes(id) ON DELETE CASCADE,
  to_node_id INT REFERENCES nodes(id) ON DELETE CASCADE,
  relation_type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pdos_repos (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL,
  category TEXT DEFAULT 'general',
  stars INT DEFAULT 0,
  forks INT DEFAULT 0,
  score NUMERIC DEFAULT 0,
  role TEXT,
  metadata JSONB DEFAULT '{}'::jsonb
);

CREATE TABLE IF NOT EXISTS pdos_executions (
  id SERIAL PRIMARY KEY,
  task TEXT NOT NULL,
  payload JSONB DEFAULT '{}'::jsonb,
  result JSONB DEFAULT '{}'::jsonb,
  status TEXT DEFAULT 'pending',
  duration_ms INT,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS pdos_decisions (
  id SERIAL PRIMARY KEY,
  query TEXT,
  context JSONB DEFAULT '{}'::jsonb,
  decisions JSONB DEFAULT '[]'::jsonb,
  confidence NUMERIC DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT now()
);

INSERT INTO nodes (slug, type, title, importance) VALUES
  ('tamv-core', 'system', 'TAMV Core', 100),
  ('isabella', 'system', 'Isabella IA', 95),
  ('nodo-cero', 'identity', 'Nodo Cero', 100),
  ('rdm-digital', 'system', 'RDM Digital OS', 90)
ON CONFLICT (slug) DO NOTHING;

INSERT INTO pdos_repos (name, category, stars, forks, score, role) VALUES
  ('kubernetes', 'orchestration', 108000, 40000, 0.98, 'core orchestrator'),
  ('postgres', 'database', 15000, 4500, 0.95, 'primary store'),
  ('redis', 'cache', 65000, 23000, 0.92, 'event bus + cache'),
  ('react', 'frontend', 227000, 46000, 0.97, 'UI runtime'),
  ('vite', 'build', 68000, 6000, 0.93, 'dev server'),
  ('deno', 'runtime', 94000, 5200, 0.90, 'edge runtime'),
  ('langchain', 'ai', 92000, 15000, 0.88, 'RAG framework'),
  ('pgvector', 'vector-db', 12000, 700, 0.91, 'embeddings store')
ON CONFLICT (name) DO UPDATE SET
  category = EXCLUDED.category,
  stars = EXCLUDED.stars,
  forks = EXCLUDED.forks,
  score = EXCLUDED.score,
  role = EXCLUDED.role;
