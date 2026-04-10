---
title: "Stripe Revenue Analytics Dashboard Builder"
description: "Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function."
slug: "stripe-revenue-analytics-dashboard"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stripe-revenue-analytics-dashboard/"
---

# Stripe Revenue Analytics Dashboard Builder

Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install stripe-revenue-analytics-dashboard
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Stripe Revenue Analytics Dashboard Builder is built around Stripe payments platform. The underlying ecosystem is represented by stripe/stripe-node (4,377+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like charges, payment intents, subscriptions, billing, payouts, webhooks, reports and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to stripe so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function. The implementation typically relies on charges, payment intents, subscriptions, billing, payouts, webhooks, reports, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.
- Accesses charges, payment intents, subscriptions, billing, payouts, webhooks, reports instead of scraping a UI, which makes runs easier to audit and retry.
- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
- Fits into broader integration points such as billing automation, reconciliation, subscriptions, and financial analytics.
For generator-style use cases, the skill turns a vague request into repeatable scaffolding with defaults that match the upstream toolchain rather than inventing ad hoc files. Key integration points include billing automation, reconciliation, subscriptions, and financial analytics. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-revenue-analytics-dashboard/)
