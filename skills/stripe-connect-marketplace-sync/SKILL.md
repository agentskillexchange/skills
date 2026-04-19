---
title: "Stripe Connect Marketplace Sync"
description: "Manage multi-party payment flows for marketplace platforms using the Stripe Connect API. This skill handles connected account onboarding, payment intent creation with automatic fee splitting, and payout reconciliation. The onboarding flow uses Stripe Account Links (POST /v1/account_links) to guide sellers through identity verification and bank account setup. Payment processing creates PaymentIntents with transfer_data to automatically split funds between the platform and connected accounts. Key operations include creating direct charges on connected accounts, destination charges with application fees, and separate charges with manual transfers. The skill monitors webhook events (payment_intent.succeeded, transfer.created, payout.paid) to maintain transaction state. Refund handling supports full and partial refunds with automatic transfer reversal via the Refunds API. Payout scheduling can be configured per connected account with daily, weekly, or monthly intervals. The stripe-node SDK (v14+) is used for all API calls with idempotency keys to prevent duplicate operations."
source: "https://github.com/stripe/stripe-node"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe Connect Marketplace Sync

Manage multi-party payment flows for marketplace platforms using the Stripe Connect API. This skill handles connected account onboarding, payment intent creation with automatic fee splitting, and payout reconciliation. The onboarding flow uses Stripe Account Links (POST /v1/account_links) to guide sellers through identity verification and bank account setup. Payment processing creates PaymentIntents with transfer_data to automatically split funds between the platform and connected accounts. Key operations include creating direct charges on connected accounts, destination charges with application fees, and separate charges with manual transfers. The skill monitors webhook events (payment_intent.succeeded, transfer.created, payout.paid) to maintain transaction state. Refund handling supports full and partial refunds with automatic transfer reversal via the Refunds API. Payout scheduling can be configured per connected account with daily, weekly, or monthly intervals. The stripe-node SDK (v14+) is used for all API calls with idempotency keys to prevent duplicate operations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-marketplace-sync/)
