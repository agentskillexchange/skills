---
title: "Plaid Financial Data Aggregator &amp; Budget Classifier"
slug: "plaid-financial-data-aggregator"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
source: "https://agentskillexchange.com/skills/plaid-financial-data-aggregator/"
---

# Plaid Financial Data Aggregator &amp; Budget Classifier

Integrates with the Plaid Transactions API using the plaid Python SDK to pull 90 days of transaction history across linked bank accounts. Transactions are classified into budget categories using a fine-tuned classifier via the OpenAI Chat Completions API and stored in PostgreSQL using SQLAlchemy.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plaid-financial-data-aggregator/)
