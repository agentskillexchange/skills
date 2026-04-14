---
title: "n8n-nodes-mcp Community Node for Model Context Protocol Workflows"
description: "n8n-nodes-mcp is a real n8n community node that lets self-hosted n8n instances connect to Model Context Protocol servers. This skill covers installing the package, configuring MCP transports inside n8n, and using the node in automation workflows that need external tools and structured context exchange."
verification: security_reviewed
source: "https://github.com/nerding-io/n8n-nodes-mcp"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "nerding-io/n8n-nodes-mcp"
  github_stars: 3002
---

# n8n-nodes-mcp Community Node for Model Context Protocol Workflows

n8n-nodes-mcp is a community package published to npm and maintained by nerding.io. It extends self-hosted n8n with nodes for connecting to Model Context Protocol servers, making it useful for automations that need to call MCP tools from inside a workflow graph. The project has an active GitHub repository, a public npm package, and clear relevance for users combining workflow automation with MCP-compatible services.

The job to be done here is concrete: install the node into a self-hosted n8n instance, add it to a workflow, point it at an MCP server, and use the returned tools or resources as part of larger business logic. That can include routing data between SaaS systems, triggering external tools from automation steps, or exposing MCP-backed capabilities to other workflow stages. Because n8n already handles scheduling, credentials, retries, and branching, this node becomes a practical bridge between visual automation and MCP tooling.

In operational terms, the key integration points are npm-based installation, n8n community node support, and MCP server connectivity. This skill belongs in the connectors space because it is primarily about wiring systems together: n8n on one side, MCP services on the other, with a reusable automation surface in the middle.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/n8n-nodes-mcp-community-node-model-context-protocol-workflows/)
