---
name: "Stripe API Reference Navigator"
description: "Navigates and queries the Stripe REST API documentation using stripe-node SDK methods. Resolves payment intent lifecycle, webhook event schemas, and Connect platform payout structures with type-safe parameter validation."
category: "Library & API Reference"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/stripe-api-reference-navigator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "stripe"  # from ase_tool_match
  github_stars: 4377  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8442269  # from ase_npm_downloads
  github_repo: "stripe/stripe-node"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/stripe-api-reference-navigator/
