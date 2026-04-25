---
title: "Plaid Financial Data Aggregator & Budget Classifier"
description: "Integrates with the Plaid Transactions API using the plaid Python SDK to pull 90 days of transaction history across linked bank accounts. Transactions are classified into budget categories using a fine-tuned classifier via the OpenAI Chat Completions API and stored in PostgreSQL using SQLAlchemy."
verification: "security_reviewed"
source: "https://plaid.com/docs/"
category:
  - "Library & API Reference"
framework:
  - "Cursor"
---

# Plaid Financial Data Aggregator & Budget Classifier

Plaid Financial Data Aggregator & Budget Classifier is built around PostgreSQL relational database. It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like SQL, pg_stat_statements, EXPLAIN ANALYZE, locks, indexes, extensions and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to postgresql so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Integrates with the Plaid Transactions API using the plaid Python SDK to pull 90 days of transaction history across linked bank accounts. Transactions are classified into budget categories using a fine-tuned classifier via the OpenAI Chat Completions API and stored in PostgreSQL using SQLAlchemy. The implementation typically relies on SQL, pg_stat_statements, EXPLAIN ANALYZE, locks, indexes, extensions, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses SQL, pg_stat_statements, EXPLAIN ANALYZE, locks, indexes, extensions instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as query analysis, diagnostics, warehouses, and application backends.

 Key integration points include query analysis, diagnostics, warehouses, and application backends. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/plaid-financial-data-aggregator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/plaid-financial-data-aggregator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/plaid-financial-data-aggregator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plaid-financial-data-aggregator/)
