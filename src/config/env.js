import dotenv from 'dotenv';

dotenv.config();

export const env = {
  port: Number(process.env.PORT || 3000),
  db: process.env.DB || 'postgresql://postgres:postgres@localhost:5432/tamv'
};
