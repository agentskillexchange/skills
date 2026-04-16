---
title: "Work with AFFiNE workspaces, documents, and databases from MCP-compatible agents"
description: "Use affine-mcp-server when an agent needs tool-callable access to AFFiNE workspaces, documents, databases, and comments inside an MCP workflow instead of sending a user back to the AFFiNE UI."
verification: "security_reviewed"
source: "https://github.com/DAWNCR0W/affine-mcp-server"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "DAWNCR0W/affine-mcp-server"
  github_stars: 142
  ase_npm_package: "affine-mcp-server"
  npm_weekly_downloads: 2148
---

# Work with AFFiNE workspaces, documents, and databases from MCP-compatible agents

affine-mcp-server gives an MCP-compatible agent a bounded AFFiNE workspace workflow. It can read and update server-backed workspaces, search and edit documents, inspect or fill databases, work with comments, and automate repeatable knowledge-base operations from an agent session instead of making a human click through the AFFiNE app.

The scope is narrow enough to be skill-shaped: this is for agent-side AFFiNE workspace operations through MCP. It is not a generic AFFiNE product card, not a general knowledge-base platform listing, and not a catch-all collaboration suite entry. Invoke it when the missing step is structured workspace access inside an MCP workflow, not when the user simply wants to browse AFFiNE normally or evaluate AFFiNE as a product.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/work-with-affine-workspaces-documents-and-databases-from-mcp-compatible-agents/)
