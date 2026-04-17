---
title: "Stripe Connect Platform Bridge"
description: "Manages Stripe Connect onboarding flows using the stripe-node SDK. Handles account creation, capability requests, OAuth redirects, and payout scheduling via the Stripe Accounts API."
verification: security_reviewed
source: "https://github.com/stripe/stripe-node"
category:
  - "Integrations & Connectors"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
  npm_weekly_downloads: 9280426
  license: "MIT"
---

# Stripe Connect Platform Bridge

Manages Stripe Connect onboarding flows using the stripe-node SDK. Handles account creation, capability requests, OAuth redirects, and payout scheduling via the Stripe Accounts API.

This skill automates stripe connect platform bridge operations for agent-driven workflows. It wraps the underlying API client libraries with sensible defaults for authentication, error handling, and pagination. Configuration is managed through environment variables and a local settings file, keeping credentials out of your codebase. The agent validates inputs against the provider’s API schema before making requests, catching configuration errors early. Includes retry logic with exponential backoff for transient failures and structured logging for audit trails. Works in both synchronous command mode and event-driven webhook mode for real-time integrations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stripe-connect-platform-bridge
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/stripe-connect-platform-bridge` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-platform-bridge/)
