---
title: "Build n8n workflows from node docs, templates, and schemas through MCP"
description: "Use n8n-MCP when an agent needs structured access to n8n nodes, properties, operations, and template examples while designing or debugging workflows, instead of guessing from raw docs or clicking through the n8n UI by hand."
verification: listed
source: "https://github.com/czlonkowski/n8n-mcp"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "czlonkowski/n8n-mcp"
  github_stars: 18088
  npm_package: "n8n-mcp"
  npm_weekly_downloads: 485039
---

# Build n8n workflows from node docs, templates, and schemas through MCP

Use n8n-MCP when the missing step is reliable workflow authoring context for n8n. It exposes n8n node documentation, property schemas, operations, AI-capable tool variants, and template examples through an MCP server so an agent can search capabilities, choose the right node shape, and draft or troubleshoot workflow changes with fewer hallucinated configurations. The scope boundary is specific enough to be skill-shaped: this is an MCP bridge for n8n workflow design and node selection, not a generic listing for the n8n platform and not just another MCP product card.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-n8n-workflows-from-node-docs-templates-and-schemas-through-mcp/)
