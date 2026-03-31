---
name: "PostgreSQL Query Plan Diagnostics"
description: "Analyzes PostgreSQL query execution plans using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) and the pg_stat_statements extension. Identifies sequential scans, nested loop inefficiencies, and index recommendations for slow queries."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/postgresql-query-plan-diagnostics-wave48/"
---
# PostgreSQL Query Plan Diagnostics

Analyzes PostgreSQL query execution plans using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) and the pg_stat_statements extension. Identifies sequential scans, nested loop inefficiencies, and index recommendations for slow queries.

## Overview

The PostgreSQL Query Plan Diagnostics skill provides deep analysis of PostgreSQL query execution plans to identify performance bottlenecks. It uses EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) to capture actual execution statistics and parses the resulting plan tree to highlight problematic nodes.

The skill connects to PostgreSQL via psycopg2 or asyncpg and retrieves slow query candidates from the pg_stat_statements extension, sorted by total_exec_time or mean_exec_time. For each candidate, it executes EXPLAIN ANALYZE within a transaction that is rolled back to capture plan data without side effects on write queries.

Key diagnostic capabilities include detection of sequential scans on large tables that would benefit from indexes, identification of nested loop joins with high row multipliers that suggest missing join indexes, and hash aggregate memory spill detection where work_mem is insufficient. The skill calculates plan node cost ratios to highlight where the optimizer’s estimates diverge significantly from actual row counts.

Advanced features include index recommendation using hypothetical indexes via the HypoPG extension, table bloat analysis using pgstattuple, wait event analysis from pg_stat_activity for lock contention diagnosis, and generation of pg_hint_plan hints for cases where the optimizer needs manual guidance. Results include visual plan tree rendering and actionable SQL commands for implementing fixes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-diagnostics-wave48
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-diagnostics-wave48 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-diagnostics-wave48 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-diagnostics-wave48 -a codex
```

### OpenClaw

```bash
clawhub install postgresql-query-plan-diagnostics-wave48
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-plan-diagnostics-wave48/)
