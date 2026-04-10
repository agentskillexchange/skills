---
title: "Stripe Payment Flow Connector"
description: "Integrates Stripe payment processing using stripe-node SDK including PaymentIntents, Checkout Sessions, Billing Portal, and webhook event verification with stripe.webhooks.constructEvent."
slug: "stripe-payment-flow-connector"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stripe-payment-flow-connector/"
---

# Stripe Payment Flow Connector

Integrates Stripe payment processing using stripe-node SDK including PaymentIntents, Checkout Sessions, Billing Portal, and webhook event verification with stripe.webhooks.constructEvent.

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
clawhub install stripe-payment-flow-connector
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Stripe Payment Flow Connector provides comprehensive payment integration through the stripe-node SDK. It creates PaymentIntent objects for custom payment flows, generates Checkout Session URLs for hosted payment pages, and manages Customer objects with saved payment methods via the SetupIntents API. The skill handles Stripe webhook events using stripe.webhooks.constructEvent for signature verification, processes event types including payment_intent.succeeded, charge.refunded, and invoice.payment_failed with proper idempotency. It manages subscription lifecycles through the Billing API including plan changes, proration calculations, and trial period management. The connector configures the Customer Portal for self-service billing management, implements usage-based billing with stripe.subscriptionItems.createUsageRecord, and handles multi-currency pricing with automatic FX conversion. It manages Stripe Connect for marketplace payment splitting using stripe.transfers, implements Strong Customer Authentication (SCA) flows for European payments, and handles 3D Secure card authentication. Advanced features include dispute management via the Disputes API, revenue recognition with Stripe Revenue Recognition, and comprehensive reconciliation reporting through the Balance Transactions API.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-payment-flow-connector/)
