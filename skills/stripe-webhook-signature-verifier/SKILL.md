---
title: "Stripe Webhook Signature Verifier"
slug: "stripe-webhook-signature-verifier"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/"
category:
  - "Security &amp; Verification"
framework:
  - "ChatGPT Agents"
---
# Stripe Webhook Signature Verifier

Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/)
