---
title: "PostgreSQL Performance Diagnostics"
description: "Analyzes PostgreSQL query performance using pg_stat_statements, pg_stat_user_tables, and EXPLAIN ANALYZE output. Identifies missing indexes via pg_stat_user_indexes and detects lock contention through pg_locks and pg_stat_activity."
verification: security_reviewed
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  ase_npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Performance Diagnostics

The PostgreSQL Performance Diagnostics skill provides comprehensive database performance analysis by querying PostgreSQL system catalogs and statistics views. It connects via psycopg2 or asyncpg to collect metrics from pg_stat_statements for identifying slow queries, high-frequency queries, and queries with poor hit ratios.

Index analysis queries pg_stat_user_indexes and pg_stat_user_tables to identify unused indexes consuming write overhead, missing indexes causing sequential scans on large tables, and bloated indexes needing REINDEX. The skill runs EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) on flagged queries to examine execution plans, highlighting nested loop joins on large datasets and sort operations spilling to disk.

Lock contention detection monitors pg_locks joined with pg_stat_activity to identify blocking chains, long-running transactions holding AccessExclusiveLocks, and deadlock patterns. Connection pool analysis checks pgbouncer stats or pg_stat_activity connection counts against max_connections settings. The diagnostic report includes specific configuration recommendations for shared_buffers, work_mem, effective_cache_size, and autovacuum tuning based on observed workload patterns.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-performance-diagnostics
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/postgresql-performance-diagnostics` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-performance-diagnostics/)
