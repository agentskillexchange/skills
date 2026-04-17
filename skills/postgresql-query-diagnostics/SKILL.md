---
name: PostgreSQL Query Diagnostics
description: Diagnoses slow PostgreSQL queries using pg_stat_statements, pg_stat_activity,
  and EXPLAIN ANALYZE output parsing. Integrates with the pgBadger log analyzer and
  pg_stat_user_tables for index recommendation.
category: Runbooks & Diagnostics
framework: Claude Agents
verification: security_reviewed
source: https://www.npmjs.com/package/pg
tool_ecosystem:
  tool: pg
  npm_weekly_downloads: 23169914
---
# PostgreSQL Query Diagnostics
Diagnoses slow PostgreSQL queries using pg_stat_statements, pg_stat_activity, and EXPLAIN ANALYZE output parsing. Integrates with the pgBadger log analyzer and pg_stat_user_tables for index recommendation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-query-diagnostics
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/postgresql-query-diagnostics` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-diagnostics/)
