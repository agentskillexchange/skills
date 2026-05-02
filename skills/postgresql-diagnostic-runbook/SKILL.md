---
title: "PostgreSQL Diagnostic Runbook"
description: "Diagnoses PostgreSQL performance issues using pg_stat_statements, pg_stat_activity, and the pgbadger log analyzer. Identifies slow queries, lock contention, and bloat via pgstattuple extension."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks & Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Diagnostic Runbook

The PostgreSQL Diagnostic Runbook skill automates the investigation of PostgreSQL database performance problems. It queries pg_stat_statements for identifying top resource-consuming queries by total time, calls, and shared block hits. The pg_stat_activity view is monitored for active query analysis, connection state distribution, and long-running transaction detection. Integration with pgbadger provides log-based analysis including query pattern classification, error rate trending, and connection statistics. The skill uses the pgstattuple extension to measure table and index bloat percentages, identifying candidates for VACUUM or REINDEX operations. Lock contention analysis queries pg_locks joined with pg_stat_activity to build lock dependency graphs and detect potential deadlock chains. Additional diagnostics include checkpoint frequency analysis via pg_stat_bgwriter, buffer cache hit ratio calculation, WAL generation rate monitoring, and replication lag measurement through pg_stat_replication. The runbook generates prioritized remediation recommendations including index creation suggestions based on sequential scan patterns, configuration parameter tuning (work_mem, shared_buffers, effective_cache_size), and query rewrite proposals. Output is formatted as structured diagnostic reports with severity classifications.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/postgresql-diagnostic-runbook/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-diagnostic-runbook
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/postgresql-diagnostic-runbook`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-diagnostic-runbook/)
