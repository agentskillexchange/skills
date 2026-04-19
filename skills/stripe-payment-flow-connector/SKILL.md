---
title: "Stripe Payment Flow Connector"
description: "The Stripe Payment Flow Connector provides comprehensive payment integration through the stripe-node SDK. It creates PaymentIntent objects for custom payment flows, generates Checkout Session URLs for hosted payment pages, and manages Customer objects with saved payment methods via the SetupIntents API. The skill handles Stripe webhook events using stripe.webhooks.constructEvent for signature verification, processes event types including payment_intent.succeeded, charge.refunded, and invoice.payment_failed with proper idempotency. It manages subscription lifecycles through the Billing API including plan changes, proration calculations, and trial period management. The connector configures the Customer Portal for self-service billing management, implements usage-based billing with stripe.subscriptionItems.createUsageRecord, and handles multi-currency pricing with automatic FX conversion. It manages Stripe Connect for marketplace payment splitting using stripe.transfers, implements Strong Customer Authentication (SCA) flows for European payments, and handles 3D Secure card authentication. Advanced features include dispute management via the Disputes API, revenue recognition with Stripe Revenue Recognition, and comprehensive reconciliation reporting through the Balance Transactions API."
source: "https://github.com/stripe/stripe-node"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe Payment Flow Connector

The Stripe Payment Flow Connector provides comprehensive payment integration through the stripe-node SDK. It creates PaymentIntent objects for custom payment flows, generates Checkout Session URLs for hosted payment pages, and manages Customer objects with saved payment methods via the SetupIntents API. The skill handles Stripe webhook events using stripe.webhooks.constructEvent for signature verification, processes event types including payment_intent.succeeded, charge.refunded, and invoice.payment_failed with proper idempotency. It manages subscription lifecycles through the Billing API including plan changes, proration calculations, and trial period management. The connector configures the Customer Portal for self-service billing management, implements usage-based billing with stripe.subscriptionItems.createUsageRecord, and handles multi-currency pricing with automatic FX conversion. It manages Stripe Connect for marketplace payment splitting using stripe.transfers, implements Strong Customer Authentication (SCA) flows for European payments, and handles 3D Secure card authentication. Advanced features include dispute management via the Disputes API, revenue recognition with Stripe Revenue Recognition, and comprehensive reconciliation reporting through the Balance Transactions API.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-payment-flow-connector/)
