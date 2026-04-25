---
title: "HashiCorp Vault MCP Server"
description: "The official HashiCorp Vault MCP server lets AI assistants read, write, list, and delete secrets in Vault’s KV engine through a safe, auditable MCP interface. Supports both stdio and HTTP transports, TLS encryption, and CORS controls."
verification: "security_reviewed"
source: "https://github.com/hashicorp/vault-mcp-server"
category:
  - "Security & Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/vault-mcp-server"
  github_stars: 45
---

# HashiCorp Vault MCP Server

The Vault MCP Server is maintained by HashiCorp (IBM) and provides full-featured MCP integration for Vault’s secrets management capabilities. Best for Reading API keys and secrets during development without leaving the agent workflow Provisioning new secret paths and managing KV mounts Managing Vault policies through natural language DevOps teams integrating secrets management into AI-assisted infrastructure workflows Key capabilities Secret operations: Write, read, list, and delete secrets in KV mounts (v1 and v2) Mount management: Create new mounts, list available mounts, and delete mounts Policy management: Read and manage Vault policies Dual transport: Stdio mode for local and StreamableHTTP for remote integrations Security model Requires a valid Vault token with appropriate permissions. HTTP mode supports TLS and CORS restrictions. All actions are auditable through Vault’s standard audit log. Intended for local development and controlled environments. Install notes Clone and build: git clone https://github.com/hashicorp/vault-mcp-server.git && make build. Or run via Docker. Set VAULT_ADDR and VAULT_TOKEN environment variables. Source: github.com/hashicorp/vault-mcp-server

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/hashicorp-vault-mcp-server/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/hashicorp-vault-mcp-server
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/hashicorp-vault-mcp-server`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-mcp-server/)
