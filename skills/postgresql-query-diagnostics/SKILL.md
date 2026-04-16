---
title: "PostgreSQL Query Diagnostics"
description: "Diagnoses slow PostgreSQL queries using pg_stat_statements, pg_stat_activity, and EXPLAIN ANALYZE output parsing. Integrates with the pgBadger log analyzer and pg_stat_user_tables for index recommendation."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  ase_npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Query Diagnostics

The PostgreSQL Query Diagnostics skill automates database performance troubleshooting by querying PostgreSQL system catalogs and statistics views. It leverages pg_stat_statements to identify the most resource-intensive queries by total execution time, calls, and block I/O, and cross-references with pg_stat_activity to detect long-running or blocked sessions.

This skill parses EXPLAIN ANALYZE output to identify performance bottlenecks including sequential scans on large tables, nested loop joins with high row estimates, and sort operations spilling to disk. It generates optimization recommendations including index suggestions based on pg_stat_user_tables and pg_stat_user_indexes data showing scan patterns.

Integration with pgBadger enables historical log analysis, identifying query patterns over time and correlating performance degradation with specific deployment events. The skill also monitors pg_stat_bgwriter and pg_stat_wal for checkpoint frequency and WAL generation rates that may indicate write amplification.

Additional diagnostics cover connection pool saturation detection, vacuum and autovacuum monitoring through pg_stat_all_tables dead tuple counts, and lock contention analysis via pg_locks joined with pg_stat_activity.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-diagnostics/)
