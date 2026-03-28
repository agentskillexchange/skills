---
name: "Stripe Revenue Reconciliation Agent"
description: "Uses the Stripe API to pull charge, refund, dispute, and payout records within a configurable date window and reconciles them against expected revenue figures. Flags mismatches, duplicate charges, and unmatched refunds, outputting a CSV report with Stripe object IDs."
category: "Integrations & Connectors"
framework: "Codex"
verification: security_reviewed
source: "https://github.com/stripe/stripe-node"
tool_ecosystem:
  tool: stripe
  github_stars: 4377
  npm_weekly_downloads: 8442269
  github_repo: stripe/stripe-node
  license: MIT
  maintained: true
---

# Stripe Revenue Reconciliation Agent

Uses the Stripe API to pull charge, refund, dispute, and payout records within a configurable date window and reconciles them against expected revenue figures. Flags mismatches, duplicate charges, and unmatched refunds, outputting a CSV report with Stripe object IDs.

## Overview

**Stripe Revenue Reconciliation Agent** is built around Stripe payments platform. The underlying ecosystem is represented by `stripe/stripe-node` (4,377+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like charges, payment intents, subscriptions, billing, payouts, webhooks, reports and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to stripe so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Uses the Stripe API to pull charge, refund, dispute, and payout records within a configurable date window and reconciles them against expected revenue figures. Flags mismatches, duplicate charges, and unmatched refunds, outputting a CSV report with Stripe object IDs. The implementation typically relies on charges, payment intents, subscriptions, billing, payouts, webhooks, reports, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses charges, payment intents, subscriptions, billing, payouts, webhooks, reports instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as billing automation, reconciliation, subscriptions, and financial analytics.

Key integration points include billing automation, reconciliation, subscriptions, and financial analytics. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-reconciliation-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-reconciliation-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-reconciliation-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-reconciliation-agent -a codex
```

### OpenClaw

```bash
clawhub install stripe-revenue-reconciliation-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/stripe-revenue-reconciliation-agent/
