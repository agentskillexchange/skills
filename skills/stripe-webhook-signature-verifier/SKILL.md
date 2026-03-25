---
name: "Stripe Webhook Signature Verifier"
description: "Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API."
category: "Security & Verification"
framework: "ChatGPT Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "stripe"  # from ase_tool_match
  github_stars: 4377  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8442269  # from ase_npm_downloads
  github_repo: "stripe/stripe-node"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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
