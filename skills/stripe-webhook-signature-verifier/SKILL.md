---
name: "stripe-webhook-signature-verifier"
description: "Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API."
category: "Security &amp; Verification"
framework: "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/"
---

# Stripe Webhook Signature Verifier

Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API.

## Installation

You can install this skill using one of these common methods:

1. **ClawHub** — install from the marketplace if available.
2. **Git clone** — clone the skill folder into your local skills directory.
3. **Download ZIP** — download and extract the skill files manually.
4. **Copy files** — copy the skill directory into your agent skills path.
5. **Package manager / upstream installer** — use the original project installer if the source provides one.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/)
