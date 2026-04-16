---
title: "PostgreSQL Slow Query Runbook"
description: "Diagnoses PostgreSQL slow queries using pg_stat_statements extension, EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis. Identifies missing indexes, sequential scan bottlenecks, and lock contention issues."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  ase_npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Slow Query Runbook

The PostgreSQL Slow Query Runbook Agent automates the diagnosis of database performance issues using PostgreSQL’s built-in monitoring extensions. It queries the pg_stat_statements view to identify the top resource-consuming queries by total_exec_time, mean_exec_time, and calls frequency.


The agent runs EXPLAIN ANALYZE on identified slow queries, parsing the execution plan tree to detect sequential scans on large tables, nested loop joins with high row estimates, and sort operations spilling to disk. It cross-references the plan with pg_stat_user_indexes to identify unused indexes consuming write overhead and missing indexes that would benefit frequent query patterns.


For lock contention analysis, it queries pg_stat_activity joined with pg_locks to identify blocking PIDs, lock types (RowExclusiveLock, AccessShareLock), and wait event details. The agent checks table bloat ratios using pgstattuple extension functions, analyzes autovacuum effectiveness via pg_stat_user_tables dead tuple counts, and reviews connection pool status through pgbouncer SHOW POOLS command output. Remediation runbooks include specific CREATE INDEX recommendations with estimated improvement percentages, vacuum tuning parameters, and query rewrite suggestions.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/)
