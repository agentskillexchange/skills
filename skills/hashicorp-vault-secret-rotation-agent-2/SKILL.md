---
title: "HashiCorp Vault Secret Rotation Agent"
description: "Connects to HashiCorp Vault HTTP API for automated secret rotation workflows. Manages dynamic database credentials via Vault database secrets engine, handles PKI certificate renewal, and implements lease lifecycle management with TTL monitoring. Overview This skill provides automated integration capabilities designed for production agent workflows. It handles authentication, rate limiting, and error recovery out of the box, allowing agents to focus on high-level task orchestration rather than low-level API management. Key Features Automatic retry logic with exponential backoff for API rate limits Structured output formatting compatible with downstream agent pipelines Comprehensive error handling with actionable diagnostic messages Configurable caching layer to reduce redundant API calls Usage Install via the Agent Skill Exchange registry and configure with your API credentials. The skill exposes a standardized interface that works across supported agent frameworks, with framework-specific optimizations applied automatically during initialization."
source: "https://github.com/hashicorp/vault"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/vault"
  github_stars: 35418
---

# HashiCorp Vault Secret Rotation Agent

Connects to HashiCorp Vault HTTP API for automated secret rotation workflows. Manages dynamic database credentials via Vault database secrets engine, handles PKI certificate renewal, and implements lease lifecycle management with TTL monitoring. Overview This skill provides automated integration capabilities designed for production agent workflows. It handles authentication, rate limiting, and error recovery out of the box, allowing agents to focus on high-level task orchestration rather than low-level API management. Key Features Automatic retry logic with exponential backoff for API rate limits Structured output formatting compatible with downstream agent pipelines Comprehensive error handling with actionable diagnostic messages Configurable caching layer to reduce redundant API calls Usage Install via the Agent Skill Exchange registry and configure with your API credentials. The skill exposes a standardized interface that works across supported agent frameworks, with framework-specific optimizations applied automatically during initialization.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-secret-rotation-agent-2/)
