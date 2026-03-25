---
name: "Bubble.io Stripe Subscription Portal Builder"
description: "Uses Bubble’s Plugin API and the Stripe.js SDK to embed a self-service subscription management portal inside a Bubble application. Configures Bubble’s API Connector to call Stripe’s Billing Portal Sessions endpoint and handles webhook events for real-time plan change updates."
category: "Templates & Workflows"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/bubble-stripe-subscription-portal/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "stripe"  # from ase_tool_match
  github_stars: 4377  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8442269  # from ase_npm_downloads
  github_repo: "stripe/stripe-node"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Bubble.io Stripe Subscription Portal Builder

Uses Bubble’s Plugin API and the Stripe.js SDK to embed a self-service subscription management portal inside a Bubble application. Configures Bubble’s API Connector to call Stripe’s Billing Portal Sessions endpoint and handles webhook events for real-time plan change updates.

## Overview

**Bubble.io Stripe Subscription Portal Builder** is built around Stripe payments platform. The underlying ecosystem is represented by `stripe/stripe-node` (4,377+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like charges, payment intents, subscriptions, billing, payouts, webhooks, reports and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to stripe so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Uses Bubble's Plugin API and the Stripe.js SDK to embed a self-service subscription management portal inside a Bubble application. Configures Bubble's API Connector to call Stripe's Billing Portal Sessions endpoint and handles webhook events for real-time plan change updates. The implementation typically relies on charges, payment intents, subscriptions, billing, payouts, webhooks, reports, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses charges, payment intents, subscriptions, billing, payouts, webhooks, reports instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as billing automation, reconciliation, subscriptions, and financial analytics.

For generator-style use cases, the skill turns a vague request into repeatable scaffolding with defaults that match the upstream toolchain rather than inventing ad hoc files. Key integration points include billing automation, reconciliation, subscriptions, and financial analytics. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill bubble-stripe-subscription-portal
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill bubble-stripe-subscription-portal -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill bubble-stripe-subscription-portal -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill bubble-stripe-subscription-portal -a codex
```

### OpenClaw

```bash
clawhub install bubble-stripe-subscription-portal
```

## Source

- Marketplace: https://agentskillexchange.com/skills/bubble-stripe-subscription-portal/
