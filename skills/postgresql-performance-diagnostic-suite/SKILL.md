---
title: PostgreSQL Performance Diagnostic Suite
description: This skill automates PostgreSQL database performance diagnostics by querying
  system catalog views and performance monitoring extensions. It connects via psycopg2
  or the PostgreSQL wire protocol to run diagnostic queries against pg_stat_statements
  for identifying slow queries, pg_stat_activity for active connection analysis, and
  pg_stat_user_tables for table bloat and sequential scan detection. The suite runs
  EXPLAIN ANALYZE on identified slow queries and parses the output to pinpoint missing
  indexes, inefficient joins, and suboptimal query plans. It integrates with pgBadger
  to parse PostgreSQL log files for pattern analysis, identifying peak load periods
  and recurring slow query patterns. The skill checks pg_stat_bgwriter for checkpoint
  frequency issues, analyzes vacuum and autovacuum statistics, and examines lock contention
  via pg_locks. Reports include actionable recommendations with specific CREATE INDEX
  statements, configuration parameter adjustments for shared_buffers, work_mem, and
  effective_cache_size.
verification: security_reviewed
source: https://agentskillexchange.com/skills/postgresql-performance-diagnostic-suite/
category:
- Runbooks &amp; Diagnostics
framework:
- MCP
---

# PostgreSQL Performance Diagnostic Suite

This skill automates PostgreSQL database performance diagnostics by querying system catalog views and performance monitoring extensions. It connects via psycopg2 or the PostgreSQL wire protocol to run diagnostic queries against pg_stat_statements for identifying slow queries, pg_stat_activity for active connection analysis, and pg_stat_user_tables for table bloat and sequential scan detection. The suite runs EXPLAIN ANALYZE on identified slow queries and parses the output to pinpoint missing indexes, inefficient joins, and suboptimal query plans. It integrates with pgBadger to parse PostgreSQL log files for pattern analysis, identifying peak load periods and recurring slow query patterns. The skill checks pg_stat_bgwriter for checkpoint frequency issues, analyzes vacuum and autovacuum statistics, and examines lock contention via pg_locks. Reports include actionable recommendations with specific CREATE INDEX statements, configuration parameter adjustments for shared_buffers, work_mem, and effective_cache_size.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-performance-diagnostic-suite/)
