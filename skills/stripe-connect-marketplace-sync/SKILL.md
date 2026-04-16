---
title: "Stripe Connect Marketplace Sync"
description: "Synchronize marketplace transactions using the Stripe Connect API with automatic payout splitting, transfer reversals, and account onboarding via Stripe.js and the stripe-node SDK."
verification: "security_reviewed"
source: "https://github.com/stripe/stripe-node"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  ase_npm_package: "stripe"
  npm_weekly_downloads: 9280426
  license: "MIT"
---

# Stripe Connect Marketplace Sync

Manage multi-party payment flows for marketplace platforms using the Stripe Connect API. This skill handles connected account onboarding, payment intent creation with automatic fee splitting, and payout reconciliation.

The onboarding flow uses Stripe Account Links (POST /v1/account_links) to guide sellers through identity verification and bank account setup. Payment processing creates PaymentIntents with transfer_data to automatically split funds between the platform and connected accounts.

Key operations include creating direct charges on connected accounts, destination charges with application fees, and separate charges with manual transfers. The skill monitors webhook events (payment_intent.succeeded, transfer.created, payout.paid) to maintain transaction state.

Refund handling supports full and partial refunds with automatic transfer reversal via the Refunds API. Payout scheduling can be configured per connected account with daily, weekly, or monthly intervals. The stripe-node SDK (v14+) is used for all API calls with idempotency keys to prevent duplicate operations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-marketplace-sync/)
