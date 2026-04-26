---
title: "PostgreSQL Vacuum Deadlock Runbook"
description: "Automates PostgreSQL vacuum and autovacuum troubleshooting via pg_stat_user_tables, pg_locks, and pg_stat_activity views. Detects table bloat using pgstattuple extension and generates remediation SQL for long-running transaction conflicts."
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

# PostgreSQL Vacuum Deadlock Runbook

Automates PostgreSQL vacuum and autovacuum troubleshooting via pg_stat_user_tables, pg_locks, and pg_stat_activity views. Detects table bloat using pgstattuple extension and generates remediation SQL for long-running transaction conflicts.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/postgresql-vacuum-deadlock-runbook/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-vacuum-deadlock-runbook
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/postgresql-vacuum-deadlock-runbook`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-vacuum-deadlock-runbook/)
