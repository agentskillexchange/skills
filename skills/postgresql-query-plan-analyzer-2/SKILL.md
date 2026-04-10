---
name: "PostgreSQL Query Plan Analyzer"
description: "Executes EXPLAIN ANALYZE BUFFERS on slow PostgreSQL queries and parses the plan tree for sequential scans, nested loop joins, and sort spills. Integrates with pg_stat_statements for identifying top resource-consuming queries."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/postgresql-query-plan-analyzer-2/"
category:
  - "Developer Tools"
framework:
  - "MCP"
---

# PostgreSQL Query Plan Analyzer

PostgreSQL Query Plan Analyzer is built around PostgreSQL relational database. It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like SQL, pg_stat_statements, EXPLAIN ANALYZE, locks, indexes, extensions and preserving the operational context that matters for real tasks.
The skill is especially useful when an agent needs to translate a natural-language request into concrete postgresql-level queries, run them safely, and then explain the result in operational terms rather than returning raw output. The original use case is clear: Executes EXPLAIN ANALYZE BUFFERS on slow PostgreSQL queries and parses the plan tree for sequential scans, nested loop joins, and sort spills. Integrates with pg_stat_statements for identifying top resource-consuming queries. The implementation typically relies on SQL, pg_stat_statements, EXPLAIN ANALYZE, locks, indexes, extensions, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses SQL, pg_stat_statements, EXPLAIN ANALYZE, locks, indexes, extensions instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as query analysis, diagnostics, warehouses, and application backends.

As a runbook-style skill, the value is not just tool access but operational sequencing: check the right signals first, reduce alert noise, and produce a summary that another engineer can act on immediately. Key integration points include query analysis, diagnostics, warehouses, and application backends. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-plan-analyzer-2/)
