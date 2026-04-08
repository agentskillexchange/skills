---
title: "Stripe Webhook Signature Verifier"
slug: "stripe-webhook-signature-verifier"
description: "Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API."
category:
  - "Security &amp; Verification"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/"
---

# Stripe Webhook Signature Verifier

Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/)
