---
title: "PostgreSQL Query Diagnostics"
description: "Diagnoses slow PostgreSQL queries using pg_stat_statements, pg_stat_activity, and EXPLAIN ANALYZE output parsing. Integrates with the pgBadger log analyzer and pg_stat_user_tables for index recommendation."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Query Diagnostics

Diagnoses slow PostgreSQL queries using pg_stat_statements, pg_stat_activity, and EXPLAIN ANALYZE output parsing. Integrates with the pgBadger log analyzer and pg_stat_user_tables for index recommendation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/postgresql-query-diagnostics/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-query-diagnostics
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/postgresql-query-diagnostics`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-diagnostics/)
