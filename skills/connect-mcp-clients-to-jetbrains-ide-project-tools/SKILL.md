---
title: "Connect MCP clients to JetBrains IDE project tools"
description: "Use the built-in JetBrains MCP server to let Codex, Claude Desktop, Cursor, VS Code, and other MCP clients inspect and operate an open IntelliJ-based project."
verification: "security_reviewed"
source: "https://www.jetbrains.com/help/idea/mcp-server.html"
author: "JetBrains"
publisher_type: "company"
category:
  - "Developer Tools"
framework:
  - "MCP"
---

# Connect MCP clients to JetBrains IDE project tools

Use the built-in JetBrains MCP server to let Codex, Claude Desktop, Cursor, VS Code, and other MCP clients inspect and operate an open IntelliJ-based project.

## Prerequisites

IntelliJ IDEA or another IntelliJ-based JetBrains IDE version 2025.2 or newer, bundled MCP Server plugin enabled, an MCP-capable client such as Codex, Claude Desktop, Cursor, or VS Code

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Use IntelliJ IDEA 2025.2 or newer. Open Settings, go to Plugins, confirm the bundled MCP Server plugin is enabled, then follow JetBrains' External client setup instructions for your MCP client. Use the @jetbrains/mcp-proxy package only when the documented client setup requires an STDIO proxy path.
```

## Documentation

- https://www.jetbrains.com/help/idea/mcp-server.html

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/connect-mcp-clients-to-jetbrains-ide-project-tools/)
