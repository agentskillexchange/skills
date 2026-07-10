---
name: "Connect Azure DevOps projects, work items, repos, and pipelines to MCP agents"
slug: "connect-azure-devops-projects-work-items-repos-and-pipelines-to-mcp-agents"
description: "Use Azure DevOps MCP when an agent needs governed access to ADO projects, work items, builds, repos, test plans, wikis, and pipelines."
github_stars: 1725
verification: "security_reviewed"
source: "https://github.com/microsoft/azure-devops-mcp"
author: "Microsoft"
publisher_type: "organization"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "microsoft/azure-devops-mcp"
  github_stars: 1725
  npm_package: "@azure-devops/mcp"
  npm_weekly_downloads: 334283
---

# Connect Azure DevOps projects, work items, repos, and pipelines to MCP agents

Use Azure DevOps MCP when an agent needs governed access to ADO projects, work items, builds, repos, test plans, wikis, and pipelines.

## Prerequisites

Azure DevOps organization, MCP-capable client, Microsoft authentication, and Node.js 20+ for the optional local stdio server

## Installation

Requirements and caveats from upstream:
- Start with the Remote MCP Server first. Use the local MCP Server only if your scenario specifically requires a local stdio setup.
- Install [Node.js](https://nodejs.org/en/download) 20+

Basic usage or getting-started notes:
- "Update the wiki page '/Getting Started' with new onboarding instructions"
- Use this configuration to connect directly to the Azure DevOps-hosted endpoint using streamable HTTP transport:
- json

- Source: https://github.com/microsoft/azure-devops-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/microsoft/azure-devops-mcp/HEAD/README.md

## Documentation

- https://learn.microsoft.com/en-us/azure/devops/mcp-server/remote-mcp-server?view=azure-devops

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/connect-azure-devops-projects-work-items-repos-and-pipelines-to-mcp-agents/)
