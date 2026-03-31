---
name: "Stripe Connect Integration"
description: "Manages Stripe Connect accounts and payment flows using the Stripe Node.js SDK (stripe@14.x). Handles onboarding via Account Links API, creates PaymentIntents with application fees, and processes Connect webhooks."
category: "Integrations & Connectors"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/stripe-connect-integration/"
---
# Stripe Connect Integration

Manages Stripe Connect accounts and payment flows using the Stripe Node.js SDK (stripe@14.x). Handles onboarding via Account Links API, creates PaymentIntents with application fees, and processes Connect webhooks.

## Overview

The Stripe Connect Integration skill provides comprehensive payment platform capabilities using the Stripe Connect API via the official Stripe Node.js SDK (stripe@14.x). It supports both Standard and Express connected account types for marketplace and platform payment scenarios.

Account onboarding is handled through the Account Links API, generating hosted onboarding URLs that guide connected accounts through identity verification and bank account setup. The skill monitors onboarding status via the Accounts API and handles account.updated webhook events.

Payment processing creates PaymentIntents with automatic splitting between platform and connected accounts using application_fee_amount or transfer_data parameters. The skill supports destination charges, separate charges and transfers, and direct charges on connected accounts. Payout scheduling is configurable per connected account. Refund handling processes both platform and connected account refunds with proper fee reversal. Webhook signature verification uses the stripe.webhooks.constructEvent method with endpoint secrets for secure event processing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-integration
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-integration -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-integration -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-integration -a codex
```

### OpenClaw

```bash
clawhub install stripe-connect-integration
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-integration/)
