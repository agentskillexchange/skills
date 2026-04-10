---
title: "Stripe Webhook Signature Verifier"
description: "Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API."
slug: "stripe-webhook-signature-verifier"
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

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install stripe-webhook-signature-verifier
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill implements secure Stripe webhook signature verification using the Stripe.js SDK and the stripe.webhooks.constructEvent method. It extracts the raw request body before any JSON parsing to preserve byte accuracy, then validates the Stripe-Signature header timestamp and HMAC-SHA256 signature against the endpoint secret. The skill enforces a configurable tolerance window (default 300 seconds) to prevent replay attacks. Failed verifications are logged to Datadog via the Datadog Logs API using the POST /api/v2/logs endpoint with structured metadata including event type, timestamp, and remote IP. Successful verifications emit metrics to Datadog StatsD for dashboard monitoring. The skill supports both synchronous Express middleware and async Lambda function handlers for AWS API Gateway, with examples for Fastify and Hono frameworks. It also includes integration with Clerk webhooks and Paddle billing events using the same signature pattern.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/)
