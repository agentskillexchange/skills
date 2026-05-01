---
title: "Work with AFFiNE workspaces, documents, and databases from MCP-compatible agents"
description: "Use affine-mcp-server when an agent needs tool-callable access to AFFiNE workspaces, documents, databases, and comments inside an MCP workflow instead of sending a user back to the AFFiNE UI."
verification: "security_reviewed"
source: "https://github.com/DAWNCR0W/affine-mcp-server"
author: "DAWNCR0W"
publisher_type: "individual"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "DAWNCR0W/affine-mcp-server"
  github_stars: 142
  npm_package: "affine-mcp-server"
  npm_weekly_downloads: 2148
---

# Work with AFFiNE workspaces, documents, and databases from MCP-compatible agents

Use affine-mcp-server when an agent needs tool-callable access to AFFiNE workspaces, documents, databases, and comments inside an MCP workflow instead of sending a user back to the AFFiNE UI.

## Prerequisites

Node.js, an MCP-compatible client, and access to an AFFiNE Cloud or self-hosted instance with an API token or saved credentials.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
<p>Install with <code>npm i -g affine-mcp-server</code> or run it ad hoc with <code>npx -y -p affine-mcp-server affine-mcp</code>. Authenticate with <code>affine-mcp login</code>, then add <code>affine-mcp</code> to your MCP client configuration for stdio transport, or run the published Docker image when you need an HTTP MCP endpoint.</p>
```

## Documentation

- https://github.com/DAWNCR0W/affine-mcp-server/blob/main/docs/getting-started.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/work-with-affine-workspaces-documents-and-databases-from-mcp-compatible-agents/)
