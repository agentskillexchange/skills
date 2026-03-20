---
name: PostgreSQL Slow Query Runbook
description: Identifies slow queries in PostgreSQL by querying pg_stat_statements and pg_stat_activity via the PostgreSQL information schema and psycopg2. Correlates query plans from EXPLAIN ANALYZE with table blo
category: Runbooks & Diagnostics
framework: Claude Agents
verification: security_reviewed
rating: 4.8
reviews: 76
source: https://agentskillexchange.com/skill/postgresql-slow-query-runbook/
---

# PostgreSQL Slow Query Runbook

Identifies slow queries in PostgreSQL by querying pg_stat_statements and pg_stat_activity via the PostgreSQL information schema and psycopg2. Correlates query plans from EXPLAIN ANALYZE with table bloat metrics from pgstattuple. Outputs an actionable runbook with index recommendations and vacuum scheduling.

## Overview

This skill connects to a PostgreSQL database using psycopg2 and queries the pg_stat_statements extension to identify queries with the highest mean execution time and total I/O blocks. It fetches active long-running queries from pg_stat_activity filtered by state and wait_event_type. For the top 5 offending queries, the skill runs EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) to capture execution plans and identifies sequential scans on large tables. Table and index bloat is measured via the pgstattuple extension. The skill generates CREATE INDEX CONCURRENTLY statements for missing indexes, autovacuum threshold adjustment recommendations based on n_dead_tup from pg_stat_user_tables, and a maintenance window schedule for VACUUM ANALYZE. Output is a structured Markdown runbook with copy-paste SQL commands.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-runbook
```

### OpenClaw

```bash
openclaw install postgresql-slow-query-runbook
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Claude Agents |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (76 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/postgresql-slow-query-runbook/)*
