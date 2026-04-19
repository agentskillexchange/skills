---
title: "HashiCorp Vault MCP Server"
description: "The Vault MCP Server is maintained by HashiCorp (IBM) and provides full-featured MCP integration for Vault&#8217;s secrets management capabilities. Best for Reading API keys and secrets during development without leaving the agent workflow Provisioning new secret paths and managing KV mounts Managing Vault policies through natural language DevOps teams integrating secrets management into AI-assisted infrastructure workflows Key capabilities Secret operations: Write, read, list, and delete secrets in KV mounts (v1 and v2) Mount management: Create new mounts, list available mounts, and delete mounts Policy management: Read and manage Vault policies Dual transport: Stdio mode for local and StreamableHTTP for remote integrations Security model Requires a valid Vault token with appropriate permissions. HTTP mode supports TLS and CORS restrictions. All actions are auditable through Vault&#8217;s standard audit log. Intended for local development and controlled environments. Install notes Clone and build: git clone https://github.com/hashicorp/vault-mcp-server.git && make build . Or run via Docker. Set VAULT_ADDR and VAULT_TOKEN environment variables. Source: github.com/hashicorp/vault-mcp-server"
source: "https://github.com/hashicorp/vault-mcp-server"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/vault-mcp-server"
  github_stars: 43
---

# HashiCorp Vault MCP Server

The Vault MCP Server is maintained by HashiCorp (IBM) and provides full-featured MCP integration for Vault&#8217;s secrets management capabilities. Best for Reading API keys and secrets during development without leaving the agent workflow Provisioning new secret paths and managing KV mounts Managing Vault policies through natural language DevOps teams integrating secrets management into AI-assisted infrastructure workflows Key capabilities Secret operations: Write, read, list, and delete secrets in KV mounts (v1 and v2) Mount management: Create new mounts, list available mounts, and delete mounts Policy management: Read and manage Vault policies Dual transport: Stdio mode for local and StreamableHTTP for remote integrations Security model Requires a valid Vault token with appropriate permissions. HTTP mode supports TLS and CORS restrictions. All actions are auditable through Vault&#8217;s standard audit log. Intended for local development and controlled environments. Install notes Clone and build: git clone https://github.com/hashicorp/vault-mcp-server.git && make build . Or run via Docker. Set VAULT_ADDR and VAULT_TOKEN environment variables. Source: github.com/hashicorp/vault-mcp-server

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-mcp-server/)
