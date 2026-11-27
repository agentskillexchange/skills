---
name: "Inspect a paused Windows executable with x64dbg MCP"
slug: "inspect-paused-windows-executable-with-x64dbg-mcp"
description: "Load an authorized Windows executable, pause at a breakpoint, and collect registers, memory, disassembly, and call-stack evidence through x64dbg MCP."
github_stars: 2819
verification: "security_reviewed"
source: "https://github.com/duty1g/x64dbg-mcp-server"
author: "duty1g"
publisher_type: "community"
category: "Runbooks & Diagnostics"
framework: "MCP"
tool_ecosystem:
  github_repo: "duty1g/x64dbg-mcp-server"
  github_stars: 2819
---

# Inspect a paused Windows executable with x64dbg MCP

Load an authorized Windows executable, pause at a breakpoint, and collect registers, memory, disassembly, and call-stack evidence through x64dbg MCP.

## Prerequisites

Windows, x64dbg/x32dbg, upstream native MCP plugin, HTTP MCP client with bearer-header support

## Installation

Install or set up from the source-backed instructions:

Download x64dbg-MCP-Server-v1.7.zip from https://github.com/duty1g/x64dbg-mcp-server/releases/tag/v1.7, extract it, and copy dist/ contents into the x64dbg root. Launch the matching debugger, set the desired bind address in Plugins > x64dbg-MCP Server > Configure MCP Server, and configure the MCP URL plus generated bearer token.

- Source: https://github.com/duty1g/x64dbg-mcp-server

## Documentation

- https://github.com/duty1g/x64dbg-mcp-server/blob/e26dc6a639b39b6c8e1e9551ef9a75d59b0e248a/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-paused-windows-executable-with-x64dbg-mcp/)
