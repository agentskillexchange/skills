---
name: PostgreSQL Diagnostic Analyzer
description: Runs diagnostic queries against PostgreSQL using pg_stat_statements,
  pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention,
  and bloat using pgstattuple and pg_repack extension analysis.
category: Runbooks & Diagnostics
framework: Gemini
verification: security_reviewed
source: https://www.npmjs.com/package/pg
tool_ecosystem:
  tool: pg
  npm_weekly_downloads: 23169914
---
# PostgreSQL Diagnostic Analyzer
Runs diagnostic queries against PostgreSQL using pg_stat_statements, pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention, and bloat using pgstattuple and pg_repack extension analysis.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-diagnostic-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/postgresql-diagnostic-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-diagnostic-analyzer/)
