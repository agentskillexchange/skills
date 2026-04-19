---
title: "PostgreSQL Health Diagnostics Agent"
description: "The PostgreSQL Health Diagnostics Agent performs comprehensive database health checks by querying PostgreSQL system catalogs and statistics views. It connects via libpq protocol and inspects pg_stat_activity to identify long-running queries, blocked sessions, and connection pool saturation. The agent analyzes query performance through pg_stat_statements, ranking queries by total_exec_time, calls, and mean_exec_time to surface optimization candidates. It checks index health via pg_stat_user_indexes to find unused indexes consuming disk space and missing indexes indicated by sequential scan ratios in pg_stat_user_tables. Table bloat is estimated by comparing pg_class.relpages against actual row counts, while vacuum health is monitored through last_autovacuum and n_dead_tup columns in pg_stat_all_tables. Lock contention analysis uses pg_locks joined with pg_stat_activity to identify blocking chains. The diagnostics agent also checks replication lag via pg_stat_replication, validates WAL archiving status, and monitors tablespace usage for capacity planning."
source: "https://www.npmjs.com/package/pg"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Health Diagnostics Agent

The PostgreSQL Health Diagnostics Agent performs comprehensive database health checks by querying PostgreSQL system catalogs and statistics views. It connects via libpq protocol and inspects pg_stat_activity to identify long-running queries, blocked sessions, and connection pool saturation. The agent analyzes query performance through pg_stat_statements, ranking queries by total_exec_time, calls, and mean_exec_time to surface optimization candidates. It checks index health via pg_stat_user_indexes to find unused indexes consuming disk space and missing indexes indicated by sequential scan ratios in pg_stat_user_tables. Table bloat is estimated by comparing pg_class.relpages against actual row counts, while vacuum health is monitored through last_autovacuum and n_dead_tup columns in pg_stat_all_tables. Lock contention analysis uses pg_locks joined with pg_stat_activity to identify blocking chains. The diagnostics agent also checks replication lag via pg_stat_replication, validates WAL archiving status, and monitors tablespace usage for capacity planning.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-health-diagnostics-agent/)
