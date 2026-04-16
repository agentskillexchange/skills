---
title: "Stripe Connect Account Provisioner"
description: "Automates Stripe Connect onboarding by provisioning connected accounts via the Stripe API. Handles account creation, KYC link generation with stripe.accountLinks.create(), and webhook verification for account.updated events."
verification: "security_reviewed"
source: "https://github.com/stripe/stripe-node"
category:
  - "Integrations &amp; Connectors"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  ase_npm_package: "stripe"
  npm_weekly_downloads: 9280426
  license: "MIT"
---

# Stripe Connect Account Provisioner

The Stripe Connect Account Provisioner streamlines marketplace and platform onboarding by automating the entire Stripe Connect account lifecycle. It uses the Stripe Node.js SDK to create Standard, Express, or Custom connected accounts programmatically.

Key capabilities include generating onboarding links via stripe.accountLinks.create(), monitoring account status through account.updated webhooks, and handling retry logic for failed verifications. The agent validates required fields (business_type, country, capabilities) before submission and provides detailed error mapping for common KYC rejection reasons.

Built-in support for idempotency keys prevents duplicate account creation during retries. The skill also manages capability requests (card_payments, transfers) and tracks payout schedules. Integrates with Stripe Dashboard API for real-time balance monitoring of connected accounts. Supports both test and live mode with automatic environment detection.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-account-provisioner/)
