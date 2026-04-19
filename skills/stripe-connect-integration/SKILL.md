---
title: "Stripe Connect Integration"
description: "The Stripe Connect Integration skill provides comprehensive payment platform capabilities using the Stripe Connect API via the official Stripe Node.js SDK (stripe@14.x). It supports both Standard and Express connected account types for marketplace and platform payment scenarios. Account onboarding is handled through the Account Links API, generating hosted onboarding URLs that guide connected accounts through identity verification and bank account setup. The skill monitors onboarding status via the Accounts API and handles account.updated webhook events. Payment processing creates PaymentIntents with automatic splitting between platform and connected accounts using application_fee_amount or transfer_data parameters. The skill supports destination charges, separate charges and transfers, and direct charges on connected accounts. Payout scheduling is configurable per connected account. Refund handling processes both platform and connected account refunds with proper fee reversal. Webhook signature verification uses the stripe.webhooks.constructEvent method with endpoint secrets for secure event processing."
source: "https://github.com/stripe/stripe-node"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe Connect Integration

The Stripe Connect Integration skill provides comprehensive payment platform capabilities using the Stripe Connect API via the official Stripe Node.js SDK (stripe@14.x). It supports both Standard and Express connected account types for marketplace and platform payment scenarios. Account onboarding is handled through the Account Links API, generating hosted onboarding URLs that guide connected accounts through identity verification and bank account setup. The skill monitors onboarding status via the Accounts API and handles account.updated webhook events. Payment processing creates PaymentIntents with automatic splitting between platform and connected accounts using application_fee_amount or transfer_data parameters. The skill supports destination charges, separate charges and transfers, and direct charges on connected accounts. Payout scheduling is configurable per connected account. Refund handling processes both platform and connected account refunds with proper fee reversal. Webhook signature verification uses the stripe.webhooks.constructEvent method with endpoint secrets for secure event processing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-integration/)
