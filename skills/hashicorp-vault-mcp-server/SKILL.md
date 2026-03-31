---
name: "HashiCorp Vault MCP Server"
description: "The official HashiCorp Vault MCP server lets AI assistants read, write, list, and delete secrets in Vault's KV engine through a safe, auditable MCP interface. Supports both stdio and HTTP transports, TLS encryption, and CORS controls."
category: "Security &amp; Verification"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/hashicorp-vault-mcp-server/"
---
# HashiCorp Vault MCP Server

The official HashiCorp Vault MCP server lets AI assistants read, write, list, and delete secrets in Vault's KV engine through a safe, auditable MCP interface. Supports both stdio and HTTP transports, TLS encryption, and CORS controls.

## Overview

The Vault MCP Server is maintained by HashiCorp (IBM) and provides full-featured MCP integration for Vault's secrets management capabilities.

Best for

Reading API keys and secrets during development without leaving the agent workflow
Provisioning new secret paths and managing KV mounts
Managing Vault policies through natural language
DevOps teams integrating secrets management into AI-assisted infrastructure workflows

Key capabilities

Secret operations: Write, read, list, and delete secrets in KV mounts (v1 and v2)
Mount management: Create new mounts, list available mounts, and delete mounts
Policy management: Read and manage Vault policies
Dual transport: Stdio mode for local and StreamableHTTP for remote integrations

Security model
Requires a valid Vault token with appropriate permissions. HTTP mode supports TLS and CORS restrictions. All actions are auditable through Vault's standard audit log. Intended for local development and controlled environments.

Install notes
Clone and build: git clone https://github.com/hashicorp/vault-mcp-server.git && make build. Or run via Docker. Set VAULT_ADDR and VAULT_TOKEN environment variables.

Source: github.com/hashicorp/vault-mcp-server

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill hashicorp-vault-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install hashicorp-vault-mcp-server
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-mcp-server/)
