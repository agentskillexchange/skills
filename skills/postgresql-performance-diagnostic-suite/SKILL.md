---
name: "PostgreSQL Performance Diagnostic Suite"
description: "Diagnoses PostgreSQL performance issues using pg_stat_statements, pg_stat_activity, and EXPLAIN ANALYZE. Integrates with pgBadger for log analysis and pg_stat_user_tables for index recommendations."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/postgresql-performance-diagnostic-suite/"
tool_ecosystem:
  tool: "postgresql"
  npm_weekly_downloads: 21413502
---

# PostgreSQL Performance Diagnostic Suite

Diagnoses PostgreSQL performance issues using pg_stat_statements, pg_stat_activity, and EXPLAIN ANALYZE. Integrates with pgBadger for log analysis and pg_stat_user_tables for index recommendations.

## Overview

This skill automates PostgreSQL database performance diagnostics by querying system catalog views and performance monitoring extensions. It connects via psycopg2 or the PostgreSQL wire protocol to run diagnostic queries against pg_stat_statements for identifying slow queries, pg_stat_activity for active connection analysis, and pg_stat_user_tables for table bloat and sequential scan detection. The suite runs EXPLAIN ANALYZE on identified slow queries and parses the output to pinpoint missing indexes, inefficient joins, and suboptimal query plans. It integrates with pgBadger to parse PostgreSQL log files for pattern analysis, identifying peak load periods and recurring slow query patterns. The skill checks pg_stat_bgwriter for checkpoint frequency issues, analyzes vacuum and autovacuum statistics, and examines lock contention via pg_locks. Reports include actionable recommendations with specific CREATE INDEX statements, configuration parameter adjustments for shared_buffers, work_mem, and effective_cache_size.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-diagnostic-suite
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-diagnostic-suite -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-diagnostic-suite -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-performance-diagnostic-suite -a codex
```

### OpenClaw

```bash
clawhub install postgresql-performance-diagnostic-suite
```

## Source

- Marketplace: https://agentskillexchange.com/skills/postgresql-performance-diagnostic-suite/
