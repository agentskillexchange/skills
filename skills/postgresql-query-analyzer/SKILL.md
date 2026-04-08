---
title: PostgreSQL Query Analyzer
description: The PostgreSQL Query Analyzer skill provides deep performance analysis
  for PostgreSQL databases by examining query execution plans and runtime statistics.
  It processes EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output to identify performance
  bottlenecks including sequential scans on large tables, nested loop joins with high
  row estimates, and excessive buffer hits. The skill queries pg_stat_statements to
  identify the top resource-consuming queries by total execution time, mean latency,
  and shared buffer usage. It correlates this data with pg_stat_user_tables to find
  tables with high sequential scan ratios that would benefit from indexing. For index
  recommendations, the skill uses the HypoPG extension to create hypothetical indexes
  and re-run EXPLAIN to validate that proposed indexes would actually improve query
  performance before creating them. It supports B-tree, GiST, GIN, and BRIN index
  type recommendations based on column data types and query patterns. Additional diagnostics
  include lock contention analysis via pg_stat_activity and pg_locks, connection pool
  utilization tracking, vacuum and autovacuum status monitoring, and table bloat estimation
  using pgstattuple. The skill generates actionable reports with SQL commands for
  implementing recommended optimizations. Compatible with PostgreSQL 13+ and works
  with both self-hosted and managed instances (RDS, Cloud SQL, Azure Database).
verification: security_reviewed
source: https://agentskillexchange.com/skills/postgresql-query-analyzer/
category:
- Runbooks &amp; Diagnostics
framework:
- Gemini
---

# PostgreSQL Query Analyzer

The PostgreSQL Query Analyzer skill provides deep performance analysis for PostgreSQL databases by examining query execution plans and runtime statistics. It processes EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output to identify performance bottlenecks including sequential scans on large tables, nested loop joins with high row estimates, and excessive buffer hits. The skill queries pg_stat_statements to identify the top resource-consuming queries by total execution time, mean latency, and shared buffer usage. It correlates this data with pg_stat_user_tables to find tables with high sequential scan ratios that would benefit from indexing. For index recommendations, the skill uses the HypoPG extension to create hypothetical indexes and re-run EXPLAIN to validate that proposed indexes would actually improve query performance before creating them. It supports B-tree, GiST, GIN, and BRIN index type recommendations based on column data types and query patterns. Additional diagnostics include lock contention analysis via pg_stat_activity and pg_locks, connection pool utilization tracking, vacuum and autovacuum status monitoring, and table bloat estimation using pgstattuple. The skill generates actionable reports with SQL commands for implementing recommended optimizations. Compatible with PostgreSQL 13+ and works with both self-hosted and managed instances (RDS, Cloud SQL, Azure Database).

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-analyzer/)
