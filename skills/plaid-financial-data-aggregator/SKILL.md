---
name: Plaid Financial Data Aggregator & Budget Classifier
description: Integrates with the Plaid Transactions API using the plaid Python SDK to pull 90 days of transaction history across linked bank accounts. Transactions are classified into budget categories using a fine-tuned classifier via the OpenAI Chat Completions API and stored in PostgreSQL using SQLAlchemy.
category: Library &amp; API Reference
framework: Any Agent
verification: security_reviewed
rating: 4.2
reviews: 39
source: https://agentskillexchange.com/skill/plaid-financial-data-aggregator/
---

# Plaid Financial Data Aggregator & Budget Classifier

Integrates with the Plaid Transactions API using the plaid Python SDK to pull 90 days of transaction history across linked bank accounts. Transactions are classified into budget categories using a fine-tuned classifier via the OpenAI Chat Completions API and stored in PostgreSQL using SQLAlchemy.

## Overview

Integrates with the Plaid Transactions API using the plaid Python SDK to pull 90 days of transaction history across linked bank accounts. Transactions are classified into budget categories using a fine-tuned classifier via the OpenAI Chat Completions API and stored in PostgreSQL using SQLAlchemy.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill plaid-financial-data-aggregator
```

### OpenClaw

```bash
clawhub install plaid-financial-data-aggregator
```

### Claude Code

```bash
claude mcp add plaid-financial-data-aggregator
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/plaid-financial-data-aggregator/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Library &amp; API Reference
- **Framework**: Any Agent
- **Rating**: 4.2/5 (39 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/plaid-financial-data-aggregator/)
