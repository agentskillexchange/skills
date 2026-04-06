---
name: PostgreSQL Slow Query Runbook
description: Diagnoses PostgreSQL slow queries using pg_stat_statements extension,
  EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis.
  Identifies missing indexes, sequential scan bottlenecks, and lock contention issues.
category: "Runbooks &amp; Diagnostics"
framework: OpenClaw
verification: security_reviewed
source: "https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/"
---
# PostgreSQL Slow Query Runbook

Diagnoses PostgreSQL slow queries using pg_stat_statements extension, EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis. Identifies missing indexes, sequential scan bottlenecks, and lock contention issues.

The PostgreSQL Slow Query Runbook Agent automates the diagnosis of database performance issues using PostgreSQL’s built-in monitoring extensions. It queries the pg_stat_statements view to identify the top resource-consuming queries by total_exec_time, mean_exec_time, and calls frequency.

The agent runs EXPLAIN ANALYZE on identified slow queries, parsing the execution plan tree to detect sequential scans on large tables, nested loop joins with high row estimates, and sort operations spilling to disk. It cross-references the plan with pg_stat_user_indexes to identify unused indexes consuming write overhead and missing indexes that would benefit frequent query patterns.

For lock contention analysis, it queries pg_stat_activity joined with pg_locks to identify blocking PIDs, lock types (RowExclusiveLock, AccessShareLock), and wait event details. The agent checks table bloat ratios using pgstattuple extension functions, analyzes autovacuum effectiveness via pg_stat_user_tables dead tuple counts, and reviews connection pool status through pgbouncer SHOW POOLS command output. Remediation runbooks include specific CREATE INDEX recommendations with estimated improvement percentages, vacuum tuning parameters, and query rewrite suggestions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-runbook-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-runbook-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-runbook-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-runbook-agent -a codex
```

### OpenClaw

```bash
clawhub install postgresql-slow-query-runbook-agent
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/)
