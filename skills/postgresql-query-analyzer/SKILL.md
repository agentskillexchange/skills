---
title: "PostgreSQL Query Analyzer"
description: "The PostgreSQL Query Analyzer skill provides deep performance analysis for PostgreSQL databases by examining query execution plans and runtime statistics. It processes EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output to identify performance bottlenecks including sequential scans on large tables, nested loop joins with high row estimates, and excessive buffer hits.\nThe skill queries pg_stat_statements to identify the top resource-consuming queries by total execution time, mean latency, and shared buffer usage. It correlates this data with pg_stat_user_tables to find tables with high sequential scan ratios that would benefit from indexing.\nFor index recommendations, the skill uses the HypoPG extension to create hypothetical indexes and re-run EXPLAIN to validate that proposed indexes would actually improve query performance before creating them. It supports B-tree, GiST, GIN, and BRIN index type recommendations based on column data types and query patterns.\nAdditional diagnostics include lock contention analysis via pg_stat_activity and pg_locks, connection pool utilization tracking, vacuum and autovacuum status monitoring, and table bloat estimation using pgstattuple. The skill generates actionable reports with SQL commands for implementing recommended optimizations.\nCompatible with PostgreSQL 13+ and works with both self-hosted and managed instances (RDS, Cloud SQL, Azure Database)."
verification: security_reviewed
source: "https://www.npmjs.com/package/pg"
framework:
  - "Gemini"
tool_ecosystem:
  ase_npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Query Analyzer

The PostgreSQL Query Analyzer skill provides deep performance analysis for PostgreSQL databases by examining query execution plans and runtime statistics. It processes EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output to identify performance bottlenecks including sequential scans on large tables, nested loop joins with high row estimates, and excessive buffer hits.
The skill queries pg_stat_statements to identify the top resource-consuming queries by total execution time, mean latency, and shared buffer usage. It correlates this data with pg_stat_user_tables to find tables with high sequential scan ratios that would benefit from indexing.
For index recommendations, the skill uses the HypoPG extension to create hypothetical indexes and re-run EXPLAIN to validate that proposed indexes would actually improve query performance before creating them. It supports B-tree, GiST, GIN, and BRIN index type recommendations based on column data types and query patterns.
Additional diagnostics include lock contention analysis via pg_stat_activity and pg_locks, connection pool utilization tracking, vacuum and autovacuum status monitoring, and table bloat estimation using pgstattuple. The skill generates actionable reports with SQL commands for implementing recommended optimizations.
Compatible with PostgreSQL 13+ and works with both self-hosted and managed instances (RDS, Cloud SQL, Azure Database).

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-query-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/postgresql-query-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-analyzer/)
