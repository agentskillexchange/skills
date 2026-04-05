---
name: "Stripe Revenue Analytics Dashboard Builder"
description: "Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function."
category: "Data Extraction &amp; Transformation"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/stripe-revenue-analytics-dashboard/"
---
# Stripe Revenue Analytics Dashboard Builder

Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function.

Stripe Revenue Analytics Dashboard Builder is built around Stripe payments platform. The underlying ecosystem is represented by stripe/stripe-node (4,377+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like charges, payment intents, subscriptions, billing, payouts, webhooks, reports and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to stripe so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function. The implementation typically relies on charges, payment intents, subscriptions, billing, payouts, webhooks, reports, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses charges, payment intents, subscriptions, billing, payouts, webhooks, reports instead of scraping a UI, which makes runs easier to audit and retry. Supports structured inputs and outputs so another tool, agent, or CI step can consume the result. Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format. Fits into broader integration points such as billing automation, reconciliation, subscriptions, and financial analytics.

For generator-style use cases, the skill turns a vague request into repeatable scaffolding with defaults that match the upstream toolchain rather than inventing ad hoc files. Key integration points include billing automation, reconciliation, subscriptions, and financial analytics. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-analytics-dashboard
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-analytics-dashboard -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-analytics-dashboard -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-analytics-dashboard -a codex
```

### OpenClaw

```bash
clawhub install stripe-revenue-analytics-dashboard
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-revenue-analytics-dashboard/)
