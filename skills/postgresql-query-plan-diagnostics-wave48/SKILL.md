---
title: "PostgreSQL Query Plan Diagnostics"
description: "Analyzes PostgreSQL query execution plans using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) and the pg_stat_statements extension. Identifies sequential scans, nested loop inefficiencies, and index recommendations for slow queries."
slug: "postgresql-query-plan-diagnostics-wave48"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/postgresql-query-plan-diagnostics-wave48/"
listed: true
---

# PostgreSQL Query Plan Diagnostics

Analyzes PostgreSQL query execution plans using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) and the pg_stat_statements extension. Identifies sequential scans, nested loop inefficiencies, and index recommendations for slow queries.

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
clawhub install postgresql-query-plan-diagnostics-wave48
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The PostgreSQL Query Plan Diagnostics skill provides deep analysis of PostgreSQL query execution plans to identify performance bottlenecks. It uses EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) to capture actual execution statistics and parses the resulting plan tree to highlight problematic nodes.
The skill connects to PostgreSQL via psycopg2 or asyncpg and retrieves slow query candidates from the pg_stat_statements extension, sorted by total_exec_time or mean_exec_time. For each candidate, it executes EXPLAIN ANALYZE within a transaction that is rolled back to capture plan data without side effects on write queries.
Key diagnostic capabilities include detection of sequential scans on large tables that would benefit from indexes, identification of nested loop joins with high row multipliers that suggest missing join indexes, and hash aggregate memory spill detection where work_mem is insufficient. The skill calculates plan node cost ratios to highlight where the optimizer’s estimates diverge significantly from actual row counts.
Advanced features include index recommendation using hypothetical indexes via the HypoPG extension, table bloat analysis using pgstattuple, wait event analysis from pg_stat_activity for lock contention diagnosis, and generation of pg_hint_plan hints for cases where the optimizer needs manual guidance. Results include visual plan tree rendering and actionable SQL commands for implementing fixes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-plan-diagnostics-wave48/)
