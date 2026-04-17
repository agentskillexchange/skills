---
title: "Stripe Payments Connector"
description: "The Stripe Payments Connector provides comprehensive integration with the Stripe payment platform using the official stripe-node SDK. It handles the complete payment lifecycle from customer creation to subscription management and dispute handling.\nCore payment flows include creating PaymentIntents with stripe.paymentIntents.create() for one-time charges, setting up recurring billing with stripe.subscriptions.create() and price objects, and processing refunds via stripe.refunds.create(). The skill supports multiple payment methods including cards, ACH direct debit, SEPA, and Apple/Google Pay through the Payment Element.\nWebhook processing is handled securely using stripe.webhooks.constructEvent() with signature verification. The agent listens for critical events including payment_intent.succeeded, invoice.payment_failed, customer.subscription.updated, and charge.dispute.created, routing each to appropriate handler functions.\nFor marketplace scenarios, the skill supports Stripe Connect with Standard, Express, and Custom account types. It manages account onboarding via Account Links, creates transfers with stripe.transfers.create(), and handles destination charges for platform fee collection. Additional features include metered billing via usage records, coupon/promotion code management, and tax calculation with Stripe Tax."
verification: security_reviewed
source: "https://github.com/stripe/stripe-node"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  ase_npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe Payments Connector

The Stripe Payments Connector provides comprehensive integration with the Stripe payment platform using the official stripe-node SDK. It handles the complete payment lifecycle from customer creation to subscription management and dispute handling.
Core payment flows include creating PaymentIntents with stripe.paymentIntents.create() for one-time charges, setting up recurring billing with stripe.subscriptions.create() and price objects, and processing refunds via stripe.refunds.create(). The skill supports multiple payment methods including cards, ACH direct debit, SEPA, and Apple/Google Pay through the Payment Element.
Webhook processing is handled securely using stripe.webhooks.constructEvent() with signature verification. The agent listens for critical events including payment_intent.succeeded, invoice.payment_failed, customer.subscription.updated, and charge.dispute.created, routing each to appropriate handler functions.
For marketplace scenarios, the skill supports Stripe Connect with Standard, Express, and Custom account types. It manages account onboarding via Account Links, creates transfers with stripe.transfers.create(), and handles destination charges for platform fee collection. Additional features include metered billing via usage records, coupon/promotion code management, and tax calculation with Stripe Tax.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stripe-payments-connector
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/stripe-payments-connector` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-payments-connector/)
