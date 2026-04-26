---
title: "PostgreSQL Query Plan Explainer"
description: "Interprets PostgreSQL EXPLAIN ANALYZE output using pg_stat_statements and auto_explain module data. Identifies sequential scan bottlenecks, index recommendations via HypoPG, and buffer cache hit ratios."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Query Plan Explainer

Interprets PostgreSQL EXPLAIN ANALYZE output using pg_stat_statements and auto_explain module data. Identifies sequential scan bottlenecks, index recommendations via HypoPG, and buffer cache hit ratios.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/postgresql-query-plan-explainer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-query-plan-explainer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/postgresql-query-plan-explainer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-plan-explainer/)
