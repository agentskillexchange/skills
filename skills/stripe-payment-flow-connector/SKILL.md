---
name: Stripe Payment Flow Connector
description: Integrates Stripe payment processing using stripe-node SDK including
  PaymentIntents, Checkout Sessions, Billing Portal, and webhook event verification
  with stripe.webhooks.constructEvent.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stripe-payment-flow-connector/
category:
- Integrations &amp; Connectors
framework:
- Cursor
---
# Stripe Payment Flow Connector

The Stripe Payment Flow Connector provides comprehensive payment integration through the stripe-node SDK. It creates PaymentIntent objects for custom payment flows, generates Checkout Session URLs for hosted payment pages, and manages Customer objects with saved payment methods via the SetupIntents API. The skill handles Stripe webhook events using stripe.webhooks.constructEvent for signature verification, processes event types including payment_intent.succeeded, charge.refunded, and invoice.payment_failed with proper idempotency. It manages subscription lifecycles through the Billing API including plan changes, proration calculations, and trial period management. The connector configures the Customer Portal for self-service billing management, implements usage-based billing with stripe.subscriptionItems.createUsageRecord, and handles multi-currency pricing with automatic FX conversion. It manages Stripe Connect for marketplace payment splitting using stripe.transfers, implements Strong Customer Authentication (SCA) flows for European payments, and handles 3D Secure card authentication. Advanced features include dispute management via the Disputes API, revenue recognition with Stripe Revenue Recognition, and comprehensive reconciliation reporting through the Balance Transactions API.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-payment-flow-connector/)
