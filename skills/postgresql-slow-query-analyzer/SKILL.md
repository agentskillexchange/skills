---
name: PostgreSQL Slow Query Analyzer
description: Queries pg_stat_statements and pg_stat_activity to surface the top slow queries by total execution time, mean latency, and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrite candidates, or vacuum triggers. Works on RDS and Supabase.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: listed
rating: 4.8
reviews: 80
source: https://agentskillexchange.com/skill/postgresql-slow-query-analyzer/
---

# PostgreSQL Slow Query Analyzer

Queries pg_stat_statements and pg_stat_activity to surface the top slow queries by total execution time, mean latency, and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrite candidates, or vacuum triggers. Works on RDS and Supabase.

## Overview

Queries pg_stat_statements and pg_stat_activity to surface the top slow queries by total execution time, mean latency, and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrite candidates, or vacuum triggers. Works on RDS and Supabase.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-analyzer
```

### OpenClaw

```bash
clawhub install postgresql-slow-query-analyzer
```

### Claude Code

```bash
claude mcp add postgresql-slow-query-analyzer
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/postgresql-slow-query-analyzer/) for detailed installation instructions.

## Verification

- **Status**: listed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.8/5 (80 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/postgresql-slow-query-analyzer/)
