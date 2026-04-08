---
title: Stripe Revenue Reconciliation Agent
description: 'Stripe Revenue Reconciliation Agent is built around Stripe payments
  platform. The underlying ecosystem is represented by stripe/stripe-node (4,377+
  GitHub stars). It gives an agent a more technical and reliable way to work with
  the tool than a thin one-line wrapper, using stable interfaces like charges, payment
  intents, subscriptions, billing, payouts, webhooks, reports and preserving the operational
  context that matters for real tasks. In practice, the skill gives an agent a stable
  interface to stripe so it can inspect state, run the right operation, and produce
  a result that fits into a larger engineering or operations pipeline. The original
  use case is clear: Uses the Stripe API to pull charge, refund, dispute, and payout
  records within a configurable date window and reconciles them against expected revenue
  figures. Flags mismatches, duplicate charges, and unmatched refunds, outputting
  a CSV report with Stripe object IDs. The implementation typically relies on charges,
  payment intents, subscriptions, billing, payouts, webhooks, reports, with configuration
  passed through environment variables, connection strings, service tokens, or workspace
  config depending on the upstream platform. Accesses charges, payment intents, subscriptions,
  billing, payouts, webhooks, reports instead of scraping a UI, which makes runs easier
  to audit and retry. Supports structured inputs and outputs so another tool, agent,
  or CI step can consume the result. Can be wired into cron jobs, webhook handlers,
  MCP transports, or local CLI workflows depending on the skill format. Fits into
  broader integration points such as billing automation, reconciliation, subscriptions,
  and financial analytics. Key integration points include billing automation, reconciliation,
  subscriptions, and financial analytics. In a real environment that usually means
  passing credentials through env vars or app config, respecting rate limits and permission
  scopes, and returning structured artifacts that can be attached to tickets, pull
  requests, dashboards, or follow-up automations.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/stripe-revenue-reconciliation-agent/
category:
- Integrations &amp; Connectors
framework:
- Codex
---

# Stripe Revenue Reconciliation Agent

Stripe Revenue Reconciliation Agent is built around Stripe payments platform. The underlying ecosystem is represented by stripe/stripe-node (4,377+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like charges, payment intents, subscriptions, billing, payouts, webhooks, reports and preserving the operational context that matters for real tasks. In practice, the skill gives an agent a stable interface to stripe so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Uses the Stripe API to pull charge, refund, dispute, and payout records within a configurable date window and reconciles them against expected revenue figures. Flags mismatches, duplicate charges, and unmatched refunds, outputting a CSV report with Stripe object IDs. The implementation typically relies on charges, payment intents, subscriptions, billing, payouts, webhooks, reports, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform. Accesses charges, payment intents, subscriptions, billing, payouts, webhooks, reports instead of scraping a UI, which makes runs easier to audit and retry. Supports structured inputs and outputs so another tool, agent, or CI step can consume the result. Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format. Fits into broader integration points such as billing automation, reconciliation, subscriptions, and financial analytics. Key integration points include billing automation, reconciliation, subscriptions, and financial analytics. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-revenue-reconciliation-agent/)
