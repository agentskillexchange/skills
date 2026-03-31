---
name: "PostgreSQL Performance Diagnostics"
description: "Analyzes PostgreSQL query performance using pg_stat_statements, pg_stat_user_tables, and EXPLAIN ANALYZE output. Identifies missing indexes via pg_stat_user_indexes and detects lock contention through pg_locks and pg_stat_activity."
category: "Runbooks &amp; Diagnostics"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/postgresql-performance-diagnostics/"
---
# PostgreSQL Performance Diagnostics

Analyzes PostgreSQL query performance using pg_stat_statements, pg_stat_user_tables, and EXPLAIN ANALYZE output. Identifies missing indexes via pg_stat_user_indexes and detects lock contention through pg_locks and pg_stat_activity.

## Overview

The PostgreSQL Performance Diagnostics skill provides comprehensive database performance analysis by querying PostgreSQL system catalogs and statistics views. It connects via psycopg2 or asyncpg to collect metrics from pg_stat_statements for identifying slow queries, high-frequency queries, and queries with poor hit ratios.

Index analysis queries pg_stat_user_indexes and pg_stat_user_tables to identify unused indexes consuming write overhead, missing indexes causing sequential scans on large tables, and bloated indexes needing REINDEX. The skill runs EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) on flagged queries to examine execution plans, highlighting nested loop joins on large datasets and sort operations spilling to disk.

Lock contention detection monitors pg_locks joined with pg_stat_activity to identify blocking chains, long-running transactions holding AccessExclusiveLocks, and deadlock patterns. Connection pool analysis checks pgbouncer stats or pg_stat_activity connection counts against max_connections settings. The diagnostic report includes specific configuration recommendations for shared_buffers, work_mem, effective_cache_size, and autovacuum tuning based on observed workload patterns.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-diagnostics
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-diagnostics -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-diagnostics -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-diagnostics -a codex
```

### OpenClaw

```bash
clawhub install postgresql-performance-diagnostics
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-performance-diagnostics/)
