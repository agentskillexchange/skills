---
title: "Stripe Webhook Signature Verifier"
description: "Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API."
verification: "security_reviewed"
source: "https://github.com/stripe/stripe-node"
category:
  - "Security & Verification"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe Webhook Signature Verifier

Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stripe-webhook-signature-verifier
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/stripe-webhook-signature-verifier`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/)
