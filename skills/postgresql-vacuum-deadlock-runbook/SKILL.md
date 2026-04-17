---
name: PostgreSQL Vacuum Deadlock Runbook
description: Automates PostgreSQL vacuum and autovacuum troubleshooting via pg_stat_user_tables,
  pg_locks, and pg_stat_activity views. Detects table bloat using pgstattuple extension
  and generates remediation SQL for long-running transaction conflicts.
category: Runbooks & Diagnostics
framework: Claude Agents
verification: security_reviewed
source: https://www.npmjs.com/package/pg
tool_ecosystem:
  tool: pg
  npm_weekly_downloads: 23169914
---
# PostgreSQL Vacuum Deadlock Runbook
Automates PostgreSQL vacuum and autovacuum troubleshooting via pg_stat_user_tables, pg_locks, and pg_stat_activity views. Detects table bloat using pgstattuple extension and generates remediation SQL for long-running transaction conflicts.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-vacuum-deadlock-runbook
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/postgresql-vacuum-deadlock-runbook` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-vacuum-deadlock-runbook/)
