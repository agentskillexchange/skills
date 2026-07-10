---
name: "HashiCorp Vault MCP Server"
slug: "hashicorp-vault-mcp-server"
description: "The official HashiCorp Vault MCP server lets AI assistants read, write, list, and delete secrets in Vault's KV engine through a safe, auditable MCP interface. Supports both stdio and HTTP transports, TLS encryption, and CORS controls."
github_stars: 49
verification: "security_reviewed"
source: "https://github.com/hashicorp/vault-mcp-server"
author: "HashiCorp"
publisher_type: "company"
category: "Security & Verification"
framework: "MCP"
tool_ecosystem:
  github_repo: "hashicorp/vault-mcp-server"
  github_stars: 49
---

# HashiCorp Vault MCP Server

The official HashiCorp Vault MCP server lets AI assistants read, write, list, and delete secrets in Vault's KV engine through a safe, auditable MCP interface. Supports both stdio and HTTP transports, TLS encryption, and CORS controls.

## Prerequisites

MCP-compatible client, HashiCorp Vault server, Vault token with appropriate permissions, Go 1.24+ or Docker

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/hashicorp/vault-mcp-server.git
- make build
- make run-http
- make docker-build

Requirements and caveats from upstream:
- Docker
- "command": "docker",
- ## Working with Docker

Basic usage or getting-started notes:
- Go 1.24 or later (if building from source)
- HashiCorp Vault server running locally or remotely
- A valid Vault token with appropriate permissions

- Source: https://github.com/hashicorp/vault-mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/hashicorp/vault-mcp-server/HEAD/README.md

## Documentation

- https://developer.hashicorp.com/vault/docs/mcp-server/overview

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hashicorp-vault-mcp-server/)
