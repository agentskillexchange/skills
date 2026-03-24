---
name: "Plaid Financial Data Aggregator & Budget Classifier"
description: "Integrates with the Plaid Transactions API using the plaid Python SDK to pull 90 days of transaction history across linked bank accounts. Transactions are classified into budget categories using a fine-tuned classifier via the OpenAI Chat Completions API and stored in PostgreSQL using SQLAlchemy."
category: "Library & API Reference"
framework: "Cursor"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/plaid-financial-data-aggregator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "postgresql"  # from ase_tool_match
  npm_weekly_downloads: 21413502  # from ase_npm_downloads
---

# Plaid Financial Data Aggregator & Budget Classifier

Integrates with the Plaid Transactions API using the plaid Python SDK to pull 90 days of transaction history across linked bank accounts. Transactions are classified into budget categories using a fine-tuned classifier via the OpenAI Chat Completions API and stored in PostgreSQL using SQLAlchemy.

## Overview

Integrates with the Plaid Transactions API using the plaid Python SDK to pull 90 days of transaction history across linked bank accounts. Transactions are classified into budget categories using a fine-tuned classifier via the OpenAI Chat Completions API and stored in PostgreSQL using SQLAlchemy.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill plaid-financial-data-aggregator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill plaid-financial-data-aggregator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill plaid-financial-data-aggregator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill plaid-financial-data-aggregator -a codex
```

### OpenClaw

```bash
clawhub install plaid-financial-data-aggregator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/plaid-financial-data-aggregator/
