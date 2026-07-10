---
title: "Control Unity Editor scenes and assets through MCP for Unity"
description: "Connect MCP-compatible agents to Unity Editor so they can inspect scenes, manage assets, edit scripts, run tests, and automate game-development tasks."
verification: "security_reviewed"
source: "https://github.com/CoplayDev/unity-mcp"
author: "CoplayDev"
publisher_type: "organization"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "CoplayDev/unity-mcp"
  github_stars: 10623
---

# Control Unity Editor scenes and assets through MCP for Unity

Connect MCP-compatible agents to Unity Editor so they can inspect scenes, manage assets, edit scripts, run tests, and automate game-development tasks.

## Prerequisites

Unity Editor, Python 3.10+, MCP-compatible client such as Claude, Codex, VS Code, or Cursor

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
In Unity Package Manager, choose `Add package from git URL` and add `https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main`, then run `Window -> MCP for Unity -> Configure All Detected Clients` before prompting the connected MCP client.
```

## Documentation

- https://coplaydev.github.io/unity-mcp/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/control-unity-editor-scenes-and-assets-through-mcp-for-unity/)
