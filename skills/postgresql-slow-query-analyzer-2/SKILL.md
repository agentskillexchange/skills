---
name: PostgreSQL Slow Query Analyzer
description: Queries pg_stat_statements and pg_stat_activity to surface top slow queries by execution time and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrites, or vacuum triggers. Works on RDS, Supabase, and self-hosted Postgres.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.4
reviews: 83
source: https://agentskillexchange.com/skill/postgresql-slow-query-analyzer-2/
---

# PostgreSQL Slow Query Analyzer

Queries pg_stat_statements and pg_stat_activity to surface top slow queries by execution time and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrites, or vacuum triggers. Works on RDS, Supabase, and self-hosted Postgres.

## Overview

Queries pg_stat_statements and pg_stat_activity to surface top slow queries by execution time and call frequency. Runs EXPLAIN ANALYZE on worst offenders and suggests index additions, rewrites, or vacuum triggers. Works on RDS, Supabase, and self-hosted Postgres.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-analyzer-2
```

### OpenClaw

```bash
clawhub install postgresql-slow-query-analyzer-2
```

### Claude Code

```bash
claude mcp add postgresql-slow-query-analyzer-2
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/postgresql-slow-query-analyzer-2/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.4/5 (83 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/postgresql-slow-query-analyzer-2/)
