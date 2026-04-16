---
title: "Stripe Payments Connector"
description: "Full Stripe API integration using the stripe-node SDK. Creates PaymentIntents via stripe.paymentIntents.create(), manages Customers and Subscriptions, handles webhook events through stripe.webhooks.constructEvent(), and supports Stripe Connect for marketplace payouts."
verification: "security_reviewed"
source: "https://github.com/stripe/stripe-node"
category:
  - "Integrations &amp; Connectors"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  ase_npm_package: "stripe"
  npm_weekly_downloads: 9280426
  license: "MIT"
---

# Stripe Payments Connector

The Stripe Payments Connector provides comprehensive integration with the Stripe payment platform using the official stripe-node SDK. It handles the complete payment lifecycle from customer creation to subscription management and dispute handling.

Core payment flows include creating PaymentIntents with stripe.paymentIntents.create() for one-time charges, setting up recurring billing with stripe.subscriptions.create() and price objects, and processing refunds via stripe.refunds.create(). The skill supports multiple payment methods including cards, ACH direct debit, SEPA, and Apple/Google Pay through the Payment Element.

Webhook processing is handled securely using stripe.webhooks.constructEvent() with signature verification. The agent listens for critical events including payment_intent.succeeded, invoice.payment_failed, customer.subscription.updated, and charge.dispute.created, routing each to appropriate handler functions.

For marketplace scenarios, the skill supports Stripe Connect with Standard, Express, and Custom account types. It manages account onboarding via Account Links, creates transfers with stripe.transfers.create(), and handles destination charges for platform fee collection. Additional features include metered billing via usage records, coupon/promotion code management, and tax calculation with Stripe Tax.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-payments-connector/)
