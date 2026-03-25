---
name: "Stripe Connect Marketplace Sync"
description: "Synchronize marketplace transactions using the Stripe Connect API with automatic payout splitting, transfer reversals, and account onboarding via Stripe.js and the stripe-node SDK."
category: "Integrations & Connectors"
framework: "Gemini"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/stripe-connect-marketplace-sync/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "stripe"  # from ase_tool_match
  github_stars: 4377  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8442269  # from ase_npm_downloads
  github_repo: "stripe/stripe-node"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Stripe Connect Marketplace Sync

Synchronize marketplace transactions using the Stripe Connect API with automatic payout splitting, transfer reversals, and account onboarding via Stripe.js and the stripe-node SDK.

## Overview

Manage multi-party payment flows for marketplace platforms using the Stripe Connect API. This skill handles connected account onboarding, payment intent creation with automatic fee splitting, and payout reconciliation.

The onboarding flow uses Stripe Account Links (POST /v1/account_links) to guide sellers through identity verification and bank account setup. Payment processing creates PaymentIntents with transfer_data to automatically split funds between the platform and connected accounts.

Key operations include creating direct charges on connected accounts, destination charges with application fees, and separate charges with manual transfers. The skill monitors webhook events (payment_intent.succeeded, transfer.created, payout.paid) to maintain transaction state.

Refund handling supports full and partial refunds with automatic transfer reversal via the Refunds API. Payout scheduling can be configured per connected account with daily, weekly, or monthly intervals. The stripe-node SDK (v14+) is used for all API calls with idempotency keys to prevent duplicate operations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-marketplace-sync
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-marketplace-sync -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-marketplace-sync -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-marketplace-sync -a codex
```

### OpenClaw

```bash
clawhub install stripe-connect-marketplace-sync
```

## Source

- Marketplace: https://agentskillexchange.com/skills/stripe-connect-marketplace-sync/
