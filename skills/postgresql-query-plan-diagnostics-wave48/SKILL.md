---
title: "PostgreSQL Query Plan Diagnostics"
description: "Analyzes PostgreSQL query execution plans using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) and the pg_stat_statements extension. Identifies sequential scans, nested loop inefficiencies, and index recommendations for slow queries."
verification: security_reviewed
source: "https://www.npmjs.com/package/pg"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  ase_npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Query Plan Diagnostics

The PostgreSQL Query Plan Diagnostics skill provides deep analysis of PostgreSQL query execution plans to identify performance bottlenecks. It uses EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) to capture actual execution statistics and parses the resulting plan tree to highlight problematic nodes.

The skill connects to PostgreSQL via psycopg2 or asyncpg and retrieves slow query candidates from the pg_stat_statements extension, sorted by total_exec_time or mean_exec_time. For each candidate, it executes EXPLAIN ANALYZE within a transaction that is rolled back to capture plan data without side effects on write queries.

Key diagnostic capabilities include detection of sequential scans on large tables that would benefit from indexes, identification of nested loop joins with high row multipliers that suggest missing join indexes, and hash aggregate memory spill detection where work_mem is insufficient. The skill calculates plan node cost ratios to highlight where the optimizer’s estimates diverge significantly from actual row counts.

Advanced features include index recommendation using hypothetical indexes via the HypoPG extension, table bloat analysis using pgstattuple, wait event analysis from pg_stat_activity for lock contention diagnosis, and generation of pg_hint_plan hints for cases where the optimizer needs manual guidance. Results include visual plan tree rendering and actionable SQL commands for implementing fixes.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/postgresql-query-plan-diagnostics-wave48
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/postgresql-query-plan-diagnostics-wave48` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-plan-diagnostics-wave48/)
