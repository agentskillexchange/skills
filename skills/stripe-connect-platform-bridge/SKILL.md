---
name: "Stripe Connect Platform Bridge"
description: "Manages Stripe Connect onboarding flows using the stripe-node SDK. Handles account creation, capability requests, OAuth redirects, and payout scheduling via the Stripe Accounts API."
category: "Integrations & Connectors"
framework: "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/stripe-connect-platform-bridge/"
tool_ecosystem:
  tool: stripe
  github_stars: 4377
  npm_weekly_downloads: 8442269
  github_repo: stripe/stripe-node
  license: MIT
  maintained: true
---

# Stripe Connect Platform Bridge

Manages Stripe Connect onboarding flows using the stripe-node SDK. Handles account creation, capability requests, OAuth redirects, and payout scheduling via the Stripe Accounts API.

## Overview

Manages Stripe Connect onboarding flows using the stripe-node SDK. Handles account creation, capability requests, OAuth redirects, and payout scheduling via the Stripe Accounts API.

This skill automates stripe connect platform bridge operations for agent-driven workflows. It wraps the underlying API client libraries with sensible defaults for authentication, error handling, and pagination. Configuration is managed through environment variables and a local settings file, keeping credentials out of your codebase. The agent validates inputs against the provider’s API schema before making requests, catching configuration errors early. Includes retry logic with exponential backoff for transient failures and structured logging for audit trails. Works in both synchronous command mode and event-driven webhook mode for real-time integrations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-platform-bridge
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-platform-bridge -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-platform-bridge -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stripe-connect-platform-bridge -a codex
```

### OpenClaw

```bash
clawhub install stripe-connect-platform-bridge
```

## Source

- Marketplace: https://agentskillexchange.com/skills/stripe-connect-platform-bridge/
