---
name: "PostgreSQL Query Optimizer Agent"
description: "Optimizes PostgreSQL queries using EXPLAIN ANALYZE output parsing with pg_stat_statements extension data. Suggests index creation via HypoPG hypothetical index simulator and validates query plans against pg_hint_plan directives."
category: "Developer Tools"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/postgresql-query-optimizer-explain-api/"
tool_ecosystem:
  tool: postgresql
  npm_weekly_downloads: 21413502
---

# PostgreSQL Query Optimizer Agent

Optimizes PostgreSQL queries using EXPLAIN ANALYZE output parsing with pg_stat_statements extension data. Suggests index creation via HypoPG hypothetical index simulator and validates query plans against pg_hint_plan directives.

## Overview

Optimizes PostgreSQL queries using EXPLAIN ANALYZE output parsing with pg_stat_statements extension data. Suggests index creation via HypoPG hypothetical index simulator and validates query plans against pg_hint_plan directives.

This skill provides a comprehensive automation layer for developers and teams who need reliable, repeatable workflows. It handles authentication, rate limiting, and error recovery automatically, so you can focus on the logic that matters. The agent monitors for changes in real time and applies incremental updates to minimize API calls and reduce latency. Configuration is handled through a simple YAML manifest that defines inputs, outputs, and trigger conditions. Built-in logging captures every action for audit trails and debugging. Supports both interactive and headless modes, making it suitable for CI/CD pipelines as well as local development. The skill includes pre-built templates for common use cases and can be extended with custom plugins. Error handling follows exponential backoff with jitter for transient failures and provides clear diagnostic messages for permanent errors. Compatible with major operating systems and containerized environments. Tested against production workloads with comprehensive integration test suites.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-optimizer-explain-api
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-optimizer-explain-api -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-optimizer-explain-api -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgresql-query-optimizer-explain-api -a codex
```

### OpenClaw

```bash
clawhub install postgresql-query-optimizer-explain-api
```

## Source

- Marketplace: https://agentskillexchange.com/skills/postgresql-query-optimizer-explain-api/
