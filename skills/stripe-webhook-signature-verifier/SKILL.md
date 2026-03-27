---
name: "Stripe Webhook Signature Verifier"
description: "Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API."
category: "Security & Verification"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/"
tool_ecosystem:
  tool: stripe
  github_stars: 4377
  npm_weekly_downloads: 8442269
  github_repo: stripe/stripe-node
  license: MIT
  maintained: true
---

# Stripe Webhook Signature Verifier

Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API.

## Overview

This skill implements secure Stripe webhook signature verification using the Stripe.js SDK and the stripe.webhooks.constructEvent method. It extracts the raw request body before any JSON parsing to preserve byte accuracy, then validates the Stripe-Signature header timestamp and HMAC-SHA256 signature against the endpoint secret. The skill enforces a configurable tolerance window (default 300 seconds) to prevent replay attacks. Failed verifications are logged to Datadog via the Datadog Logs API using the POST /api/v2/logs endpoint with structured metadata including event type, timestamp, and remote IP. Successful verifications emit metrics to Datadog StatsD for dashboard monitoring. The skill supports both synchronous Express middleware and async Lambda function handlers for AWS API Gateway, with examples for Fastify and Hono frameworks. It also includes integration with Clerk webhooks and Paddle billing events using the same signature pattern.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stripe-webhook-signature-verifier
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stripe-webhook-signature-verifier -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stripe-webhook-signature-verifier -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stripe-webhook-signature-verifier -a codex
```

### OpenClaw

```bash
clawhub install stripe-webhook-signature-verifier
```

## Source

- Marketplace: https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/
