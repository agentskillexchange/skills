---
title: "PostgreSQL Performance Diagnostics"
description: "Analyzes PostgreSQL query performance using pg_stat_statements, pg_stat_user_tables, and EXPLAIN ANALYZE output. Identifies missing indexes via pg_stat_user_indexes and detects lock contention through pg_locks and pg_stat_activity."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks &amp; Diagnostics"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-performance-diagnostics/)
