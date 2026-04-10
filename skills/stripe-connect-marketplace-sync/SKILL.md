---
title: "Stripe Connect Marketplace Sync"
description: "Synchronize marketplace transactions using the Stripe Connect API with automatic payout splitting, transfer reversals, and account onboarding via Stripe.js and the stripe-node SDK."
slug: "stripe-connect-marketplace-sync"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stripe-connect-marketplace-sync/"
listed: true
---

# Stripe Connect Marketplace Sync

Synchronize marketplace transactions using the Stripe Connect API with automatic payout splitting, transfer reversals, and account onboarding via Stripe.js and the stripe-node SDK.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install stripe-connect-marketplace-sync
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Manage multi-party payment flows for marketplace platforms using the Stripe Connect API. This skill handles connected account onboarding, payment intent creation with automatic fee splitting, and payout reconciliation.
The onboarding flow uses Stripe Account Links (POST /v1/account_links) to guide sellers through identity verification and bank account setup. Payment processing creates PaymentIntents with transfer_data to automatically split funds between the platform and connected accounts.
Key operations include creating direct charges on connected accounts, destination charges with application fees, and separate charges with manual transfers. The skill monitors webhook events (payment_intent.succeeded, transfer.created, payout.paid) to maintain transaction state.
Refund handling supports full and partial refunds with automatic transfer reversal via the Refunds API. Payout scheduling can be configured per connected account with daily, weekly, or monthly intervals. The stripe-node SDK (v14+) is used for all API calls with idempotency keys to prevent duplicate operations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-marketplace-sync/)
