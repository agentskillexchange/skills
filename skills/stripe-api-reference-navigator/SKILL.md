---
title: "Stripe API Reference Navigator"
description: "Navigates and queries the Stripe REST API documentation using stripe-node SDK methods. Resolves payment intent lifecycle, webhook event schemas, and Connect platform payout structures with type-safe parameter validation."
verification: "security_reviewed"
source: "https://github.com/stripe/stripe-node"
category:
  - "Library &amp; API Reference"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  ase_npm_package: "stripe"
  npm_weekly_downloads: 9280426
  license: "MIT"
---

# Stripe API Reference Navigator

The Stripe API Reference Navigator provides intelligent traversal of the entire Stripe REST API surface. Built around the stripe-node SDK, it resolves complex payment flows including PaymentIntent confirmation sequences, SetupIntent lifecycle management, and Subscription billing anchor calculations. The skill understands Connect platform semantics—application fees, destination charges, and separate charges with transfers—and can generate correct API call sequences for multi-party payment scenarios. It parses webhook event payloads against the official Stripe OpenAPI spec, validating that your endpoint handlers cover all required fields. Supports idempotency key strategies, API versioning headers, and automatic pagination through list endpoints using auto-paging iterators. Includes built-in knowledge of rate limit tiers and retry-after semantics for production-grade integrations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-api-reference-navigator/)
