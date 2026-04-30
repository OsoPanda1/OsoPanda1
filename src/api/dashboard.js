import { evaluateTelemetry } from '../kernel/orchestrator.js';
import { query } from '../db/db.js';

export async function dashboardHandler(req, res) {
  const payload = req.body || {};
  const decision = evaluateTelemetry(payload);

  await query(
    'INSERT INTO pdos_executions (task, payload, result, status, duration_ms) VALUES ($1, $2::jsonb, $3::jsonb, $4, $5)',
    ['dashboard-eval', JSON.stringify(payload), JSON.stringify(decision), 'completed', 1]
  );

  await query(
    'INSERT INTO pdos_decisions (query, context, decisions, confidence) VALUES ($1, $2::jsonb, $3::jsonb, $4)',
    ['dashboard-routing', JSON.stringify(payload), JSON.stringify(decision.actions), decision.confidence]
  );

  return res.json({ ok: true, decision });
}
