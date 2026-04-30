import express from 'express';
import cors from 'cors';
import { env } from './config/env.js';
import { dashboardHandler } from './api/dashboard.js';
import { query } from './db/db.js';

const app = express();
app.use(cors());
app.use(express.json());

app.get('/', (_req, res) => {
  res.json({ service: 'tamv-pdos-core', version: '0.1.0' });
});

app.get('/health', async (_req, res) => {
  const pong = await query('SELECT 1 as ok');
  res.json({ ok: pong.rows[0].ok === 1 });
});

app.get('/nodes', async (_req, res) => {
  const rows = await query('SELECT * FROM nodes ORDER BY importance DESC, id ASC');
  res.json(rows.rows);
});

app.get('/repos', async (_req, res) => {
  const rows = await query('SELECT * FROM pdos_repos ORDER BY score DESC, stars DESC');
  res.json(rows.rows);
});

app.post('/dashboard', dashboardHandler);

app.listen(env.port, () => {
  console.log(`tamv-pdos-core running on :${env.port}`);
});
