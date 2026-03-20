---
name: PostgreSQL Query Plan Diagnostics
description: Analyzes PostgreSQL query execution plans using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) and the pg_stat_statements extension. Identifies sequential scans, nested loop inefficiencies, and index recommendations for slow queries.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.9
reviews: 5
source: https://agentskillexchange.com/skill/postgresql-query-plan-diagnostics-wave48/
---

# PostgreSQL Query Plan Diagnostics

Analyzes PostgreSQL query execution plans using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) and the pg_stat_statements extension. Identifies sequential scans, nested loop inefficiencies, and index recommendations for slow queries.

## Overview

Analyzes PostgreSQL query execution plans using EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) and the pg_stat_statements extension. Identifies sequential scans, nested loop inefficiencies, and index recommendations for slow queries.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-plan-diagnostics-wave48
```

### OpenClaw

```bash
clawhub install postgresql-query-plan-diagnostics-wave48
```

### Claude Code

```bash
claude mcp add postgresql-query-plan-diagnostics-wave48
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/postgresql-query-plan-diagnostics-wave48/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.9/5 (5 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/postgresql-query-plan-diagnostics-wave48/)
