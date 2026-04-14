---
title: "Stripe Connect Platform Bridge"
description: "Manages Stripe Connect onboarding flows using the stripe-node SDK. Handles account creation, capability requests, OAuth redirects, and payout scheduling via the Stripe Accounts API."
verification: security_reviewed
source: "https://github.com/stripe/stripe-node"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe Connect Platform Bridge

Manages Stripe Connect onboarding flows using the stripe-node SDK. Handles account creation, capability requests, OAuth redirects, and payout scheduling via the Stripe Accounts API.

This skill automates stripe connect platform bridge operations for agent-driven workflows. It wraps the underlying API client libraries with sensible defaults for authentication, error handling, and pagination. Configuration is managed through environment variables and a local settings file, keeping credentials out of your codebase. The agent validates inputs against the provider’s API schema before making requests, catching configuration errors early. Includes retry logic with exponential backoff for transient failures and structured logging for audit trails. Works in both synchronous command mode and event-driven webhook mode for real-time integrations.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-platform-bridge/)
