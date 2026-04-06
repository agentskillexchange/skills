---
name: PostgreSQL Performance Runbook
description: Executes diagnostic queries against PostgreSQL using pg_stat_statements,
  pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention,
  bloated tables via pgstattuple, and generates EXPLAIN ANALYZE reports with buffer
  statistics.
category: "Runbooks &amp; Diagnostics"
framework: Codex
verification: security_reviewed
source: "https://agentskillexchange.com/skills/postgresql-performance-runbook/"
---
# PostgreSQL Performance Runbook

Executes diagnostic queries against PostgreSQL using pg_stat_statements, pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention, bloated tables via pgstattuple, and generates EXPLAIN ANALYZE reports with buffer statistics.

The PostgreSQL Performance Runbook skill automates database performance diagnostics by querying PostgreSQL system catalog views and extensions. It connects via libpq and runs a structured diagnostic sequence.

The skill queries pg_stat_statements for top queries by total_exec_time and mean_exec_time, pg_stat_activity for active/idle-in-transaction sessions, pg_locks joined with pg_stat_activity for lock contention analysis, and pg_stat_user_tables for sequential scan heavy tables needing indexes.

Advanced diagnostics include: pgstattuple extension queries for table and index bloat estimation, pg_stat_bgwriter for checkpoint frequency analysis, pg_stat_wal for WAL generation rate, and pg_stat_replication for replica lag measurement.

For identified slow queries, the skill generates EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) output with interpretation of nested loop vs hash join choices, bitmap scan effectiveness, and sort memory spillage. It recommends specific CREATE INDEX statements, work_mem adjustments, and vacuum parameter tuning.

The runbook output is structured with severity levels (critical/warning/info) and includes specific configuration parameter recommendations with pg_reload_conf() safety notes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-runbook -a codex
```

### OpenClaw

```bash
clawhub install postgresql-performance-runbook
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-performance-runbook/)
