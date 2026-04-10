---
name: PostgreSQL Health Diagnostics Agent
description: Queries PostgreSQL system catalogs pg_stat_activity, pg_stat_user_tables,
  and pg_locks to diagnose performance issues. Analyzes slow queries via pg_stat_statements
  and checks vacuum status through pg_stat_all_tables autovacuum columns.
verification: security_reviewed
source: https://agentskillexchange.com/skills/postgresql-health-diagnostics-agent/
category:
- Runbooks &amp; Diagnostics
framework:
- MCP
---
# PostgreSQL Health Diagnostics Agent

The PostgreSQL Health Diagnostics Agent performs comprehensive database health checks by querying PostgreSQL system catalogs and statistics views. It connects via libpq protocol and inspects pg_stat_activity to identify long-running queries, blocked sessions, and connection pool saturation. The agent analyzes query performance through pg_stat_statements, ranking queries by total_exec_time, calls, and mean_exec_time to surface optimization candidates. It checks index health via pg_stat_user_indexes to find unused indexes consuming disk space and missing indexes indicated by sequential scan ratios in pg_stat_user_tables. Table bloat is estimated by comparing pg_class.relpages against actual row counts, while vacuum health is monitored through last_autovacuum and n_dead_tup columns in pg_stat_all_tables. Lock contention analysis uses pg_locks joined with pg_stat_activity to identify blocking chains. The diagnostics agent also checks replication lag via pg_stat_replication, validates WAL archiving status, and monitors tablespace usage for capacity planning.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-health-diagnostics-agent/)
