---
name: "Terraform MCP Server for Infrastructure as Code"
slug: "terraform-mcp-server-infrastructure-as-code"
description: "The official HashiCorp Terraform MCP server integrates with the Terraform Registry and HCP Terraform, enabling AI agents to browse providers, discover modules, manage workspaces, and validate infrastructure configurations through the Model Context Protocol."
github_stars: 1298
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform-mcp-server"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "hashicorp/terraform-mcp-server"
  github_stars: 1298
---

# Terraform MCP Server for Infrastructure as Code

The official HashiCorp Terraform MCP server integrates with the Terraform Registry and HCP Terraform, enabling AI agents to browse providers, discover modules, manage workspaces, and validate infrastructure configurations through the Model Context Protocol.

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -p 8080:8080 --rm -e TRANSPORT_MODE=streamable-http -e TRANSPORT_HOST=0.0.0.0 hashicorp/terraform-mcp-server
- go install github.com/hashicorp/terraform-mcp-server/cmd/terraform-mcp-server@latest
- go install github.com/hashicorp/terraform-mcp-server/cmd/terraform-mcp-server@main
- git clone https://github.com/hashicorp/terraform-mcp-server.git

Requirements and caveats from upstream:
- Ensure [Docker](https://www.docker.com/) is installed and running to use the server in a containerized environment.
- | ENABLE_TF_OPERATIONS | Enable tools that require explicit approval | false |
- "command": "docker",

Basic usage or getting-started notes:
- **Workspace Operations**: Create, update, delete workspaces with support for variables, tags, and run management
- **OTel metrics for monitoring tool usage**: Integration with open telemetry meters to track tool-call volume, latency and failures in Streamable HTTP mode. Also exposes default http server metrics when this feature is...
- Install an AI assistant that supports the Model Context Protocol (MCP).

- Source: https://github.com/hashicorp/terraform-mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/hashicorp/terraform-mcp-server/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-mcp-server-infrastructure-as-code/)
