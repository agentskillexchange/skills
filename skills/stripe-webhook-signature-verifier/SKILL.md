---
title: Stripe Webhook Signature Verifier
description: This skill implements secure Stripe webhook signature verification using
  the Stripe.js SDK and the stripe.webhooks.constructEvent method. It extracts the
  raw request body before any JSON parsing to preserve byte accuracy, then validates
  the Stripe-Signature header timestamp and HMAC-SHA256 signature against the endpoint
  secret. The skill enforces a configurable tolerance window (default 300 seconds)
  to prevent replay attacks. Failed verifications are logged to Datadog via the Datadog
  Logs API using the POST /api/v2/logs endpoint with structured metadata including
  event type, timestamp, and remote IP. Successful verifications emit metrics to Datadog
  StatsD for dashboard monitoring. The skill supports both synchronous Express middleware
  and async Lambda function handlers for AWS API Gateway, with examples for Fastify
  and Hono frameworks. It also includes integration with Clerk webhooks and Paddle
  billing events using the same signature pattern.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/
category:
- Security &amp; Verification
framework:
- ChatGPT Agents
---

# Stripe Webhook Signature Verifier

This skill implements secure Stripe webhook signature verification using the Stripe.js SDK and the stripe.webhooks.constructEvent method. It extracts the raw request body before any JSON parsing to preserve byte accuracy, then validates the Stripe-Signature header timestamp and HMAC-SHA256 signature against the endpoint secret. The skill enforces a configurable tolerance window (default 300 seconds) to prevent replay attacks. Failed verifications are logged to Datadog via the Datadog Logs API using the POST /api/v2/logs endpoint with structured metadata including event type, timestamp, and remote IP. Successful verifications emit metrics to Datadog StatsD for dashboard monitoring. The skill supports both synchronous Express middleware and async Lambda function handlers for AWS API Gateway, with examples for Fastify and Hono frameworks. It also includes integration with Clerk webhooks and Paddle billing events using the same signature pattern.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/)
