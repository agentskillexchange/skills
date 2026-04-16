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
  ase_npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Diagnostic Runbook

The PostgreSQL Diagnostic Runbook skill automates the investigation of PostgreSQL database performance problems. It queries pg_stat_statements for identifying top resource-consuming queries by total time, calls, and shared block hits. The pg_stat_activity view is monitored for active query analysis, connection state distribution, and long-running transaction detection. Integration with pgbadger provides log-based analysis including query pattern classification, error rate trending, and connection statistics. The skill uses the pgstattuple extension to measure table and index bloat percentages, identifying candidates for VACUUM or REINDEX operations. Lock contention analysis queries pg_locks joined with pg_stat_activity to build lock dependency graphs and detect potential deadlock chains. Additional diagnostics include checkpoint frequency analysis via pg_stat_bgwriter, buffer cache hit ratio calculation, WAL generation rate monitoring, and replication lag measurement through pg_stat_replication. The runbook generates prioritized remediation recommendations including index creation suggestions based on sequential scan patterns, configuration parameter tuning (work_mem, shared_buffers, effective_cache_size), and query rewrite proposals. Output is formatted as structured diagnostic reports with severity classifications.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-diagnostic-runbook/)
