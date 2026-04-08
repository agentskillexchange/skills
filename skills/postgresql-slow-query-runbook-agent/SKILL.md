---
title: PostgreSQL Slow Query Runbook
description: The PostgreSQL Slow Query Runbook Agent automates the diagnosis of database
  performance issues using PostgreSQL’s built-in monitoring extensions. It queries
  the pg_stat_statements view to identify the top resource-consuming queries by total_exec_time,
  mean_exec_time, and calls frequency. The agent runs EXPLAIN ANALYZE on identified
  slow queries, parsing the execution plan tree to detect sequential scans on large
  tables, nested loop joins with high row estimates, and sort operations spilling
  to disk. It cross-references the plan with pg_stat_user_indexes to identify unused
  indexes consuming write overhead and missing indexes that would benefit frequent
  query patterns. For lock contention analysis, it queries pg_stat_activity joined
  with pg_locks to identify blocking PIDs, lock types (RowExclusiveLock, AccessShareLock),
  and wait event details. The agent checks table bloat ratios using pgstattuple extension
  functions, analyzes autovacuum effectiveness via pg_stat_user_tables dead tuple
  counts, and reviews connection pool status through pgbouncer SHOW POOLS command
  output. Remediation runbooks include specific CREATE INDEX recommendations with
  estimated improvement percentages, vacuum tuning parameters, and query rewrite suggestions.
verification: security_reviewed
source: https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---

# PostgreSQL Slow Query Runbook

The PostgreSQL Slow Query Runbook Agent automates the diagnosis of database performance issues using PostgreSQL’s built-in monitoring extensions. It queries the pg_stat_statements view to identify the top resource-consuming queries by total_exec_time, mean_exec_time, and calls frequency. The agent runs EXPLAIN ANALYZE on identified slow queries, parsing the execution plan tree to detect sequential scans on large tables, nested loop joins with high row estimates, and sort operations spilling to disk. It cross-references the plan with pg_stat_user_indexes to identify unused indexes consuming write overhead and missing indexes that would benefit frequent query patterns. For lock contention analysis, it queries pg_stat_activity joined with pg_locks to identify blocking PIDs, lock types (RowExclusiveLock, AccessShareLock), and wait event details. The agent checks table bloat ratios using pgstattuple extension functions, analyzes autovacuum effectiveness via pg_stat_user_tables dead tuple counts, and reviews connection pool status through pgbouncer SHOW POOLS command output. Remediation runbooks include specific CREATE INDEX recommendations with estimated improvement percentages, vacuum tuning parameters, and query rewrite suggestions.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/)
