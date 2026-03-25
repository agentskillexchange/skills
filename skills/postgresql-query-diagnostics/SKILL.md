---
name: "PostgreSQL Query Diagnostics"
description: "Diagnoses slow PostgreSQL queries using pg_stat_statements, pg_stat_activity, and EXPLAIN ANALYZE output parsing. Integrates with the pgBadger log analyzer and pg_stat_user_tables for index recommendation."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-query-diagnostics/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "postgresql"  # from ase_tool_match
  npm_weekly_downloads: 21413502  # from ase_npm_downloads
---

# PostgreSQL Query Diagnostics

Diagnoses slow PostgreSQL queries using pg_stat_statements, pg_stat_activity, and EXPLAIN ANALYZE output parsing. Integrates with the pgBadger log analyzer and pg_stat_user_tables for index recommendation.

## Overview

The PostgreSQL Query Diagnostics skill automates database performance troubleshooting by querying PostgreSQL system catalogs and statistics views. It leverages pg_stat_statements to identify the most resource-intensive queries by total execution time, calls, and block I/O, and cross-references with pg_stat_activity to detect long-running or blocked sessions.

This skill parses EXPLAIN ANALYZE output to identify performance bottlenecks including sequential scans on large tables, nested loop joins with high row estimates, and sort operations spilling to disk. It generates optimization recommendations including index suggestions based on pg_stat_user_tables and pg_stat_user_indexes data showing scan patterns.

Integration with pgBadger enables historical log analysis, identifying query patterns over time and correlating performance degradation with specific deployment events. The skill also monitors pg_stat_bgwriter and pg_stat_wal for checkpoint frequency and WAL generation rates that may indicate write amplification.

Additional diagnostics cover connection pool saturation detection, vacuum and autovacuum monitoring through pg_stat_all_tables dead tuple counts, and lock contention analysis via pg_locks joined with pg_stat_activity.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-diagnostics
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-diagnostics -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-diagnostics -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-diagnostics -a codex
```

### OpenClaw

```bash
clawhub install postgresql-query-diagnostics
```

## Source

- Marketplace: https://agentskillexchange.com/skills/postgresql-query-diagnostics/
