---
name: "Terraform MCP Server for Infrastructure as Code"
description: "The official HashiCorp Terraform MCP server integrates with the Terraform Registry and HCP Terraform, enabling AI agents to browse providers, discover modules, manage workspaces, and validate infrastructure configurations through the Model Context Protocol."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform-mcp-server"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hashicorp/terraform-mcp-server"
  github_stars: 1298
---

# Terraform MCP Server for Infrastructure as Code

The Terraform MCP Server is an official Model Context Protocol server built by HashiCorp that provides seamless integration with the Terraform ecosystem. It enables AI agents to interact with Terraform Registry APIs, HCP Terraform, and Terraform Enterprise through structured MCP tool calls, making it a key enabler for infrastructure-as-code automation with AI assistants.
The server supports dual transport modes: Stdio for local integration with coding tools and StreamableHTTP for network-accessible deployments. For security, the HTTP transport includes configurable CORS policies, rate limiting (both global and per-session), TLS support, and allowed-origins restrictions to prevent DNS rebinding attacks.
Core capabilities include direct integration with the public Terraform Registry for browsing providers, modules, and policy libraries. Agents can look up provider documentation, discover available resources and data sources, examine module inputs and outputs, and explore policy packs. For HCP Terraform and Terraform Enterprise environments, the server adds workspace management (create, update, delete), variable configuration, tag management, run triggering, and organization/project listing.
The server can be run via Docker for containerized environments or directly as a binary. Configuration is managed through environment variables including TFE_ADDRESS for custom Terraform Enterprise endpoints, TFE_TOKEN for API authentication, and various MCP_* variables for transport and security settings. The ENABLE_TF_OPERATIONS flag controls access to write operations that require explicit approval.
With over 1,280 GitHub stars and active maintenance by HashiCorp, this server represents the official way to give AI agents structured access to Terraform infrastructure data. It integrates with VS Code, Cursor, Claude Desktop, and other MCP-compatible clients. Licensed under MPL-2.0, it follows HashiCorp standard licensing practices for their open-source tools.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-mcp-server-infrastructure-as-code/)
