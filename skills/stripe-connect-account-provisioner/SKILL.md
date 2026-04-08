---
title: Stripe Connect Account Provisioner
description: The Stripe Connect Account Provisioner streamlines marketplace and platform
  onboarding by automating the entire Stripe Connect account lifecycle. It uses the
  Stripe Node.js SDK to create Standard, Express, or Custom connected accounts programmatically.
  Key capabilities include generating onboarding links via stripe.accountLinks.create()
  , monitoring account status through account.updated webhooks, and handling retry
  logic for failed verifications. The agent validates required fields (business_type,
  country, capabilities) before submission and provides detailed error mapping for
  common KYC rejection reasons. Built-in support for idempotency keys prevents duplicate
  account creation during retries. The skill also manages capability requests (card_payments,
  transfers) and tracks payout schedules. Integrates with Stripe Dashboard API for
  real-time balance monitoring of connected accounts. Supports both test and live
  mode with automatic environment detection.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stripe-connect-account-provisioner/
category:
- Integrations &amp; Connectors
framework:
- OpenClaw
---

# Stripe Connect Account Provisioner

The Stripe Connect Account Provisioner streamlines marketplace and platform onboarding by automating the entire Stripe Connect account lifecycle. It uses the Stripe Node.js SDK to create Standard, Express, or Custom connected accounts programmatically. Key capabilities include generating onboarding links via stripe.accountLinks.create() , monitoring account status through account.updated webhooks, and handling retry logic for failed verifications. The agent validates required fields (business_type, country, capabilities) before submission and provides detailed error mapping for common KYC rejection reasons. Built-in support for idempotency keys prevents duplicate account creation during retries. The skill also manages capability requests (card_payments, transfers) and tracks payout schedules. Integrates with Stripe Dashboard API for real-time balance monitoring of connected accounts. Supports both test and live mode with automatic environment detection.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-account-provisioner/)
