---
name: "n8n-nodes-mcp Community Node for Model Context Protocol Workflows"
description: "n8n-nodes-mcp is a real n8n community node that lets self-hosted n8n instances connect to Model Context Protocol servers. This skill covers installing the package, configuring MCP transports inside n8n, and using the node in automation workflows that need external tools and structured context exchange."
verification: security_reviewed
source: "https://github.com/nerding-io/n8n-nodes-mcp"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "nerding-io/n8n-nodes-mcp"
  github_stars: 3003
---

# n8n-nodes-mcp Community Node for Model Context Protocol Workflows

n8n-nodes-mcp is a community package published to npm and maintained by nerding.io. It extends self-hosted n8n with nodes for connecting to Model Context Protocol servers, making it useful for automations that need to call MCP tools from inside a workflow graph. The project has an active GitHub repository, a public npm package, and clear relevance for users combining workflow automation with MCP-compatible services.
The job to be done here is concrete: install the node into a self-hosted n8n instance, add it to a workflow, point it at an MCP server, and use the returned tools or resources as part of larger business logic. That can include routing data between SaaS systems, triggering external tools from automation steps, or exposing MCP-backed capabilities to other workflow stages. Because n8n already handles scheduling, credentials, retries, and branching, this node becomes a practical bridge between visual automation and MCP tooling.
In operational terms, the key integration points are npm-based installation, n8n community node support, and MCP server connectivity. This skill belongs in the connectors space because it is primarily about wiring systems together: n8n on one side, MCP services on the other, with a reusable automation surface in the middle.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/n8n-nodes-mcp-community-node-model-context-protocol-workflows/)
