---
title: "n8n-nodes-mcp Community Node for Model Context Protocol Workflows"
description: "n8n-nodes-mcp is a real n8n community node that lets self-hosted n8n instances connect to Model Context Protocol servers. This skill covers installing the package, configuring MCP transports inside n8n, and using the node in automation workflows that need external tools and structured context exchange."
slug: "n8n-nodes-mcp-community-node-model-context-protocol-workflows"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/nerding-io/n8n-nodes-mcp"
tool_ecosystem:
  github_repo: "nerding-io/n8n-nodes-mcp"
  github_stars: 3003
listed: true
---

# n8n-nodes-mcp Community Node for Model Context Protocol Workflows

n8n-nodes-mcp is a real n8n community node that lets self-hosted n8n instances connect to Model Context Protocol servers. This skill covers installing the package, configuring MCP transports inside n8n, and using the node in automation workflows that need external tools and structured context exchange.

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
clawhub install n8n-nodes-mcp-community-node-model-context-protocol-workflows
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

n8n-nodes-mcp is a community package published to npm and maintained by nerding.io. It extends self-hosted n8n with nodes for connecting to Model Context Protocol servers, making it useful for automations that need to call MCP tools from inside a workflow graph. The project has an active GitHub repository, a public npm package, and clear relevance for users combining workflow automation with MCP-compatible services.
The job to be done here is concrete: install the node into a self-hosted n8n instance, add it to a workflow, point it at an MCP server, and use the returned tools or resources as part of larger business logic. That can include routing data between SaaS systems, triggering external tools from automation steps, or exposing MCP-backed capabilities to other workflow stages. Because n8n already handles scheduling, credentials, retries, and branching, this node becomes a practical bridge between visual automation and MCP tooling.
In operational terms, the key integration points are npm-based installation, n8n community node support, and MCP server connectivity. This skill belongs in the connectors space because it is primarily about wiring systems together: n8n on one side, MCP services on the other, with a reusable automation surface in the middle.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/n8n-nodes-mcp-community-node-model-context-protocol-workflows/)
