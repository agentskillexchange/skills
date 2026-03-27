---
name: "Obsidian Vault Manager"
description: "Obsidian Vault Manager is built around HashiCorp Vault secrets platform. The underlying ecosystem is represented by hashicorp/vault (35,266+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like KV v2, policies, leases, tokens, transit, dynamic secrets and preserving the […]"
category: "Developer Tools"
framework: "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/obsidian-vault-manager/"
tool_ecosystem:
  tool: vault
  github_stars: 35275
  github_repo: hashicorp/vault
  maintained: true
---

# Obsidian Vault Manager

Obsidian Vault Manager is built around HashiCorp Vault secrets platform. The underlying ecosystem is represented by hashicorp/vault (35,266+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like KV v2, policies, leases, tokens, transit, dynamic secrets and preserving the […]

## Overview

**Obsidian Vault Manager** is built around HashiCorp Vault secrets platform. The underlying ecosystem is represented by `hashicorp/vault` (35,266+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like KV v2, policies, leases, tokens, transit, dynamic secrets and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to vault so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on KV v2, policies, leases, tokens, transit, dynamic secrets, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses KV v2, policies, leases, tokens, transit, dynamic secrets instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as secret management, encryption, and runtime credential delivery.

Key integration points include secret management, encryption, and runtime credential delivery. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill obsidian-vault-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill obsidian-vault-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill obsidian-vault-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill obsidian-vault-manager -a codex
```

### OpenClaw

```bash
clawhub install obsidian-vault-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/obsidian-vault-manager/
