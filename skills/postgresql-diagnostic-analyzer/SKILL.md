---
name: "PostgreSQL Diagnostic Analyzer"
description: "Runs diagnostic queries against PostgreSQL using pg_stat_statements, pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention, and bloat using pgstattuple and pg_repack extension analysis."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/postgresql-diagnostic-analyzer/"
---
# PostgreSQL Diagnostic Analyzer

Runs diagnostic queries against PostgreSQL using pg_stat_statements, pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention, and bloat using pgstattuple and pg_repack extension analysis.

## Overview

PostgreSQL Diagnostic Analyzer is built around PostgreSQL relational database. It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like SQL, pg_stat_statements, EXPLAIN ANALYZE, locks, indexes, extensions and preserving the operational context that matters for real tasks.

The skill is especially useful when an agent needs to translate a natural-language request into concrete postgresql-level queries, run them safely, and then explain the result in operational terms rather than returning raw output. The original use case is clear: Runs diagnostic queries against PostgreSQL using pg_stat_statements, pg_stat_activity, and pg_locks system views. Identifies slow queries, lock contention, and bloat using pgstattuple and pg_repack extension analysis. The implementation typically relies on SQL, pg_stat_statements, EXPLAIN ANALYZE, locks, indexes, extensions, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

- Accesses SQL, pg_stat_statements, EXPLAIN ANALYZE, locks, indexes, extensions instead of scraping a UI, which makes runs easier to audit and retry.

- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

- Fits into broader integration points such as query analysis, diagnostics, warehouses, and application backends.

As a runbook-style skill, the value is not just tool access but operational sequencing: check the right signals first, reduce alert noise, and produce a summary that another engineer can act on immediately. Key integration points include query analysis, diagnostics, warehouses, and application backends. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-diagnostic-analyzer/)
