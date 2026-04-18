---
title: "Stripe API Reference Navigator"
description: "Navigates and queries the Stripe REST API documentation using stripe-node SDK methods. Resolves payment intent lifecycle, webhook event schemas, and Connect platform payout structures with type-safe parameter validation."
verification: security_reviewed
source: "https://github.com/stripe/stripe-node"
category:
  - "Library & API Reference"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  ase_npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe API Reference Navigator

The Stripe API Reference Navigator provides intelligent traversal of the entire Stripe REST API surface. Built around the stripe-node SDK, it resolves complex payment flows including PaymentIntent confirmation sequences, SetupIntent lifecycle management, and Subscription billing anchor calculations. The skill understands Connect platform semantics—application fees, destination charges, and separate charges with transfers—and can generate correct API call sequences for multi-party payment scenarios. It parses webhook event payloads against the official Stripe OpenAPI spec, validating that your endpoint handlers cover all required fields. Supports idempotency key strategies, API versioning headers, and automatic pagination through list endpoints using auto-paging iterators. Includes built-in knowledge of rate limit tiers and retry-after semantics for production-grade integrations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stripe-api-reference-navigator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/stripe-api-reference-navigator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-api-reference-navigator/)
