---
title: "PostgreSQL Performance Diagnostic Suite"
description: "Diagnoses PostgreSQL performance issues using pg_stat_statements, pg_stat_activity, and EXPLAIN ANALYZE. Integrates with pgBadger for log analysis and pg_stat_user_tables for index recommendations."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Performance Diagnostic Suite

This skill automates PostgreSQL database performance diagnostics by querying system catalog views and performance monitoring extensions. It connects via psycopg2 or the PostgreSQL wire protocol to run diagnostic queries against pg_stat_statements for identifying slow queries, pg_stat_activity for active connection analysis, and pg_stat_user_tables for table bloat and sequential scan detection. The suite runs EXPLAIN ANALYZE on identified slow queries and parses the output to pinpoint missing indexes, inefficient joins, and suboptimal query plans. It integrates with pgBadger to parse PostgreSQL log files for pattern analysis, identifying peak load periods and recurring slow query patterns. The skill checks pg_stat_bgwriter for checkpoint frequency issues, analyzes vacuum and autovacuum statistics, and examines lock contention via pg_locks. Reports include actionable recommendations with specific CREATE INDEX statements, configuration parameter adjustments for shared_buffers, work_mem, and effective_cache_size.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/postgresql-performance-diagnostic-suite/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-performance-diagnostic-suite
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/postgresql-performance-diagnostic-suite`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-performance-diagnostic-suite/)
