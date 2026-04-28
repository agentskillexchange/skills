---
title: PostgreSQL Slow Query Analyzer
description: Queries pg_stat_statements and pg_stat_activity to surface the top slow
  queries by total execution time, mean latency, and call frequency. Runs EXPLAIN
  ANALYZE on worst offenders and suggests index additions, rewrite candidates, or
  vacuum triggers. Works on RDS and Supabase.
verification: security_reviewed
source: https://www.npmjs.com/package/pg
category:
- Runbooks & Diagnostics
framework:
- MCP
tool_ecosystem:
  npm_package: pg
  npm_weekly_downloads: 23169914
---

# PostgreSQL Slow Query Analyzer

Queries pg_stat_statements and pg_stat_activity to surface the top slow queries by total execution time, mean latency, and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrite candidates, or vacuum triggers. Works on RDS and Supabase.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/postgresql-slow-query-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-slow-query-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/postgresql-slow-query-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-slow-query-analyzer/)
