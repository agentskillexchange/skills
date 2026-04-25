---
title: "Work with AFFiNE workspaces, documents, and databases from MCP-compatible agents"
description: "Use affine-mcp-server when an agent needs tool-callable access to AFFiNE workspaces, documents, databases, and comments inside an MCP workflow instead of sending a user back to the AFFiNE UI."
verification: "security_reviewed"
source: "https://github.com/DAWNCR0W/affine-mcp-server"
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

affine-mcp-server gives an MCP-compatible agent a bounded AFFiNE workspace workflow. It can read and update server-backed workspaces, search and edit documents, inspect or fill databases, work with comments, and automate repeatable knowledge-base operations from an agent session instead of making a human click through the AFFiNE app. The scope is narrow enough to be skill-shaped: this is for agent-side AFFiNE workspace operations through MCP. It is not a generic AFFiNE product card, not a general knowledge-base platform listing, and not a catch-all collaboration suite entry. Invoke it when the missing step is structured workspace access inside an MCP workflow, not when the user simply wants to browse AFFiNE normally or evaluate AFFiNE as a product.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/work-with-affine-workspaces-documents-and-databases-from-mcp-compatible-agents/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/work-with-affine-workspaces-documents-and-databases-from-mcp-compatible-agents
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/work-with-affine-workspaces-documents-and-databases-from-mcp-compatible-agents`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/work-with-affine-workspaces-documents-and-databases-from-mcp-compatible-agents/)
