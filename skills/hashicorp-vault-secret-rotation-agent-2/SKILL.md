---
name: "HashiCorp Vault Secret Rotation Agent"
description: "Connects to HashiCorp Vault HTTP API for automated secret rotation workflows. Manages dynamic database credentials via Vault database secrets engine, handles PKI certificate renewal, and implements lease lifecycle management with TTL monitoring."
category: "Security & Verification"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/hashicorp-vault-secret-rotation-agent-2/"
tool_ecosystem:
  tool: vault
  github_stars: 35275
  github_repo: hashicorp/vault
  maintained: true
---

# HashiCorp Vault Secret Rotation Agent

Connects to HashiCorp Vault HTTP API for automated secret rotation workflows. Manages dynamic database credentials via Vault database secrets engine, handles PKI certificate renewal, and implements lease lifecycle management with TTL monitoring.

## Overview

Connects to HashiCorp Vault HTTP API for automated secret rotation workflows. Manages dynamic database credentials via Vault database secrets engine, handles PKI certificate renewal, and implements lease lifecycle management with TTL monitoring.

Overview

This skill provides automated integration capabilities designed for production agent workflows. It handles authentication, rate limiting, and error recovery out of the box, allowing agents to focus on high-level task orchestration rather than low-level API management.

Key Features

Automatic retry logic with exponential backoff for API rate limits

Structured output formatting compatible with downstream agent pipelines

Comprehensive error handling with actionable diagnostic messages

Configurable caching layer to reduce redundant API calls

Usage

Install via the Agent Skill Exchange registry and configure with your API credentials. The skill exposes a standardized interface that works across supported agent frameworks, with framework-specific optimizations applied automatically during initialization.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-secret-rotation-agent-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-secret-rotation-agent-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-secret-rotation-agent-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-secret-rotation-agent-2 -a codex
```

### OpenClaw

```bash
clawhub install hashicorp-vault-secret-rotation-agent-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/hashicorp-vault-secret-rotation-agent-2/
