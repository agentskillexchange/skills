---
name: "PostgreSQL Diagnostic Analyzer"
description: "Runs diagnostic queries against PostgreSQL using pg_stat_statements, pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention, and bloat using pgstattuple and pg_repack extension analysis."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-diagnostic-analyzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "postgresql"  # from ase_tool_match
  npm_weekly_downloads: 21413502  # from ase_npm_downloads
---

# PostgreSQL Diagnostic Analyzer

Runs diagnostic queries against PostgreSQL using pg_stat_statements, pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention, and bloat using pgstattuple and pg_repack extension analysis.

## Overview

The PostgreSQL Diagnostic Analyzer skill performs comprehensive database health assessments by querying PostgreSQL system catalogs and extension views. It connects via the standard libpq protocol and runs a battery of diagnostic queries against pg_stat_statements to identify top resource-consuming queries by total time, mean time, and calls.

The skill analyzes active sessions through pg_stat_activity to detect long-running transactions, idle-in-transaction connections, and waiting queries. It examines pg_locks to identify lock contention patterns, deadlock risks, and blocking chains. Table and index bloat analysis uses pgstattuple extension functions to calculate dead tuple ratios and recommend VACUUM or pg_repack operations.

Additional diagnostics include checking replication lag via pg_stat_replication, analyzing checkpoint frequency through pg_stat_bgwriter, evaluating cache hit ratios from pg_stat_user_tables, and reviewing connection pool utilization. The skill generates structured reports with prioritized recommendations, including specific index creation suggestions based on seq_scan counts and estimated performance impact.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-diagnostic-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-diagnostic-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-diagnostic-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-diagnostic-analyzer -a codex
```

### OpenClaw

```bash
clawhub install postgresql-diagnostic-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/postgresql-diagnostic-analyzer/
