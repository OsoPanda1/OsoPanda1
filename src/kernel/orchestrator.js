export function evaluateTelemetry(payload = {}) {
  const cpu = Number(payload.cpu || 0);
  const memory = Number(payload.memory || 0);

  const actions = [];
  if (cpu > 1.2) actions.push('scale_up_workers');
  if (memory > 75) actions.push('enable_memory_guard');
  if (actions.length === 0) actions.push('keep_stable');

  const confidence = Math.min(0.99, 0.6 + actions.length * 0.1);
  return { cpu, memory, actions, confidence };
}
