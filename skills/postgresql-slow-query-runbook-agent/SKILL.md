---
name: PostgreSQL Slow Query Runbook
description: Diagnoses PostgreSQL slow queries using pg_stat_statements extension,
  EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis.
  Identifies missing indexes, sequential scan bottlenecks, and lock contention issues.
verification: security_reviewed
source: https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---
# PostgreSQL Slow Query Runbook

The PostgreSQL Slow Query Runbook Agent automates the diagnosis of database performance issues using PostgreSQL's built-in monitoring extensions. It queries the pg_stat_statements view to identify the top resource-consuming queries by total_exec_time, mean_exec_time, and calls frequency.
The agent runs EXPLAIN ANALYZE on identified slow queries, parsing the execution plan tree to detect sequential scans on large tables, nested loop joins with high row estimates, and sort operations spilling to disk. It cross-references the plan with pg_stat_user_indexes to identify unused indexes consuming write overhead and missing indexes that would benefit frequent query patterns.
For lock contention analysis, it queries pg_stat_activity joined with pg_locks to identify blocking PIDs, lock types (RowExclusiveLock, AccessShareLock), and wait event details. The agent checks table bloat ratios using pgstattuple extension functions, analyzes autovacuum effectiveness via pg_stat_user_tables dead tuple counts, and reviews connection pool status through pgbouncer SHOW POOLS command output. Remediation runbooks include specific CREATE INDEX recommendations with estimated improvement percentages, vacuum tuning parameters, and query rewrite suggestions.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/)
