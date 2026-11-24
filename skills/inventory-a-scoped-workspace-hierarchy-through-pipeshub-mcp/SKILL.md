---
name: "Inspect a scoped workspace hierarchy through PipesHub MCP"
slug: "inventory-a-scoped-workspace-hierarchy-through-pipeshub-mcp"
description: "Paginate a named folder, space, or epic into a source-linked record inventory, preserving scope and reporting indexing, access, and pagination limits."
github_stars: 4149
verification: "security_reviewed"
source: "https://github.com/pipeshub-ai/pipeshub-ai"
author: "PipesHub"
publisher_type: "organization"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "pipeshub-ai/pipeshub-ai"
  github_stars: 4149
  npm_package: "@pipeshub-ai/mcp"
  npm_weekly_downloads: 4829
---

# Inspect a scoped workspace hierarchy through PipesHub MCP

Paginate a named folder, space, or epic into a source-linked record inventory, preserving scope and reporting indexing, access, and pagination limits.

## Prerequisites

Existing indexed PipesHub instance; user-authenticated Streamable HTTP MCP client; pipeshub_sources and pipeshub_get_record_content

## Installation

Install or set up from the source-backed instructions:

Use an existing configured and indexed PipesHub instance. Connect its /mcp endpoint with user-bound authentication using the official MCP client setup guide at https://github.com/pipeshub-ai/mcp-server/blob/21d551f003c2e61850fd7c3452310d8d953df026/README.md. Keep credentials in the client secret facility or supported environment interpolation. Remote HTTP requires no local npm bridge. The optional upstream instruction package installs with npx skills add pipeshub-ai/mcp-server; review it before installation. Confirm the connection with pipeshub_sources and verify navigate mode is available. This intake did not install or authenticate anything.

- Source: https://github.com/pipeshub-ai/pipeshub-ai

## Documentation

- https://github.com/pipeshub-ai/mcp-server/blob/21d551f003c2e61850fd7c3452310d8d953df026/skills/pipeshub/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inventory-a-scoped-workspace-hierarchy-through-pipeshub-mcp/)
