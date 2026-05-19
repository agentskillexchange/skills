---
name: "Operate Harness pipelines, projects, and delivery resources from MCP-enabled agents"
slug: "operate-harness-pipelines-projects-and-delivery-resources-from-mcp-enabled-agents"
description: "Use the Harness MCP Server when an agent needs governed access to Harness pipelines, services, environments, feature flags, cost data, and related platform resources from an MCP workflow instead of sending a human through the Harness UI."
github_stars: 43
verification: "security_reviewed"
source: "https://github.com/harness/mcp-server"
category: "CI/CD Integrations"
framework: "MCP"
tool_ecosystem:
  github_repo: "harness/mcp-server"
  github_stars: 43
  npm_package: "harness-mcp-v2"
  npm_weekly_downloads: 1019
---

# Operate Harness pipelines, projects, and delivery resources from MCP-enabled agents

Use the Harness MCP Server when an agent needs governed access to Harness pipelines, services, environments, feature flags, cost data, and related platform resources from an MCP workflow instead of sending a human through the Harness UI.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g harness-mcp-v2
- git clone https://github.com/harness/mcp-server.git
- pnpm install
- pnpm build

Requirements and caveats from upstream:
- **Works everywhere.** Stdio transport for local clients (Claude Desktop, Cursor, Windsurf), HTTP transport for remote/shared deployments, Docker and Kubernetes ready.
- **Important:** The hosted MCP service uses **Harness Platform OAuth**, not HARNESS_API_KEY. It must also be enabled/configured per account by **Harness Support** before the endpoint can be used.

Basic usage or getting-started notes:
- Before installing or running the server, you need a Harness API key:
- Log in to your [Harness account](https://app.harness.io)
- Go to **My Profile** → **API Keys** → **+ New API Key**

- Source: https://github.com/harness/mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/harness/mcp-server/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/operate-harness-pipelines-projects-and-delivery-resources-from-mcp-enabled-agents/)
