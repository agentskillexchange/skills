---
name: PostgreSQL Query Analyzer
description: Analyzes PostgreSQL slow queries using EXPLAIN (ANALYZE, BUFFERS, FORMAT
  JSON) output and pg_stat_statements views. Identifies missing indexes via pg_stat_user_tables
  sequential scan counters and suggests index creation with HypoPG extension.
category: Runbooks & Diagnostics
framework: Gemini
verification: security_reviewed
source: https://www.npmjs.com/package/pg
tool_ecosystem:
  tool: pg
  npm_weekly_downloads: 23169914
---
# PostgreSQL Query Analyzer
Analyzes PostgreSQL slow queries using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output and pg_stat_statements views. Identifies missing indexes via pg_stat_user_tables sequential scan counters and suggests index creation with HypoPG extension.

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
