---
name: PostgreSQL Health Diagnostics Agent
description: Queries PostgreSQL system catalogs pg_stat_activity, pg_stat_user_tables,
  and pg_locks to diagnose performance issues. Analyzes slow queries via pg_stat_statements
  and checks vacuum status through pg_stat_all_tables autovacuum columns.
category: Runbooks & Diagnostics
framework: MCP
verification: security_reviewed
source: https://www.npmjs.com/package/pg
tool_ecosystem:
  tool: pg
  npm_weekly_downloads: 23169914
---
# PostgreSQL Health Diagnostics Agent
Queries PostgreSQL system catalogs pg_stat_activity, pg_stat_user_tables, and pg_locks to diagnose performance issues. Analyzes slow queries via pg_stat_statements and checks vacuum status through pg_stat_all_tables autovacuum columns.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-health-diagnostics-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/postgresql-health-diagnostics-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-health-diagnostics-agent/)
