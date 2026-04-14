---
title: "HashiCorp Vault MCP Server"
description: "The official HashiCorp Vault MCP server lets AI assistants read, write, list, and delete secrets in Vault’s KV engine through a safe, auditable MCP interface. Supports both stdio and HTTP transports, TLS encryption, and CORS controls."
verification: security_reviewed
source: "https://github.com/hashicorp/vault-mcp-server"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/vault-mcp-server"
  github_stars: 43
---

# HashiCorp Vault MCP Server

The Vault MCP Server is maintained by HashiCorp (IBM) and provides full-featured MCP integration for Vault’s secrets management capabilities.

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
Requires a valid Vault token with appropriate permissions. HTTP mode supports TLS and CORS restrictions. All actions are auditable through Vault’s standard audit log. Intended for local development and controlled environments.

Install notes
Clone and build: git clone https://github.com/hashicorp/vault-mcp-server.git && make build. Or run via Docker. Set VAULT_ADDR and VAULT_TOKEN environment variables.

Source: github.com/hashicorp/vault-mcp-server

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-mcp-server/)
