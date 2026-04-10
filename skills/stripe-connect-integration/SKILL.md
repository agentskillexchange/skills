---
title: "Stripe Connect Integration"
description: "Manages Stripe Connect accounts and payment flows using the Stripe Node.js SDK (stripe@14.x). Handles onboarding via Account Links API, creates PaymentIntents with application fees, and processes Connect webhooks."
slug: "stripe-connect-integration"
category:
  - "Integrations &amp; Connectors"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stripe-connect-integration/"
---

# Stripe Connect Integration

Manages Stripe Connect accounts and payment flows using the Stripe Node.js SDK (stripe@14.x). Handles onboarding via Account Links API, creates PaymentIntents with application fees, and processes Connect webhooks.

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
clawhub install stripe-connect-integration
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Stripe Connect Integration skill provides comprehensive payment platform capabilities using the Stripe Connect API via the official Stripe Node.js SDK (stripe@14.x). It supports both Standard and Express connected account types for marketplace and platform payment scenarios.
Account onboarding is handled through the Account Links API, generating hosted onboarding URLs that guide connected accounts through identity verification and bank account setup. The skill monitors onboarding status via the Accounts API and handles account.updated webhook events.
Payment processing creates PaymentIntents with automatic splitting between platform and connected accounts using application_fee_amount or transfer_data parameters. The skill supports destination charges, separate charges and transfers, and direct charges on connected accounts. Payout scheduling is configurable per connected account. Refund handling processes both platform and connected account refunds with proper fee reversal. Webhook signature verification uses the stripe.webhooks.constructEvent method with endpoint secrets for secure event processing.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-integration/)
