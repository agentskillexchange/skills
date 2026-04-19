---
title: "PostgreSQL Slow Query Runbook"
description: "The PostgreSQL Slow Query Runbook Agent automates the diagnosis of database performance issues using PostgreSQL&#8217;s built-in monitoring extensions. It queries the pg_stat_statements view to identify the top resource-consuming queries by total_exec_time, mean_exec_time, and calls frequency. The agent runs EXPLAIN ANALYZE on identified slow queries, parsing the execution plan tree to detect sequential scans on large tables, nested loop joins with high row estimates, and sort operations spilling to disk. It cross-references the plan with pg_stat_user_indexes to identify unused indexes consuming write overhead and missing indexes that would benefit frequent query patterns. For lock contention analysis, it queries pg_stat_activity joined with pg_locks to identify blocking PIDs, lock types (RowExclusiveLock, AccessShareLock), and wait event details. The agent checks table bloat ratios using pgstattuple extension functions, analyzes autovacuum effectiveness via pg_stat_user_tables dead tuple counts, and reviews connection pool status through pgbouncer SHOW POOLS command output. Remediation runbooks include specific CREATE INDEX recommendations with estimated improvement percentages, vacuum tuning parameters, and query rewrite suggestions."
source: "https://www.npmjs.com/package/pg"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Slow Query Runbook

The PostgreSQL Slow Query Runbook Agent automates the diagnosis of database performance issues using PostgreSQL&#8217;s built-in monitoring extensions. It queries the pg_stat_statements view to identify the top resource-consuming queries by total_exec_time, mean_exec_time, and calls frequency. The agent runs EXPLAIN ANALYZE on identified slow queries, parsing the execution plan tree to detect sequential scans on large tables, nested loop joins with high row estimates, and sort operations spilling to disk. It cross-references the plan with pg_stat_user_indexes to identify unused indexes consuming write overhead and missing indexes that would benefit frequent query patterns. For lock contention analysis, it queries pg_stat_activity joined with pg_locks to identify blocking PIDs, lock types (RowExclusiveLock, AccessShareLock), and wait event details. The agent checks table bloat ratios using pgstattuple extension functions, analyzes autovacuum effectiveness via pg_stat_user_tables dead tuple counts, and reviews connection pool status through pgbouncer SHOW POOLS command output. Remediation runbooks include specific CREATE INDEX recommendations with estimated improvement percentages, vacuum tuning parameters, and query rewrite suggestions.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/)
