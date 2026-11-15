---
name: "Connect MCP clients to JetBrains IDE project tools"
slug: "connect-mcp-clients-to-jetbrains-ide-project-tools"
description: "Use the built-in JetBrains MCP server to let Codex, Claude Desktop, Cursor, VS Code, and other MCP clients inspect and operate an open IntelliJ-based project."
verification: "security_reviewed"
source: "https://www.jetbrains.com/help/idea/mcp-server.html"
author: "JetBrains"
publisher_type: "company"
category: "Developer Tools"
framework: "MCP"
---

# Connect MCP clients to JetBrains IDE project tools

Use the built-in JetBrains MCP server to let Codex, Claude Desktop, Cursor, VS Code, and other MCP clients inspect and operate an open IntelliJ-based project.

## Prerequisites

IntelliJ IDEA or another IntelliJ-based JetBrains IDE version 2025.2 or newer, bundled MCP Server plugin enabled, an MCP-capable client such as Codex, Claude Desktop, Cursor, or VS Code

## Installation

Requirements and caveats from upstream:
- STEP_* and RESUME require a suspended session.
- DRAIN_EVENTS also requires an existing session; do not reuse a stale sessionId after the session has terminated.
- Use exact child names from the current paused xdebug_get_frame_values / previous xdebug_get_value_by_path output because index node names may differ by language/debugger (for example, "[0]" vs "0" ).

Basic usage or getting-started notes:
- The MCP server allows connected external clients to execute terminal commands or run configurations in the IDE without prompting for user confirmation each time.
- In the Command execution section, enable the Run shell commands or run configurations without confirmation (brave mode) setting.
- The MCP Server exposes a set of tools that allow external clients to interact with your IDE and project – for example, to analyze code, modify files, run configurations, or execute terminal commands.

- Source: https://www.jetbrains.com/help/idea/mcp-server.html

## Documentation

- https://www.jetbrains.com/help/idea/mcp-server.html

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/connect-mcp-clients-to-jetbrains-ide-project-tools/)
