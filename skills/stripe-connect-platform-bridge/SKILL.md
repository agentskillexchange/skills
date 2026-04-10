---
name: Stripe Connect Platform Bridge
description: Manages Stripe Connect onboarding flows using the stripe-node SDK. Handles
  account creation, capability requests, OAuth redirects, and payout scheduling via
  the Stripe Accounts API.
verification: security_reviewed
source: https://agentskillexchange.com/skills/stripe-connect-platform-bridge/
category:
- Integrations &amp; Connectors
framework:
- Claude Agents
---
# Stripe Connect Platform Bridge

Manages Stripe Connect onboarding flows using the stripe-node SDK. Handles account creation, capability requests, OAuth redirects, and payout scheduling via the Stripe Accounts API.
This skill automates stripe connect platform bridge operations for agent-driven workflows. It wraps the underlying API client libraries with sensible defaults for authentication, error handling, and pagination. Configuration is managed through environment variables and a local settings file, keeping credentials out of your codebase. The agent validates inputs against the provider's API schema before making requests, catching configuration errors early. Includes retry logic with exponential backoff for transient failures and structured logging for audit trails. Works in both synchronous command mode and event-driven webhook mode for real-time integrations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-platform-bridge/)
