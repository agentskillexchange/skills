---
title: Stripe Connect Marketplace Sync
description: Manage multi-party payment flows for marketplace platforms using the
  Stripe Connect API. This skill handles connected account onboarding, payment intent
  creation with automatic fee splitting, and payout reconciliation. The onboarding
  flow uses Stripe Account Links (POST /v1/account_links) to guide sellers through
  identity verification and bank account setup. Payment processing creates PaymentIntents
  with transfer_data to automatically split funds between the platform and connected
  accounts. Key operations include creating direct charges on connected accounts,
  destination charges with application fees, and separate charges with manual transfers.
  The skill monitors webhook events (payment_intent.succeeded, transfer.created, payout.paid)
  to maintain transaction state. Refund handling supports full and partial refunds
  with automatic transfer reversal via the Refunds API. Payout scheduling can be configured
  per connected account with daily, weekly, or monthly intervals. The stripe-node
  SDK (v14+) is used for all API calls with idempotency keys to prevent duplicate
  operations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stripe-connect-marketplace-sync/
category:
- Integrations &amp; Connectors
framework:
- Gemini
---

# Stripe Connect Marketplace Sync

Manage multi-party payment flows for marketplace platforms using the Stripe Connect API. This skill handles connected account onboarding, payment intent creation with automatic fee splitting, and payout reconciliation. The onboarding flow uses Stripe Account Links (POST /v1/account_links) to guide sellers through identity verification and bank account setup. Payment processing creates PaymentIntents with transfer_data to automatically split funds between the platform and connected accounts. Key operations include creating direct charges on connected accounts, destination charges with application fees, and separate charges with manual transfers. The skill monitors webhook events (payment_intent.succeeded, transfer.created, payout.paid) to maintain transaction state. Refund handling supports full and partial refunds with automatic transfer reversal via the Refunds API. Payout scheduling can be configured per connected account with daily, weekly, or monthly intervals. The stripe-node SDK (v14+) is used for all API calls with idempotency keys to prevent duplicate operations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-marketplace-sync/)
