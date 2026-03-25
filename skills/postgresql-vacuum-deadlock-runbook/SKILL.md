---
name: "PostgreSQL Vacuum Deadlock Runbook"
description: "Automates PostgreSQL vacuum and autovacuum troubleshooting via pg_stat_user_tables, pg_locks, and pg_stat_activity views. Detects table bloat using pgstattuple extension and generates remediation SQL for long-running transaction conflicts."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-vacuum-deadlock-runbook/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "postgresql"  # from ase_tool_match
  npm_weekly_downloads: 21413502  # from ase_npm_downloads
---

# PostgreSQL Vacuum Deadlock Runbook

Automates PostgreSQL vacuum and autovacuum troubleshooting via pg_stat_user_tables, pg_locks, and pg_stat_activity views. Detects table bloat using pgstattuple extension and generates remediation SQL for long-running transaction conflicts.

## Overview

Overview

The PostgreSQL Vacuum Deadlock Runbook automates diagnosis and resolution of vacuum-related issues in PostgreSQL databases. It queries system catalog views to identify table bloat, long-running transactions blocking autovacuum, and lock contention patterns that degrade database performance.

Key Capabilities

This skill uses `pg_stat_user_tables` to monitor dead tuple accumulation, last vacuum timestamps, and autovacuum trigger thresholds. It queries `pg_locks` joined with `pg_stat_activity` to detect blocking relationships and identify transactions holding AccessExclusiveLock that prevent vacuum operations. The `pgstattuple` extension provides precise table and index bloat measurements.

Remediation Actions

Generates parameterized SQL for adjusting per-table autovacuum settings including `autovacuum_vacuum_scale_factor`, `autovacuum_vacuum_cost_delay`, and `autovacuum_freeze_max_age`. Handles wraparound vacuum emergencies by identifying tables approaching the 2-billion transaction ID limit and provides safe termination queries for blocking backends.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-vacuum-deadlock-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-vacuum-deadlock-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-vacuum-deadlock-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-vacuum-deadlock-runbook -a codex
```

### OpenClaw

```bash
clawhub install postgresql-vacuum-deadlock-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/postgresql-vacuum-deadlock-runbook/
