---
title: PostgreSQL Query Plan Diagnostics
description: The PostgreSQL Query Plan Diagnostics skill provides deep analysis of
  PostgreSQL query execution plans to identify performance bottlenecks. It uses EXPLAIN
  (ANALYZE, BUFFERS, FORMAT JSON) to capture actual execution statistics and parses
  the resulting plan tree to highlight problematic nodes. The skill connects to PostgreSQL
  via psycopg2 or asyncpg and retrieves slow query candidates from the pg_stat_statements
  extension, sorted by total_exec_time or mean_exec_time. For each candidate, it executes
  EXPLAIN ANALYZE within a transaction that is rolled back to capture plan data without
  side effects on write queries. Key diagnostic capabilities include detection of
  sequential scans on large tables that would benefit from indexes, identification
  of nested loop joins with high row multipliers that suggest missing join indexes,
  and hash aggregate memory spill detection where work_mem is insufficient. The skill
  calculates plan node cost ratios to highlight where the optimizer’s estimates diverge
  significantly from actual row counts. Advanced features include index recommendation
  using hypothetical indexes via the HypoPG extension, table bloat analysis using
  pgstattuple, wait event analysis from pg_stat_activity for lock contention diagnosis,
  and generation of pg_hint_plan hints for cases where the optimizer needs manual
  guidance. Results include visual plan tree rendering and actionable SQL commands
  for implementing fixes.
verification: security_reviewed
source: https://agentskillexchange.com/skills/postgresql-query-plan-diagnostics-wave48/
category:
- Runbooks &amp; Diagnostics
framework:
- Claude Code
---

# PostgreSQL Query Plan Diagnostics

The PostgreSQL Query Plan Diagnostics skill provides deep analysis of PostgreSQL query execution plans to identify performance bottlenecks. It uses EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) to capture actual execution statistics and parses the resulting plan tree to highlight problematic nodes. The skill connects to PostgreSQL via psycopg2 or asyncpg and retrieves slow query candidates from the pg_stat_statements extension, sorted by total_exec_time or mean_exec_time. For each candidate, it executes EXPLAIN ANALYZE within a transaction that is rolled back to capture plan data without side effects on write queries. Key diagnostic capabilities include detection of sequential scans on large tables that would benefit from indexes, identification of nested loop joins with high row multipliers that suggest missing join indexes, and hash aggregate memory spill detection where work_mem is insufficient. The skill calculates plan node cost ratios to highlight where the optimizer’s estimates diverge significantly from actual row counts. Advanced features include index recommendation using hypothetical indexes via the HypoPG extension, table bloat analysis using pgstattuple, wait event analysis from pg_stat_activity for lock contention diagnosis, and generation of pg_hint_plan hints for cases where the optimizer needs manual guidance. Results include visual plan tree rendering and actionable SQL commands for implementing fixes.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-plan-diagnostics-wave48/)
