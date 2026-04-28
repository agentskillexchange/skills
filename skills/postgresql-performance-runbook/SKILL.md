---
title: PostgreSQL Performance Runbook
description: Executes diagnostic queries against PostgreSQL using pg_stat_statements,
  pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention,
  bloated tables via pgstattuple, and generates EXPLAIN ANALYZE reports with buffer
  statistics.
verification: security_reviewed
source: https://www.npmjs.com/package/pg
category:
- Runbooks & Diagnostics
framework:
- Codex
tool_ecosystem:
  npm_package: pg
  npm_weekly_downloads: 23169914
---

# PostgreSQL Performance Runbook

Executes diagnostic queries against PostgreSQL using pg_stat_statements, pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention, bloated tables via pgstattuple, and generates EXPLAIN ANALYZE reports with buffer statistics.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/postgresql-performance-runbook/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-performance-runbook
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/postgresql-performance-runbook`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-performance-runbook/)
