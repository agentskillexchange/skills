---
title: "PostgreSQL Vacuum Deadlock Runbook"
description: "Automates PostgreSQL vacuum and autovacuum troubleshooting via pg_stat_user_tables, pg_locks, and pg_stat_activity views. Detects table bloat using pgstattuple extension and generates remediation SQL for long-running transaction conflicts."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  ase_npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Vacuum Deadlock Runbook

Overview

The PostgreSQL Vacuum Deadlock Runbook automates diagnosis and resolution of vacuum-related issues in PostgreSQL databases. It queries system catalog views to identify table bloat, long-running transactions blocking autovacuum, and lock contention patterns that degrade database performance.

Key Capabilities

This skill uses pg_stat_user_tables to monitor dead tuple accumulation, last vacuum timestamps, and autovacuum trigger thresholds. It queries pg_locks joined with pg_stat_activity to detect blocking relationships and identify transactions holding AccessExclusiveLock that prevent vacuum operations. The pgstattuple extension provides precise table and index bloat measurements.

Remediation Actions

Generates parameterized SQL for adjusting per-table autovacuum settings including autovacuum_vacuum_scale_factor, autovacuum_vacuum_cost_delay, and autovacuum_freeze_max_age. Handles wraparound vacuum emergencies by identifying tables approaching the 2-billion transaction ID limit and provides safe termination queries for blocking backends.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-vacuum-deadlock-runbook/)
