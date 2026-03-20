---
name: PostgreSQL Slow Query Runbook
description: Diagnoses PostgreSQL slow queries using pg_stat_statements extension, EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis. Identifies missing indexes, sequential scan bottlenecks, and lock contention issues.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.1
reviews: 86
source: https://agentskillexchange.com/skill/postgresql-slow-query-runbook-agent/
---

# PostgreSQL Slow Query Runbook

Diagnoses PostgreSQL slow queries using pg_stat_statements extension, EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis. Identifies missing indexes, sequential scan bottlenecks, and lock contention issues.

## Overview

Diagnoses PostgreSQL slow queries using pg_stat_statements extension, EXPLAIN ANALYZE output parsing, and pg_stat_user_indexes for index usage analysis. Identifies missing indexes, sequential scan bottlenecks, and lock contention issues.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill postgresql-slow-query-runbook-agent
```

### OpenClaw

```bash
clawhub install postgresql-slow-query-runbook-agent
```

### Claude Code

```bash
claude mcp add postgresql-slow-query-runbook-agent
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/postgresql-slow-query-runbook-agent/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.1/5 (86 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/postgresql-slow-query-runbook-agent/)
