---
title: "Stripe Connect Account Provisioner"
description: "The Stripe Connect Account Provisioner streamlines marketplace and platform onboarding by automating the entire Stripe Connect account lifecycle. It uses the Stripe Node.js SDK to create Standard, Express, or Custom connected accounts programmatically. Key capabilities include generating onboarding links via stripe.accountLinks.create() , monitoring account status through account.updated webhooks, and handling retry logic for failed verifications. The agent validates required fields (business_type, country, capabilities) before submission and provides detailed error mapping for common KYC rejection reasons. Built-in support for idempotency keys prevents duplicate account creation during retries. The skill also manages capability requests (card_payments, transfers) and tracks payout schedules. Integrates with Stripe Dashboard API for real-time balance monitoring of connected accounts. Supports both test and live mode with automatic environment detection."
source: "https://github.com/stripe/stripe-node"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe Connect Account Provisioner

The Stripe Connect Account Provisioner streamlines marketplace and platform onboarding by automating the entire Stripe Connect account lifecycle. It uses the Stripe Node.js SDK to create Standard, Express, or Custom connected accounts programmatically. Key capabilities include generating onboarding links via stripe.accountLinks.create() , monitoring account status through account.updated webhooks, and handling retry logic for failed verifications. The agent validates required fields (business_type, country, capabilities) before submission and provides detailed error mapping for common KYC rejection reasons. Built-in support for idempotency keys prevents duplicate account creation during retries. The skill also manages capability requests (card_payments, transfers) and tracks payout schedules. Integrates with Stripe Dashboard API for real-time balance monitoring of connected accounts. Supports both test and live mode with automatic environment detection.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-account-provisioner/)
