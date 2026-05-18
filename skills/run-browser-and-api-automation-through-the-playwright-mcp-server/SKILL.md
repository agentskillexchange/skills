---
name: "Run browser and API automation through the Playwright MCP server"
slug: "run-browser-and-api-automation-through-the-playwright-mcp-server"
description: "Expose Playwright browser and API automation commands to MCP-capable agents for supervised test workflows."
github_stars: 5489
verification: "security_reviewed"
source: "https://github.com/executeautomation/mcp-playwright"
author: "executeautomation"
publisher_type: "organization"
category: "Browser Automation"
framework: "MCP"
tool_ecosystem:
  github_repo: "executeautomation/mcp-playwright"
  github_stars: 5489
  npm_package: "@executeautomation/playwright-mcp-server"
  npm_weekly_downloads: 0
---

# Run browser and API automation through the Playwright MCP server

Expose Playwright browser and API automation commands to MCP-capable agents for supervised test workflows.

## Prerequisites

Node.js, Playwright browsers, an MCP-capable client such as Claude Desktop, Cursor, Cline, or compatible agent runtime

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g @executeautomation/playwright-mcp-server
- npx @michaellatman/mcp-get@latest install @executeautomation/playwright-mcp-server
- npx @smithery/cli install @executeautomation/playwright-mcp-server --client claude
- npx playwright install

Requirements and caveats from upstream:
- **Note for Claude Desktop Users:** Claude Desktop currently requires stdio mode (command/args configuration). HTTP mode is recommended for VS Code, custom clients, and remote deployments. See [CLAUDE_DESKTOP_CONFIG.md...
- node run-tests.cjs

Basic usage or getting-started notes:
- You can install the package using either npm, mcp-get, or Smithery:
- Using npm:
- bash

- Source: https://github.com/executeautomation/mcp-playwright
- Extracted from upstream docs: https://raw.githubusercontent.com/executeautomation/mcp-playwright/HEAD/README.md

## Documentation

- https://github.com/executeautomation/mcp-playwright

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-browser-and-api-automation-through-the-playwright-mcp-server/)
