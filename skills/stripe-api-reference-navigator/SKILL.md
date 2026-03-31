---
name: "Stripe API Reference Navigator"
description: "Navigates and queries the Stripe REST API documentation using stripe-node SDK methods. Resolves payment intent lifecycle, webhook event schemas, and Connect platform payout structures with type-safe parameter validation."
category: "Library &amp; API Reference"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/stripe/stripe-node"
tool_ecosystem:
  tool: stripe
  github_repo: stripe/stripe-node
  github_stars: 4377
  license: MIT
  maintained: true
---
# Stripe API Reference Navigator

Navigates and queries the Stripe REST API documentation using stripe-node SDK methods. Resolves payment intent lifecycle, webhook event schemas, and Connect platform payout structures with type-safe parameter validation.

## Overview

The Stripe API Reference Navigator provides intelligent traversal of the entire Stripe REST API surface. Built around the stripe-node SDK, it resolves complex payment flows including PaymentIntent confirmation sequences, SetupIntent lifecycle management, and Subscription billing anchor calculations. The skill understands Connect platform semantics—application fees, destination charges, and separate charges with transfers—and can generate correct API call sequences for multi-party payment scenarios. It parses webhook event payloads against the official Stripe OpenAPI spec, validating that your endpoint handlers cover all required fields. Supports idempotency key strategies, API versioning headers, and automatic pagination through list endpoints using auto-paging iterators. Includes built-in knowledge of rate limit tiers and retry-after semantics for production-grade integrations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stripe-api-reference-navigator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stripe-api-reference-navigator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stripe-api-reference-navigator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stripe-api-reference-navigator -a codex
```

### OpenClaw

```bash
clawhub install stripe-api-reference-navigator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-api-reference-navigator/)
