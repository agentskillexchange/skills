---
title: "Stripe Payments Connector"
description: "Full Stripe API integration using the stripe-node SDK. Creates PaymentIntents via stripe.paymentIntents.create(), manages Customers and Subscriptions, handles webhook events through stripe.webhooks.constructEvent(), and supports Stripe Connect for marketplace payouts."
slug: "stripe-payments-connector"
category:
  - "Integrations &amp; Connectors"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stripe-payments-connector/"
---

# Stripe Payments Connector

Full Stripe API integration using the stripe-node SDK. Creates PaymentIntents via stripe.paymentIntents.create(), manages Customers and Subscriptions, handles webhook events through stripe.webhooks.constructEvent(), and supports Stripe Connect for marketplace payouts.

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
clawhub install stripe-payments-connector
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Stripe Payments Connector provides comprehensive integration with the Stripe payment platform using the official stripe-node SDK. It handles the complete payment lifecycle from customer creation to subscription management and dispute handling.
Core payment flows include creating PaymentIntents with stripe.paymentIntents.create() for one-time charges, setting up recurring billing with stripe.subscriptions.create() and price objects, and processing refunds via stripe.refunds.create(). The skill supports multiple payment methods including cards, ACH direct debit, SEPA, and Apple/Google Pay through the Payment Element.
Webhook processing is handled securely using stripe.webhooks.constructEvent() with signature verification. The agent listens for critical events including payment_intent.succeeded, invoice.payment_failed, customer.subscription.updated, and charge.dispute.created, routing each to appropriate handler functions.
For marketplace scenarios, the skill supports Stripe Connect with Standard, Express, and Custom account types. It manages account onboarding via Account Links, creates transfers with stripe.transfers.create(), and handles destination charges for platform fee collection. Additional features include metered billing via usage records, coupon/promotion code management, and tax calculation with Stripe Tax.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-payments-connector/)
