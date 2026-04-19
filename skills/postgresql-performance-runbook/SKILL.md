---
title: "PostgreSQL Performance Runbook"
description: "The PostgreSQL Performance Runbook skill automates database performance diagnostics by querying PostgreSQL system catalog views and extensions. It connects via libpq and runs a structured diagnostic sequence. The skill queries pg_stat_statements for top queries by total_exec_time and mean_exec_time, pg_stat_activity for active/idle-in-transaction sessions, pg_locks joined with pg_stat_activity for lock contention analysis, and pg_stat_user_tables for sequential scan heavy tables needing indexes. Advanced diagnostics include: pgstattuple extension queries for table and index bloat estimation, pg_stat_bgwriter for checkpoint frequency analysis, pg_stat_wal for WAL generation rate, and pg_stat_replication for replica lag measurement. For identified slow queries, the skill generates EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) output with interpretation of nested loop vs hash join choices, bitmap scan effectiveness, and sort memory spillage. It recommends specific CREATE INDEX statements, work_mem adjustments, and vacuum parameter tuning. The runbook output is structured with severity levels (critical/warning/info) and includes specific configuration parameter recommendations with pg_reload_conf() safety notes."
source: "https://www.npmjs.com/package/pg"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Codex"
tool_ecosystem:
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Performance Runbook

The PostgreSQL Performance Runbook skill automates database performance diagnostics by querying PostgreSQL system catalog views and extensions. It connects via libpq and runs a structured diagnostic sequence. The skill queries pg_stat_statements for top queries by total_exec_time and mean_exec_time, pg_stat_activity for active/idle-in-transaction sessions, pg_locks joined with pg_stat_activity for lock contention analysis, and pg_stat_user_tables for sequential scan heavy tables needing indexes. Advanced diagnostics include: pgstattuple extension queries for table and index bloat estimation, pg_stat_bgwriter for checkpoint frequency analysis, pg_stat_wal for WAL generation rate, and pg_stat_replication for replica lag measurement. For identified slow queries, the skill generates EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) output with interpretation of nested loop vs hash join choices, bitmap scan effectiveness, and sort memory spillage. It recommends specific CREATE INDEX statements, work_mem adjustments, and vacuum parameter tuning. The runbook output is structured with severity levels (critical/warning/info) and includes specific configuration parameter recommendations with pg_reload_conf() safety notes.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-performance-runbook/)
