---
title: "Stripe Payment Flow Connector"
description: "Integrates Stripe payment processing using stripe-node SDK including PaymentIntents, Checkout Sessions, Billing Portal, and webhook event verification with stripe.webhooks.constructEvent."
verification: "security_reviewed"
source: "https://github.com/stripe/stripe-node"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  ase_npm_package: "stripe"
  npm_weekly_downloads: 9280426
  license: "MIT"
---

# Stripe Payment Flow Connector

The Stripe Payment Flow Connector provides comprehensive payment integration through the stripe-node SDK. It creates PaymentIntent objects for custom payment flows, generates Checkout Session URLs for hosted payment pages, and manages Customer objects with saved payment methods via the SetupIntents API. The skill handles Stripe webhook events using stripe.webhooks.constructEvent for signature verification, processes event types including payment_intent.succeeded, charge.refunded, and invoice.payment_failed with proper idempotency. It manages subscription lifecycles through the Billing API including plan changes, proration calculations, and trial period management. The connector configures the Customer Portal for self-service billing management, implements usage-based billing with stripe.subscriptionItems.createUsageRecord, and handles multi-currency pricing with automatic FX conversion. It manages Stripe Connect for marketplace payment splitting using stripe.transfers, implements Strong Customer Authentication (SCA) flows for European payments, and handles 3D Secure card authentication. Advanced features include dispute management via the Disputes API, revenue recognition with Stripe Revenue Recognition, and comprehensive reconciliation reporting through the Balance Transactions API.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-payment-flow-connector/)
