---
title: Stripe Connect Integration
description: The Stripe Connect Integration skill provides comprehensive payment platform
  capabilities using the Stripe Connect API via the official Stripe Node.js SDK (stripe@14.x).
  It supports both Standard and Express connected account types for marketplace and
  platform payment scenarios. Account onboarding is handled through the Account Links
  API, generating hosted onboarding URLs that guide connected accounts through identity
  verification and bank account setup. The skill monitors onboarding status via the
  Accounts API and handles account.updated webhook events. Payment processing creates
  PaymentIntents with automatic splitting between platform and connected accounts
  using application_fee_amount or transfer_data parameters. The skill supports destination
  charges, separate charges and transfers, and direct charges on connected accounts.
  Payout scheduling is configurable per connected account. Refund handling processes
  both platform and connected account refunds with proper fee reversal. Webhook signature
  verification uses the stripe.webhooks.constructEvent method with endpoint secrets
  for secure event processing.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stripe-connect-integration/
category:
- Integrations &amp; Connectors
framework:
- ChatGPT Agents
---

# Stripe Connect Integration

The Stripe Connect Integration skill provides comprehensive payment platform capabilities using the Stripe Connect API via the official Stripe Node.js SDK (stripe@14.x). It supports both Standard and Express connected account types for marketplace and platform payment scenarios. Account onboarding is handled through the Account Links API, generating hosted onboarding URLs that guide connected accounts through identity verification and bank account setup. The skill monitors onboarding status via the Accounts API and handles account.updated webhook events. Payment processing creates PaymentIntents with automatic splitting between platform and connected accounts using application_fee_amount or transfer_data parameters. The skill supports destination charges, separate charges and transfers, and direct charges on connected accounts. Payout scheduling is configurable per connected account. Refund handling processes both platform and connected account refunds with proper fee reversal. Webhook signature verification uses the stripe.webhooks.constructEvent method with endpoint secrets for secure event processing.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-integration/)
