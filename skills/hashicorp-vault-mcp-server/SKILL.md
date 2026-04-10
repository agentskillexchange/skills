---
title: "HashiCorp Vault MCP Server"
description: "The official HashiCorp Vault MCP server lets AI assistants read, write, list, and delete secrets in Vault’s KV engine through a safe, auditable MCP interface. Supports both stdio and HTTP transports, TLS encryption, and CORS controls."
slug: "hashicorp-vault-mcp-server"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/hashicorp/vault-mcp-server"
tool_ecosystem:
  github_repo: "hashicorp/vault-mcp-server"
  github_stars: 42
listed: true
---

# HashiCorp Vault MCP Server

The official HashiCorp Vault MCP server lets AI assistants read, write, list, and delete secrets in Vault’s KV engine through a safe, auditable MCP interface. Supports both stdio and HTTP transports, TLS encryption, and CORS controls.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install hashicorp-vault-mcp-server
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Vault MCP Server is maintained by HashiCorp (IBM) and provides full-featured MCP integration for Vault’s secrets management capabilities.
Best for
- Reading API keys and secrets during development without leaving the agent workflow
- Provisioning new secret paths and managing KV mounts
- Managing Vault policies through natural language
- DevOps teams integrating secrets management into AI-assisted infrastructure workflows
Key capabilities
- Secret operations: Write, read, list, and delete secrets in KV mounts (v1 and v2)
- Mount management: Create new mounts, list available mounts, and delete mounts
- Policy management: Read and manage Vault policies
- Dual transport: Stdio mode for local and StreamableHTTP for remote integrations
Security model
Requires a valid Vault token with appropriate permissions. HTTP mode supports TLS and CORS restrictions. All actions are auditable through Vault’s standard audit log. Intended for local development and controlled environments.
Install notes
Clone and build: git clone https://github.com/hashicorp/vault-mcp-server.git && make build. Or run via Docker. Set VAULT_ADDR and VAULT_TOKEN environment variables.
Source: github.com/hashicorp/vault-mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-mcp-server/)
