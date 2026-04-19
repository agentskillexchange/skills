---
title: "Stripe Connect Platform Bridge"
description: "Manages Stripe Connect onboarding flows using the stripe-node SDK. Handles account creation, capability requests, OAuth redirects, and payout scheduling via the Stripe Accounts API. This skill automates stripe connect platform bridge operations for agent-driven workflows. It wraps the underlying API client libraries with sensible defaults for authentication, error handling, and pagination. Configuration is managed through environment variables and a local settings file, keeping credentials out of your codebase. The agent validates inputs against the provider&#8217;s API schema before making requests, catching configuration errors early. Includes retry logic with exponential backoff for transient failures and structured logging for audit trails. Works in both synchronous command mode and event-driven webhook mode for real-time integrations."
source: "https://github.com/stripe/stripe-node"
verification: "security_reviewed"
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

Manages Stripe Connect onboarding flows using the stripe-node SDK. Handles account creation, capability requests, OAuth redirects, and payout scheduling via the Stripe Accounts API. This skill automates stripe connect platform bridge operations for agent-driven workflows. It wraps the underlying API client libraries with sensible defaults for authentication, error handling, and pagination. Configuration is managed through environment variables and a local settings file, keeping credentials out of your codebase. The agent validates inputs against the provider&#8217;s API schema before making requests, catching configuration errors early. Includes retry logic with exponential backoff for transient failures and structured logging for audit trails. Works in both synchronous command mode and event-driven webhook mode for real-time integrations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-platform-bridge/)
