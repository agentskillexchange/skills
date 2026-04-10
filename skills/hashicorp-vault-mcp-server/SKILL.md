---
name: HashiCorp Vault MCP Server
description: The official HashiCorp Vault MCP server lets AI assistants read, write,
  list, and delete secrets in Vault&#8217;s KV engine through a safe, auditable MCP
  interface. Supports both stdio and HTTP transports, TLS encryption, and CORS controls.
verification: security_reviewed
source: https://github.com/hashicorp/vault-mcp-server
category:
- Security &amp; Verification
framework:
- MCP
tool_ecosystem:
  github_repo: hashicorp/vault-mcp-server
  github_stars: 42
---
# HashiCorp Vault MCP Server

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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-mcp-server/)
