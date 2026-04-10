---
name: PostgreSQL Diagnostic Runbook
description: Diagnoses PostgreSQL performance issues using pg_stat_statements, pg_stat_activity,
  and the pgbadger log analyzer. Identifies slow queries, lock contention, and bloat
  via pgstattuple extension.
verification: security_reviewed
source: https://agentskillexchange.com/skills/postgresql-diagnostic-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- ChatGPT Agents
---
# PostgreSQL Diagnostic Runbook

The PostgreSQL Diagnostic Runbook skill automates the investigation of PostgreSQL database performance problems. It queries pg_stat_statements for identifying top resource-consuming queries by total time, calls, and shared block hits. The pg_stat_activity view is monitored for active query analysis, connection state distribution, and long-running transaction detection. Integration with pgbadger provides log-based analysis including query pattern classification, error rate trending, and connection statistics. The skill uses the pgstattuple extension to measure table and index bloat percentages, identifying candidates for VACUUM or REINDEX operations. Lock contention analysis queries pg_locks joined with pg_stat_activity to build lock dependency graphs and detect potential deadlock chains. Additional diagnostics include checkpoint frequency analysis via pg_stat_bgwriter, buffer cache hit ratio calculation, WAL generation rate monitoring, and replication lag measurement through pg_stat_replication. The runbook generates prioritized remediation recommendations including index creation suggestions based on sequential scan patterns, configuration parameter tuning (work_mem, shared_buffers, effective_cache_size), and query rewrite proposals. Output is formatted as structured diagnostic reports with severity classifications.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-diagnostic-runbook/)
