---
title: "PostgreSQL Diagnostic Runbook"
description: "The PostgreSQL Diagnostic Runbook skill automates the investigation of PostgreSQL database performance problems. It queries pg_stat_statements for identifying top resource-consuming queries by total time, calls, and shared block hits. The pg_stat_activity view is monitored for active query analysis, connection state distribution, and long-running transaction detection. Integration with pgbadger provides log-based analysis including query pattern classification, error rate trending, and connection statistics. The skill uses the pgstattuple extension to measure table and index bloat percentages, identifying candidates for VACUUM or REINDEX operations. Lock contention analysis queries pg_locks joined with pg_stat_activity to build lock dependency graphs and detect potential deadlock chains. Additional diagnostics include checkpoint frequency analysis via pg_stat_bgwriter, buffer cache hit ratio calculation, WAL generation rate monitoring, and replication lag measurement through pg_stat_replication. The runbook generates prioritized remediation recommendations including index creation suggestions based on sequential scan patterns, configuration parameter tuning (work_mem, shared_buffers, effective_cache_size), and query rewrite proposals. Output is formatted as structured diagnostic reports with severity classifications."
source: "https://www.npmjs.com/package/pg"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Diagnostic Runbook

The PostgreSQL Diagnostic Runbook skill automates the investigation of PostgreSQL database performance problems. It queries pg_stat_statements for identifying top resource-consuming queries by total time, calls, and shared block hits. The pg_stat_activity view is monitored for active query analysis, connection state distribution, and long-running transaction detection. Integration with pgbadger provides log-based analysis including query pattern classification, error rate trending, and connection statistics. The skill uses the pgstattuple extension to measure table and index bloat percentages, identifying candidates for VACUUM or REINDEX operations. Lock contention analysis queries pg_locks joined with pg_stat_activity to build lock dependency graphs and detect potential deadlock chains. Additional diagnostics include checkpoint frequency analysis via pg_stat_bgwriter, buffer cache hit ratio calculation, WAL generation rate monitoring, and replication lag measurement through pg_stat_replication. The runbook generates prioritized remediation recommendations including index creation suggestions based on sequential scan patterns, configuration parameter tuning (work_mem, shared_buffers, effective_cache_size), and query rewrite proposals. Output is formatted as structured diagnostic reports with severity classifications.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-diagnostic-runbook/)
