---
title: "Build, test, and inspect Apple apps through MCP with XcodeBuildMCP"
description: "Connect coding agents to Xcode build, test, simulator, and project-inspection tools through XcodeBuildMCP’s MCP server or CLI."
verification: "security_reviewed"
source: "https://github.com/getsentry/XcodeBuildMCP"
author: "Sentry"
publisher_type: "organization"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "getsentry/XcodeBuildMCP"
  github_stars: 5719
  npm_package: "xcodebuildmcp"
  npm_weekly_downloads: 44479
---

# Build, test, and inspect Apple apps through MCP with XcodeBuildMCP

Connect coding agents to Xcode build, test, simulator, and project-inspection tools through XcodeBuildMCP’s MCP server or CLI.

## Prerequisites

Xcode 16 or later, Node.js 18 or later for npm install, MCP-compatible client

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with Homebrew using `brew tap getsentry/xcodebuildmcp && brew install xcodebuildmcp`, or with npm using `npm install -g xcodebuildmcp@latest`. Verify with `xcodebuildmcp --help`, then connect the MCP server to your client or run `xcodebuildmcp init` to install the optional agent skills.
```

## Documentation

- https://www.xcodebuildmcp.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-test-and-inspect-apple-apps-through-mcp-with-xcodebuildmcp/)
