---
title: "PostgreSQL Query Analyzer"
description: "Analyzes PostgreSQL slow queries using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output and pg_stat_statements views. Identifies missing indexes via pg_stat_user_tables sequential scan counters and suggests index creation with HypoPG extension."
verification: security_reviewed
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Query Analyzer

Analyzes PostgreSQL slow queries using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) output and pg_stat_statements views. Identifies missing indexes via pg_stat_user_tables sequential scan counters and suggests index creation with HypoPG extension.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/postgresql-query-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-query-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/postgresql-query-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-analyzer/)
