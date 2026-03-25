---
name: "PostgreSQL Slow Query Analyzer"
description: "Queries pg_stat_statements and pg_stat_activity to surface the top slow queries by total execution time, mean latency, and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrite candidates, or vacuum triggers. Works on RDS and Supabase."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/postgresql-slow-query-analyzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "postgresql"  # from ase_tool_match
  npm_weekly_downloads: 21413502  # from ase_npm_downloads
---

# PostgreSQL Slow Query Analyzer

Queries pg_stat_statements and pg_stat_activity to surface the top slow queries by total execution time, mean latency, and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrite candidates, or vacuum triggers. Works on RDS and Supabase.

## Overview

Queries pg_stat_statements and pg_stat_activity to surface the top slow queries by total execution time, mean latency, and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrite candidates, or vacuum triggers. Works on RDS and Supabase.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-analyzer -a codex
```

### OpenClaw

```bash
clawhub install postgresql-slow-query-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/postgresql-slow-query-analyzer/
