---
title: "Stripe Connect Account Provisioner"
description: "Automates Stripe Connect onboarding by provisioning connected accounts via the Stripe API. Handles account creation, KYC link generation with stripe.accountLinks.create(), and webhook verification for account.updated events."
verification: "security_reviewed"
source: "https://github.com/stripe/stripe-node"
category:
  - "Integrations & Connectors"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe Connect Account Provisioner

The Stripe Connect Account Provisioner streamlines marketplace and platform onboarding by automating the entire Stripe Connect account lifecycle. It uses the Stripe Node.js SDK to create Standard, Express, or Custom connected accounts programmatically. Key capabilities include generating onboarding links via stripe.accountLinks.create(), monitoring account status through account.updated webhooks, and handling retry logic for failed verifications. The agent validates required fields (business_type, country, capabilities) before submission and provides detailed error mapping for common KYC rejection reasons. Built-in support for idempotency keys prevents duplicate account creation during retries. The skill also manages capability requests (card_payments, transfers) and tracks payout schedules. Integrates with Stripe Dashboard API for real-time balance monitoring of connected accounts. Supports both test and live mode with automatic environment detection.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/stripe-connect-account-provisioner/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stripe-connect-account-provisioner
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/stripe-connect-account-provisioner`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-account-provisioner/)
