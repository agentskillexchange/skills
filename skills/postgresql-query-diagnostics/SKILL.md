---
title: "PostgreSQL Query Diagnostics"
description: "Diagnoses slow PostgreSQL queries using pg_stat_statements, pg_stat_activity, and EXPLAIN ANALYZE output parsing. Integrates with the pgBadger log analyzer and pg_stat_user_tables for index recommendation."
slug: "postgresql-query-diagnostics"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/postgresql-query-diagnostics/"
listed: true
---

# PostgreSQL Query Diagnostics

Diagnoses slow PostgreSQL queries using pg_stat_statements, pg_stat_activity, and EXPLAIN ANALYZE output parsing. Integrates with the pgBadger log analyzer and pg_stat_user_tables for index recommendation.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install postgresql-query-diagnostics
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The PostgreSQL Query Diagnostics skill automates database performance troubleshooting by querying PostgreSQL system catalogs and statistics views. It leverages pg_stat_statements to identify the most resource-intensive queries by total execution time, calls, and block I/O, and cross-references with pg_stat_activity to detect long-running or blocked sessions.
This skill parses EXPLAIN ANALYZE output to identify performance bottlenecks including sequential scans on large tables, nested loop joins with high row estimates, and sort operations spilling to disk. It generates optimization recommendations including index suggestions based on pg_stat_user_tables and pg_stat_user_indexes data showing scan patterns.
Integration with pgBadger enables historical log analysis, identifying query patterns over time and correlating performance degradation with specific deployment events. The skill also monitors pg_stat_bgwriter and pg_stat_wal for checkpoint frequency and WAL generation rates that may indicate write amplification.
Additional diagnostics cover connection pool saturation detection, vacuum and autovacuum monitoring through pg_stat_all_tables dead tuple counts, and lock contention analysis via pg_locks joined with pg_stat_activity.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-diagnostics/)
