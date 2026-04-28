---
title: PostgreSQL Health Diagnostics Agent
description: Queries PostgreSQL system catalogs pg_stat_activity, pg_stat_user_tables,
  and pg_locks to diagnose performance issues. Analyzes slow queries via pg_stat_statements
  and checks vacuum status through pg_stat_all_tables autovacuum columns.
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

# PostgreSQL Health Diagnostics Agent

Queries PostgreSQL system catalogs pg_stat_activity, pg_stat_user_tables, and pg_locks to diagnose performance issues. Analyzes slow queries via pg_stat_statements and checks vacuum status through pg_stat_all_tables autovacuum columns.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/postgresql-health-diagnostics-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-health-diagnostics-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/postgresql-health-diagnostics-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-health-diagnostics-agent/)
