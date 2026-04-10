---
name: "Obsidian Vault Manager"
description: "Obsidian Vault Manager is built around HashiCorp Vault secrets platform. The underlying ecosystem is represented by hashicorp/vault (35,266+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like KV v2, policies, leases, tokens, transit, dynamic secrets and preserving the [&hellip;]"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/obsidian-vault-manager/"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
---

# Obsidian Vault Manager

Obsidian Vault Manager is built around HashiCorp Vault secrets platform. The underlying ecosystem is represented by hashicorp/vault (35,266+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like KV v2, policies, leases, tokens, transit, dynamic secrets and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to vault so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The implementation typically relies on KV v2, policies, leases, tokens, transit, dynamic secrets, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses KV v2, policies, leases, tokens, transit, dynamic secrets instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as secret management, encryption, and runtime credential delivery.

 Key integration points include secret management, encryption, and runtime credential delivery. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/obsidian-vault-manager/)
