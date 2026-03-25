---
name: "Stripe Connect Account Provisioner"
description: "Automates Stripe Connect onboarding by provisioning connected accounts via the Stripe API. Handles account creation, KYC link generation with stripe.accountLinks.create(), and webhook verification for account.updated events."
category: "Integrations & Connectors"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/stripe-connect-account-provisioner/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "stripe"  # from ase_tool_match
  github_stars: 4377  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8442269  # from ase_npm_downloads
  github_repo: "stripe/stripe-node"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Stripe Connect Account Provisioner

Automates Stripe Connect onboarding by provisioning connected accounts via the Stripe API. Handles account creation, KYC link generation with stripe.accountLinks.create(), and webhook verification for account.updated events.

## Overview

The Stripe Connect Account Provisioner streamlines marketplace and platform onboarding by automating the entire Stripe Connect account lifecycle. It uses the Stripe Node.js SDK to create Standard, Express, or Custom connected accounts programmatically.

Key capabilities include generating onboarding links via `stripe.accountLinks.create()`, monitoring account status through `account.updated` webhooks, and handling retry logic for failed verifications. The agent validates required fields (business_type, country, capabilities) before submission and provides detailed error mapping for common KYC rejection reasons.

Built-in support for idempotency keys prevents duplicate account creation during retries. The skill also manages capability requests (card_payments, transfers) and tracks payout schedules. Integrates with Stripe Dashboard API for real-time balance monitoring of connected accounts. Supports both test and live mode with automatic environment detection.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-account-provisioner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-account-provisioner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-account-provisioner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-account-provisioner -a codex
```

### OpenClaw

```bash
clawhub install stripe-connect-account-provisioner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/stripe-connect-account-provisioner/
