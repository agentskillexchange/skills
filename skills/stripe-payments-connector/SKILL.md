---
title: Stripe Payments Connector
description: The Stripe Payments Connector provides comprehensive integration with
  the Stripe payment platform using the official stripe-node SDK. It handles the complete
  payment lifecycle from customer creation to subscription management and dispute
  handling. Core payment flows include creating PaymentIntents with stripe.paymentIntents.create()
  for one-time charges, setting up recurring billing with stripe.subscriptions.create()
  and price objects, and processing refunds via stripe.refunds.create(). The skill
  supports multiple payment methods including cards, ACH direct debit, SEPA, and Apple/Google
  Pay through the Payment Element. Webhook processing is handled securely using stripe.webhooks.constructEvent()
  with signature verification. The agent listens for critical events including payment_intent.succeeded,
  invoice.payment_failed, customer.subscription.updated, and charge.dispute.created,
  routing each to appropriate handler functions. For marketplace scenarios, the skill
  supports Stripe Connect with Standard, Express, and Custom account types. It manages
  account onboarding via Account Links, creates transfers with stripe.transfers.create(),
  and handles destination charges for platform fee collection. Additional features
  include metered billing via usage records, coupon/promotion code management, and
  tax calculation with Stripe Tax.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stripe-payments-connector/
category:
- Integrations &amp; Connectors
framework:
- ChatGPT Agents
---

# Stripe Payments Connector

The Stripe Payments Connector provides comprehensive integration with the Stripe payment platform using the official stripe-node SDK. It handles the complete payment lifecycle from customer creation to subscription management and dispute handling. Core payment flows include creating PaymentIntents with stripe.paymentIntents.create() for one-time charges, setting up recurring billing with stripe.subscriptions.create() and price objects, and processing refunds via stripe.refunds.create(). The skill supports multiple payment methods including cards, ACH direct debit, SEPA, and Apple/Google Pay through the Payment Element. Webhook processing is handled securely using stripe.webhooks.constructEvent() with signature verification. The agent listens for critical events including payment_intent.succeeded, invoice.payment_failed, customer.subscription.updated, and charge.dispute.created, routing each to appropriate handler functions. For marketplace scenarios, the skill supports Stripe Connect with Standard, Express, and Custom account types. It manages account onboarding via Account Links, creates transfers with stripe.transfers.create(), and handles destination charges for platform fee collection. Additional features include metered billing via usage records, coupon/promotion code management, and tax calculation with Stripe Tax.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-payments-connector/)
