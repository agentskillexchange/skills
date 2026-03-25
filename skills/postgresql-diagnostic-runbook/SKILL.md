---
name: "PostgreSQL Diagnostic Runbook"
description: "Diagnoses PostgreSQL performance issues using pg_stat_statements, pg_stat_activity, and the pgbadger log analyzer. Identifies slow queries, lock contention, and bloat via pgstattuple extension."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/postgresql-diagnostic-runbook/"
tool_ecosystem:
  tool: "postgresql"
  npm_weekly_downloads: 21413502
---

# PostgreSQL Diagnostic Runbook

Diagnoses PostgreSQL performance issues using pg_stat_statements, pg_stat_activity, and the pgbadger log analyzer. Identifies slow queries, lock contention, and bloat via pgstattuple extension.

## Overview

The PostgreSQL Diagnostic Runbook skill automates the investigation of PostgreSQL database performance problems. It queries pg_stat_statements for identifying top resource-consuming queries by total time, calls, and shared block hits. The pg_stat_activity view is monitored for active query analysis, connection state distribution, and long-running transaction detection. Integration with pgbadger provides log-based analysis including query pattern classification, error rate trending, and connection statistics. The skill uses the pgstattuple extension to measure table and index bloat percentages, identifying candidates for VACUUM or REINDEX operations. Lock contention analysis queries pg_locks joined with pg_stat_activity to build lock dependency graphs and detect potential deadlock chains. Additional diagnostics include checkpoint frequency analysis via pg_stat_bgwriter, buffer cache hit ratio calculation, WAL generation rate monitoring, and replication lag measurement through pg_stat_replication. The runbook generates prioritized remediation recommendations including index creation suggestions based on sequential scan patterns, configuration parameter tuning (work_mem, shared_buffers, effective_cache_size), and query rewrite proposals. Output is formatted as structured diagnostic reports with severity classifications.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-diagnostic-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-diagnostic-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-diagnostic-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-diagnostic-runbook -a codex
```

### OpenClaw

```bash
clawhub install postgresql-diagnostic-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/postgresql-diagnostic-runbook/
