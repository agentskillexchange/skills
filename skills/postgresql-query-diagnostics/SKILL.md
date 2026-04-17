---
title: "PostgreSQL Query Diagnostics"
description: "Diagnoses slow PostgreSQL queries using pg_stat_statements, pg_stat_activity, and EXPLAIN ANALYZE output parsing. Integrates with the pgBadger log analyzer and pg_stat_user_tables for index recommendation."
verification: security_reviewed
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Query Diagnostics

The PostgreSQL Query Diagnostics skill automates database performance troubleshooting by querying PostgreSQL system catalogs and statistics views. It leverages pg_stat_statements to identify the most resource-intensive queries by total execution time, calls, and block I/O, and cross-references with pg_stat_activity to detect long-running or blocked sessions.

This skill parses EXPLAIN ANALYZE output to identify performance bottlenecks including sequential scans on large tables, nested loop joins with high row estimates, and sort operations spilling to disk. It generates optimization recommendations including index suggestions based on pg_stat_user_tables and pg_stat_user_indexes data showing scan patterns.

Integration with pgBadger enables historical log analysis, identifying query patterns over time and correlating performance degradation with specific deployment events. The skill also monitors pg_stat_bgwriter and pg_stat_wal for checkpoint frequency and WAL generation rates that may indicate write amplification.

Additional diagnostics cover connection pool saturation detection, vacuum and autovacuum monitoring through pg_stat_all_tables dead tuple counts, and lock contention analysis via pg_locks joined with pg_stat_activity.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-query-diagnostics
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/postgresql-query-diagnostics` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-diagnostics/)
