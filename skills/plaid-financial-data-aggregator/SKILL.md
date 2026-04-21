---
title: "Plaid Financial Data Aggregator &amp; Budget Classifier"
slug: "plaid-financial-data-aggregator"
description: "Integrates with the Plaid Transactions API using the plaid Python SDK to pull 90 days of transaction history across linked bank accounts. Transactions are classified into budget categories using a fine-tuned classifier via the OpenAI Chat Completions API and stored in PostgreSQL using SQLAlchemy."
verification: security_reviewed
source: "https://plaid.com/docs/"
framework:
  - "Cursor"
---

# Plaid Financial Data Aggregator &amp; Budget Classifier

Integrates with the Plaid Transactions API using the plaid Python SDK to pull 90 days of transaction history across linked bank accounts. Transactions are classified into budget categories using a fine-tuned classifier via the OpenAI Chat Completions API and stored in PostgreSQL using SQLAlchemy.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plaid-financial-data-aggregator/)
