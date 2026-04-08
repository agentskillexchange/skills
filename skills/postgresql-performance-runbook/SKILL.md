---
title: PostgreSQL Performance Runbook
description: 'The PostgreSQL Performance Runbook skill automates database performance
  diagnostics by querying PostgreSQL system catalog views and extensions. It connects
  via libpq and runs a structured diagnostic sequence. The skill queries pg_stat_statements
  for top queries by total_exec_time and mean_exec_time, pg_stat_activity for active/idle-in-transaction
  sessions, pg_locks joined with pg_stat_activity for lock contention analysis, and
  pg_stat_user_tables for sequential scan heavy tables needing indexes. Advanced diagnostics
  include: pgstattuple extension queries for table and index bloat estimation, pg_stat_bgwriter
  for checkpoint frequency analysis, pg_stat_wal for WAL generation rate, and pg_stat_replication
  for replica lag measurement. For identified slow queries, the skill generates EXPLAIN
  (ANALYZE, BUFFERS, FORMAT TEXT) output with interpretation of nested loop vs hash
  join choices, bitmap scan effectiveness, and sort memory spillage. It recommends
  specific CREATE INDEX statements, work_mem adjustments, and vacuum parameter tuning.
  The runbook output is structured with severity levels (critical/warning/info) and
  includes specific configuration parameter recommendations with pg_reload_conf()
  safety notes.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/postgresql-performance-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- Codex
---

# PostgreSQL Performance Runbook

The PostgreSQL Performance Runbook skill automates database performance diagnostics by querying PostgreSQL system catalog views and extensions. It connects via libpq and runs a structured diagnostic sequence. The skill queries pg_stat_statements for top queries by total_exec_time and mean_exec_time, pg_stat_activity for active/idle-in-transaction sessions, pg_locks joined with pg_stat_activity for lock contention analysis, and pg_stat_user_tables for sequential scan heavy tables needing indexes. Advanced diagnostics include: pgstattuple extension queries for table and index bloat estimation, pg_stat_bgwriter for checkpoint frequency analysis, pg_stat_wal for WAL generation rate, and pg_stat_replication for replica lag measurement. For identified slow queries, the skill generates EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) output with interpretation of nested loop vs hash join choices, bitmap scan effectiveness, and sort memory spillage. It recommends specific CREATE INDEX statements, work_mem adjustments, and vacuum parameter tuning. The runbook output is structured with severity levels (critical/warning/info) and includes specific configuration parameter recommendations with pg_reload_conf() safety notes.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-performance-runbook/)
