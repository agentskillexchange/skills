---
title: "PostgreSQL Vacuum Deadlock Runbook"
description: "Automates PostgreSQL vacuum and autovacuum troubleshooting via pg_stat_user_tables, pg_locks, and pg_stat_activity views. Detects table bloat using pgstattuple extension and generates remediation SQL for long-running transaction conflicts."
verification: security_reviewed
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  ase_npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Vacuum Deadlock Runbook

Overview The PostgreSQL Vacuum Deadlock Runbook automates diagnosis and resolution of vacuum-related issues in PostgreSQL databases. It queries system catalog views to identify table bloat, long-running transactions blocking autovacuum, and lock contention patterns that degrade database performance.

Key Capabilities This skill uses pg_stat_user_tables to monitor dead tuple accumulation, last vacuum timestamps, and autovacuum trigger thresholds. It queries pg_locks joined with pg_stat_activity to detect blocking relationships and identify transactions holding AccessExclusiveLock that prevent vacuum operations. The pgstattuple extension provides precise table and index bloat measurements.

Remediation Actions Generates parameterized SQL for adjusting per-table autovacuum settings including autovacuum_vacuum_scale_factor, autovacuum_vacuum_cost_delay, and autovacuum_freeze_max_age. Handles wraparound vacuum emergencies by identifying tables approaching the 2-billion transaction ID limit and provides safe termination queries for blocking backends.

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
