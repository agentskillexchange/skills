---
title: PostgreSQL Performance Diagnostics
description: The PostgreSQL Performance Diagnostics skill provides comprehensive database
  performance analysis by querying PostgreSQL system catalogs and statistics views.
  It connects via psycopg2 or asyncpg to collect metrics from pg_stat_statements for
  identifying slow queries, high-frequency queries, and queries with poor hit ratios.
  Index analysis queries pg_stat_user_indexes and pg_stat_user_tables to identify
  unused indexes consuming write overhead, missing indexes causing sequential scans
  on large tables, and bloated indexes needing REINDEX. The skill runs EXPLAIN (ANALYZE,
  BUFFERS, FORMAT JSON) on flagged queries to examine execution plans, highlighting
  nested loop joins on large datasets and sort operations spilling to disk. Lock contention
  detection monitors pg_locks joined with pg_stat_activity to identify blocking chains,
  long-running transactions holding AccessExclusiveLocks, and deadlock patterns. Connection
  pool analysis checks pgbouncer stats or pg_stat_activity connection counts against
  max_connections settings. The diagnostic report includes specific configuration
  recommendations for shared_buffers, work_mem, effective_cache_size, and autovacuum
  tuning based on observed workload patterns.
verification: security_reviewed
source: https://agentskillexchange.com/skills/postgresql-performance-diagnostics/
category:
- Runbooks &amp; Diagnostics
framework:
- MCP
---

# PostgreSQL Performance Diagnostics

The PostgreSQL Performance Diagnostics skill provides comprehensive database performance analysis by querying PostgreSQL system catalogs and statistics views. It connects via psycopg2 or asyncpg to collect metrics from pg_stat_statements for identifying slow queries, high-frequency queries, and queries with poor hit ratios. Index analysis queries pg_stat_user_indexes and pg_stat_user_tables to identify unused indexes consuming write overhead, missing indexes causing sequential scans on large tables, and bloated indexes needing REINDEX. The skill runs EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) on flagged queries to examine execution plans, highlighting nested loop joins on large datasets and sort operations spilling to disk. Lock contention detection monitors pg_locks joined with pg_stat_activity to identify blocking chains, long-running transactions holding AccessExclusiveLocks, and deadlock patterns. Connection pool analysis checks pgbouncer stats or pg_stat_activity connection counts against max_connections settings. The diagnostic report includes specific configuration recommendations for shared_buffers, work_mem, effective_cache_size, and autovacuum tuning based on observed workload patterns.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-performance-diagnostics/)
