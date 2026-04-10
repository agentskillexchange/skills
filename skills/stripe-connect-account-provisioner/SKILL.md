---
title: "Stripe Connect Account Provisioner"
description: "Automates Stripe Connect onboarding by provisioning connected accounts via the Stripe API. Handles account creation, KYC link generation with stripe.accountLinks.create(), and webhook verification for account.updated events."
slug: "stripe-connect-account-provisioner"
category:
  - "Integrations &amp; Connectors"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stripe-connect-account-provisioner/"
---

# Stripe Connect Account Provisioner

Automates Stripe Connect onboarding by provisioning connected accounts via the Stripe API. Handles account creation, KYC link generation with stripe.accountLinks.create(), and webhook verification for account.updated events.

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
clawhub install stripe-connect-account-provisioner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Stripe Connect Account Provisioner streamlines marketplace and platform onboarding by automating the entire Stripe Connect account lifecycle. It uses the Stripe Node.js SDK to create Standard, Express, or Custom connected accounts programmatically.
Key capabilities include generating onboarding links via stripe.accountLinks.create(), monitoring account status through account.updated webhooks, and handling retry logic for failed verifications. The agent validates required fields (business_type, country, capabilities) before submission and provides detailed error mapping for common KYC rejection reasons.
Built-in support for idempotency keys prevents duplicate account creation during retries. The skill also manages capability requests (card_payments, transfers) and tracks payout schedules. Integrates with Stripe Dashboard API for real-time balance monitoring of connected accounts. Supports both test and live mode with automatic environment detection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-account-provisioner/)
