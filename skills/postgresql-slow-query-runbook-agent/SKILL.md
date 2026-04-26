---
title: "PostgreSQL Slow Query Runbook"
description: "Diagnoses PostgreSQL slow queries using pg_stat_statements extension, EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis. Identifies missing indexes, sequential scan bottlenecks, and lock contention issues."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Slow Query Runbook

Diagnoses PostgreSQL slow queries using pg_stat_statements extension, EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis. Identifies missing indexes, sequential scan bottlenecks, and lock contention issues.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-slow-query-runbook-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/postgresql-slow-query-runbook-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-slow-query-runbook-agent/)
