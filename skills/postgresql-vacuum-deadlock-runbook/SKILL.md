---
title: PostgreSQL Vacuum Deadlock Runbook
description: Overview The PostgreSQL Vacuum Deadlock Runbook automates diagnosis and
  resolution of vacuum-related issues in PostgreSQL databases. It queries system catalog
  views to identify table bloat, long-running transactions blocking autovacuum, and
  lock contention patterns that degrade database performance. Key Capabilities This
  skill uses pg_stat_user_tables to monitor dead tuple accumulation, last vacuum timestamps,
  and autovacuum trigger thresholds. It queries pg_locks joined with pg_stat_activity
  to detect blocking relationships and identify transactions holding AccessExclusiveLock
  that prevent vacuum operations. The pgstattuple extension provides precise table
  and index bloat measurements. Remediation Actions Generates parameterized SQL for
  adjusting per-table autovacuum settings including autovacuum_vacuum_scale_factor
  , autovacuum_vacuum_cost_delay , and autovacuum_freeze_max_age . Handles wraparound
  vacuum emergencies by identifying tables approaching the 2-billion transaction ID
  limit and provides safe termination queries for blocking backends.
verification: security_reviewed
source: https://agentskillexchange.com/skills/postgresql-vacuum-deadlock-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- Claude Agents
---

# PostgreSQL Vacuum Deadlock Runbook

Overview The PostgreSQL Vacuum Deadlock Runbook automates diagnosis and resolution of vacuum-related issues in PostgreSQL databases. It queries system catalog views to identify table bloat, long-running transactions blocking autovacuum, and lock contention patterns that degrade database performance. Key Capabilities This skill uses pg_stat_user_tables to monitor dead tuple accumulation, last vacuum timestamps, and autovacuum trigger thresholds. It queries pg_locks joined with pg_stat_activity to detect blocking relationships and identify transactions holding AccessExclusiveLock that prevent vacuum operations. The pgstattuple extension provides precise table and index bloat measurements. Remediation Actions Generates parameterized SQL for adjusting per-table autovacuum settings including autovacuum_vacuum_scale_factor , autovacuum_vacuum_cost_delay , and autovacuum_freeze_max_age . Handles wraparound vacuum emergencies by identifying tables approaching the 2-billion transaction ID limit and provides safe termination queries for blocking backends.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-vacuum-deadlock-runbook/)
