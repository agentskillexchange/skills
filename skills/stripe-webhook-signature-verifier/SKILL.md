---
name: Stripe Webhook Signature Verifier
description: Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API.
category: Security &amp; Verification
framework: Any Agent
verification: verified_metadata
rating: 4.0
reviews: 36
source: https://agentskillexchange.com/skill/stripe-webhook-signature-verifier/
---

# Stripe Webhook Signature Verifier

Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API.

## Overview

Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill stripe-webhook-signature-verifier
```

### OpenClaw

```bash
clawhub install stripe-webhook-signature-verifier
```

### Claude Code

```bash
claude mcp add stripe-webhook-signature-verifier
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/stripe-webhook-signature-verifier/) for detailed installation instructions.

## Verification

- **Status**: verified_metadata
- **Category**: Security &amp; Verification
- **Framework**: Any Agent
- **Rating**: 4.0/5 (36 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/stripe-webhook-signature-verifier/)
