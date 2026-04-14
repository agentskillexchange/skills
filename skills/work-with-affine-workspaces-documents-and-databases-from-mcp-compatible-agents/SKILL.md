---
title: "Work with AFFiNE workspaces, documents, and databases from MCP-compatible agents"
description: "Use affine-mcp-server when an agent needs tool-callable access to AFFiNE workspaces, documents, databases, and comments inside an MCP workflow instead of sending a user back to the AFFiNE UI."
verification: security_reviewed
source: "https://github.com/DAWNCR0W/affine-mcp-server"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "DAWNCR0W/affine-mcp-server"
  github_stars: 142
  npm_package: "affine-mcp-server"
  npm_weekly_downloads: 2148
---

# Work with AFFiNE workspaces, documents, and databases from MCP-compatible agents

affine-mcp-server gives an MCP-compatible agent a bounded AFFiNE workspace workflow. It can read and update server-backed workspaces, search and edit documents, inspect or fill databases, work with comments, and automate repeatable knowledge-base operations from an agent session instead of making a human click through the AFFiNE app.

The scope is narrow enough to be skill-shaped: this is for agent-side AFFiNE workspace operations through MCP. It is not a generic AFFiNE product card, not a general knowledge-base platform listing, and not a catch-all collaboration suite entry. Invoke it when the missing step is structured workspace access inside an MCP workflow, not when the user simply wants to browse AFFiNE normally or evaluate AFFiNE as a product.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/work-with-affine-workspaces-documents-and-databases-from-mcp-compatible-agents/)
