---
name: "Playwright MCP Server for Browser Automation"
slug: "playwright-mcp-server-browser-automation"
description: "The official Microsoft Playwright MCP server provides browser automation capabilities through the Model Context Protocol, enabling LLMs to interact with web pages via structured accessibility snapshots without requiring vision models or screenshots."
github_stars: 30110
verification: "security_reviewed"
source: "https://github.com/microsoft/playwright-mcp"
author: "Microsoft"
category: "Browser Automation"
framework: "MCP"
tool_ecosystem:
  github_repo: "microsoft/playwright-mcp"
  github_stars: 30110
  npm_package: "@playwright/mcp"
  npm_weekly_downloads: 2424399
---

# Playwright MCP Server for Browser Automation

The official Microsoft Playwright MCP server provides browser automation capabilities through the Model Context Protocol, enabling LLMs to interact with web pages via structured accessibility snapshots without requiring vision models or screenshots.

## Installation

Use the upstream install or setup path that matches your environment:
- npx @playwright/mcp@latest --config path/to/config.json
- npx @playwright/mcp@latest --port 8931
- docker run -d -i --rm --init --pull=always \
- docker build -t mcr.microsoft.com/playwright/mcp .

Requirements and caveats from upstream:
- Node.js 18 or newer
- node utils/generate-links.js
- | --extension | Connect to a running browser instance (Edge/Chrome only). Requires the "Playwright Extension" to be installed.<br>*env* PLAYWRIGHT_MCP_EXTENSION |

Basic usage or getting-started notes:
- VS Code, Cursor, Windsurf, Claude Desktop, Goose, Junie or any other MCP client
- <!--
- // Generate using:

- Source: https://github.com/microsoft/playwright-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/microsoft/playwright-mcp/HEAD/README.md

## Documentation

- https://github.com/microsoft/playwright-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-mcp-server-browser-automation/)
