---
name: "PostgreSQL Query Plan Explainer"
description: "Interprets PostgreSQL EXPLAIN ANALYZE output using pg_stat_statements and auto_explain module data. Identifies sequential scan bottlenecks, index recommendations via HypoPG, and buffer cache hit ratios."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-query-plan-explainer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "postgresql"  # from ase_tool_match
  npm_weekly_downloads: 21413502  # from ase_npm_downloads
---

# PostgreSQL Query Plan Explainer

Interprets PostgreSQL EXPLAIN ANALYZE output using pg_stat_statements and auto_explain module data. Identifies sequential scan bottlenecks, index recommendations via HypoPG, and buffer cache hit ratios.

## Overview

The PostgreSQL Query Plan Explainer skill transforms raw EXPLAIN ANALYZE output into actionable database performance recommendations. It parses the query plan tree to identify costly nodes including sequential scans on large tables, nested loop joins with high row estimates, and sort operations spilling to disk.

The skill queries pg_stat_statements to correlate plan analysis with historical query performance metrics including mean execution time, total calls, and shared buffer hits. It uses the auto_explain module configuration to capture slow query plans automatically at configurable thresholds.

Index recommendations leverage HypoPG (hypopg.readthedocs.io) to simulate hypothetical indexes without creating them, testing B-tree, GiST, and GIN index types against the query workload. The skill calculates expected cost reduction percentages for each recommended index.

Buffer cache analysis computes hit ratios from pg_stat_user_tables (heap_blks_hit vs heap_blks_read) and flags tables with poor cache residency. Connection pooling recommendations reference PgBouncer configuration parameters for transaction-mode vs session-mode pooling decisions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-explainer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-explainer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-explainer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-explainer -a codex
```

### OpenClaw

```bash
clawhub install postgresql-query-plan-explainer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/postgresql-query-plan-explainer/
