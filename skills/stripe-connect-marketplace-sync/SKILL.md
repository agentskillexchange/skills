---
title: "Stripe Connect Marketplace Sync"
description: "Synchronize marketplace transactions using the Stripe Connect API with automatic payout splitting, transfer reversals, and account onboarding via Stripe.js and the stripe-node SDK."
verification: security_reviewed
source: "https://github.com/stripe/stripe-node"
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

Manage multi-party payment flows for marketplace platforms using the Stripe Connect API. This skill handles connected account onboarding, payment intent creation with automatic fee splitting, and payout reconciliation.

The onboarding flow uses Stripe Account Links (POST /v1/account_links) to guide sellers through identity verification and bank account setup. Payment processing creates PaymentIntents with transfer_data to automatically split funds between the platform and connected accounts.

Key operations include creating direct charges on connected accounts, destination charges with application fees, and separate charges with manual transfers. The skill monitors webhook events (payment_intent.succeeded, transfer.created, payout.paid) to maintain transaction state.

Refund handling supports full and partial refunds with automatic transfer reversal via the Refunds API. Payout scheduling can be configured per connected account with daily, weekly, or monthly intervals. The stripe-node SDK (v14+) is used for all API calls with idempotency keys to prevent duplicate operations.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-marketplace-sync/)
