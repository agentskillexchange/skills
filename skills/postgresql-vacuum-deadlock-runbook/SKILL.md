---
title: "PostgreSQL Vacuum Deadlock Runbook"
description: "Overview The PostgreSQL Vacuum Deadlock Runbook automates diagnosis and resolution of vacuum-related issues in PostgreSQL databases. It queries system catalog views to identify table bloat, long-running transactions blocking autovacuum, and lock contention patterns that degrade database performance. Key Capabilities This skill uses pg_stat_user_tables to monitor dead tuple accumulation, last vacuum timestamps, and autovacuum trigger thresholds. It queries pg_locks joined with pg_stat_activity to detect blocking relationships and identify transactions holding AccessExclusiveLock that prevent vacuum operations. The pgstattuple extension provides precise table and index bloat measurements. Remediation Actions Generates parameterized SQL for adjusting per-table autovacuum settings including autovacuum_vacuum_scale_factor , autovacuum_vacuum_cost_delay , and autovacuum_freeze_max_age . Handles wraparound vacuum emergencies by identifying tables approaching the 2-billion transaction ID limit and provides safe termination queries for blocking backends."
source: "https://www.npmjs.com/package/pg"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Vacuum Deadlock Runbook

Overview The PostgreSQL Vacuum Deadlock Runbook automates diagnosis and resolution of vacuum-related issues in PostgreSQL databases. It queries system catalog views to identify table bloat, long-running transactions blocking autovacuum, and lock contention patterns that degrade database performance. Key Capabilities This skill uses pg_stat_user_tables to monitor dead tuple accumulation, last vacuum timestamps, and autovacuum trigger thresholds. It queries pg_locks joined with pg_stat_activity to detect blocking relationships and identify transactions holding AccessExclusiveLock that prevent vacuum operations. The pgstattuple extension provides precise table and index bloat measurements. Remediation Actions Generates parameterized SQL for adjusting per-table autovacuum settings including autovacuum_vacuum_scale_factor , autovacuum_vacuum_cost_delay , and autovacuum_freeze_max_age . Handles wraparound vacuum emergencies by identifying tables approaching the 2-billion transaction ID limit and provides safe termination queries for blocking backends.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-vacuum-deadlock-runbook/)
