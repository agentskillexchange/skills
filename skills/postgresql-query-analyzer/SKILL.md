---
name: "PostgreSQL Query Analyzer"
description: "Analyzes PostgreSQL slow queries using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output and pg_stat_statements views. Identifies missing indexes via pg_stat_user_tables sequential scan counters and suggests index creation with HypoPG extension."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-query-analyzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "postgresql"  # from ase_tool_match
  npm_weekly_downloads: 21413502  # from ase_npm_downloads
---

# PostgreSQL Query Analyzer

Analyzes PostgreSQL slow queries using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output and pg_stat_statements views. Identifies missing indexes via pg_stat_user_tables sequential scan counters and suggests index creation with HypoPG extension.

## Overview

The PostgreSQL Query Analyzer skill provides deep performance analysis for PostgreSQL databases by examining query execution plans and runtime statistics. It processes EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output to identify performance bottlenecks including sequential scans on large tables, nested loop joins with high row estimates, and excessive buffer hits.

The skill queries pg_stat_statements to identify the top resource-consuming queries by total execution time, mean latency, and shared buffer usage. It correlates this data with pg_stat_user_tables to find tables with high sequential scan ratios that would benefit from indexing.

For index recommendations, the skill uses the HypoPG extension to create hypothetical indexes and re-run EXPLAIN to validate that proposed indexes would actually improve query performance before creating them. It supports B-tree, GiST, GIN, and BRIN index type recommendations based on column data types and query patterns.

Additional diagnostics include lock contention analysis via pg_stat_activity and pg_locks, connection pool utilization tracking, vacuum and autovacuum status monitoring, and table bloat estimation using pgstattuple. The skill generates actionable reports with SQL commands for implementing recommended optimizations.

Compatible with PostgreSQL 13+ and works with both self-hosted and managed instances (RDS, Cloud SQL, Azure Database).

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-analyzer -a codex
```

### OpenClaw

```bash
clawhub install postgresql-query-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/postgresql-query-analyzer/
