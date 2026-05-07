---
title: "Stripe Webhook Signature Verifier"
slug: "stripe-webhook-signature-verifier"
description: "Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API."
verification: verified
source: "https://github.com/stripe/stripe-node"
category: "Security & Verification"
framework: "ChatGPT Agents"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
---
# Stripe Webhook Signature Verifier

Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API.

## Installation

1. Clone this skill repository.
2. Open this skill folder.
3. Review prerequisites and setup needs.
4. Install required dependencies.
5. Run and test in your environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/)
