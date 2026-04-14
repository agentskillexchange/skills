---
title: "Stripe Connect Integration"
description: "Manages Stripe Connect accounts and payment flows using the Stripe Node.js SDK (stripe@14.x). Handles onboarding via Account Links API, creates PaymentIntents with application fees, and processes Connect webhooks."
verification: security_reviewed
source: "https://github.com/stripe/stripe-node"
category:
  - "Integrations &amp; Connectors"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe Connect Integration

The Stripe Connect Integration skill provides comprehensive payment platform capabilities using the Stripe Connect API via the official Stripe Node.js SDK (stripe@14.x). It supports both Standard and Express connected account types for marketplace and platform payment scenarios.

Account onboarding is handled through the Account Links API, generating hosted onboarding URLs that guide connected accounts through identity verification and bank account setup. The skill monitors onboarding status via the Accounts API and handles account.updated webhook events.

Payment processing creates PaymentIntents with automatic splitting between platform and connected accounts using application_fee_amount or transfer_data parameters. The skill supports destination charges, separate charges and transfers, and direct charges on connected accounts. Payout scheduling is configurable per connected account. Refund handling processes both platform and connected account refunds with proper fee reversal. Webhook signature verification uses the stripe.webhooks.constructEvent method with endpoint secrets for secure event processing.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-integration/)
