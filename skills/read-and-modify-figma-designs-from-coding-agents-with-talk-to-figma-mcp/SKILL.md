---
name: "Read and modify Figma designs from coding agents with Talk to Figma MCP"
slug: "read-and-modify-figma-designs-from-coding-agents-with-talk-to-figma-mcp"
description: "Bridge Cursor, Claude Code, and other MCP clients into Figma so agents can inspect selections, create nodes, annotate designs, and apply bulk edits."
github_stars: 6832
verification: "security_reviewed"
source: "https://github.com/grab/cursor-talk-to-figma-mcp"
author: "Grab"
publisher_type: "organization"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "grab/cursor-talk-to-figma-mcp"
  github_stars: 6832
  npm_package: "cursor-talk-to-figma-mcp"
  npm_weekly_downloads: 11128
---

# Read and modify Figma designs from coding agents with Talk to Figma MCP

Bridge Cursor, Claude Code, and other MCP clients into Figma so agents can inspect selections, create nodes, annotate designs, and apply bulk edits.

## Prerequisites

Bun, MCP-compatible client, Figma desktop or web app, Talk to Figma Figma plugin

## Installation

Requirements and caveats from upstream:
- read_my_design - Get detailed node information about the current selection without parameters
- get_node_info - Get detailed information about a specific node
- get_nodes_info - Get detailed information about multiple nodes by providing an array of node IDs

Basic usage or getting-started notes:
- Run setup, this will also install MCP in your Cursor's active project
- Start the WebSocket server
- Install the MCP server in Cursor

- Source: https://github.com/grab/cursor-talk-to-figma-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/grab/cursor-talk-to-figma-mcp/HEAD/README.md

## Documentation

- https://www.figma.com/community/plugin/1485687494525374295/cursor-talk-to-figma-mcp-plugin

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/read-and-modify-figma-designs-from-coding-agents-with-talk-to-figma-mcp/)
