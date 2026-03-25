---
name: "PostgreSQL Query Plan Analyzer"
description: "Executes EXPLAIN ANALYZE BUFFERS on slow PostgreSQL queries and parses the plan tree for sequential scans, nested loop joins, and sort spills. Integrates with pg_stat_statements for identifying top resource-consuming queries."
category: "Developer Tools"
framework: "Claude Code"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-query-plan-analyzer-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "postgresql"  # from ase_tool_match
  npm_weekly_downloads: 21413502  # from ase_npm_downloads
---

# PostgreSQL Query Plan Analyzer

Executes EXPLAIN ANALYZE BUFFERS on slow PostgreSQL queries and parses the plan tree for sequential scans, nested loop joins, and sort spills. Integrates with pg_stat_statements for identifying top resource-consuming queries.

## Overview

The PostgreSQL Query Plan Analyzer skill provides deep query performance diagnostics for PostgreSQL databases. It executes EXPLAIN with ANALYZE, BUFFERS, and FORMAT JSON on target queries to capture actual execution times, row estimates vs actuals, and buffer hit ratios. The skill parses the JSON plan tree to identify performance anti-patterns including sequential scans on large tables, nested loop joins with high row multipliers, hash joins exceeding work_mem, and sort operations overflowing to temporary files. It queries pg_stat_statements to rank queries by total execution time, calls count, and mean latency. The skill analyzes index usage via pg_stat_user_indexes to detect unused indexes and suggests covering indexes for frequent query patterns. Output includes visual plan tree annotation, index recommendations, and configuration tuning suggestions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-analyzer-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-analyzer-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-analyzer-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-analyzer-2 -a codex
```

### OpenClaw

```bash
clawhub install postgresql-query-plan-analyzer-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/postgresql-query-plan-analyzer-2/
