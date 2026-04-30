import { query, pool } from './db.js';

const repos = [
  ['kubernetes', 'orchestration', 108000, 40000, 0.98, 'core orchestrator'],
  ['postgres', 'database', 15000, 4500, 0.95, 'primary store'],
  ['redis', 'cache', 65000, 23000, 0.92, 'event bus + cache']
];

async function run() {
  for (const repo of repos) {
    await query(
      `INSERT INTO pdos_repos (name, category, stars, forks, score, role)
       VALUES ($1, $2, $3, $4, $5, $6)
       ON CONFLICT (name) DO UPDATE SET
         category = EXCLUDED.category,
         stars = EXCLUDED.stars,
         forks = EXCLUDED.forks,
         score = EXCLUDED.score,
         role = EXCLUDED.role`,
      repo
    );
  }
  console.log('Seed completado');
  await pool.end();
}

run().catch(async (err) => {
  console.error(err);
  await pool.end();
  process.exit(1);
});
