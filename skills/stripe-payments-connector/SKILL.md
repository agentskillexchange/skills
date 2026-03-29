---
name: "Stripe Payments Connector"
description: "Full Stripe API integration using the stripe-node SDK. Creates PaymentIntents via stripe.paymentIntents.create(), manages Customers and Subscriptions, handles webhook events through stripe.webhooks.constructEvent(), and supports Stripe Connect for marketplace payouts."
category: "Integrations & Connectors"
framework: "ChatGPT Agents"
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
# Stripe Payments Connector

Full Stripe API integration using the stripe-node SDK. Creates PaymentIntents via stripe.paymentIntents.create(), manages Customers and Subscriptions, handles webhook events through stripe.webhooks.constructEvent(), and supports Stripe Connect for marketplace payouts.

## Overview

The Stripe Payments Connector provides comprehensive integration with the Stripe payment platform using the official stripe-node SDK. It handles the complete payment lifecycle from customer creation to subscription management and dispute handling.

Core payment flows include creating PaymentIntents with stripe.paymentIntents.create() for one-time charges, setting up recurring billing with stripe.subscriptions.create() and price objects, and processing refunds via stripe.refunds.create(). The skill supports multiple payment methods including cards, ACH direct debit, SEPA, and Apple/Google Pay through the Payment Element.

Webhook processing is handled securely using stripe.webhooks.constructEvent() with signature verification. The agent listens for critical events including payment_intent.succeeded, invoice.payment_failed, customer.subscription.updated, and charge.dispute.created, routing each to appropriate handler functions.

For marketplace scenarios, the skill supports Stripe Connect with Standard, Express, and Custom account types. It manages account onboarding via Account Links, creates transfers with stripe.transfers.create(), and handles destination charges for platform fee collection. Additional features include metered billing via usage records, coupon/promotion code management, and tax calculation with Stripe Tax.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stripe-payments-connector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stripe-payments-connector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stripe-payments-connector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stripe-payments-connector -a codex
```

### OpenClaw

```bash
clawhub install stripe-payments-connector
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-payments-connector/)
