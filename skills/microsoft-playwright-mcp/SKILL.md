---
name: "Microsoft Playwright MCP"
slug: "microsoft-playwright-mcp"
description: "Microsoft Playwright MCP exposes Playwright browser automation through the Model Context Protocol, giving agents structured page access instead of screenshot-only workflows. It is a strong fit when you want dependable navigation, form filling, DOM inspection, and test-like automation inside an MCP-compatible client."
github_stars: 30794
verification: "security_reviewed"
source: "https://github.com/microsoft/playwright-mcp"
author: "microsoft"
category: "Browser Automation"
framework: "MCP"
tool_ecosystem:
  github_repo: "microsoft/playwright-mcp"
  github_stars: 30794
  npm_package: "@playwright/mcp"
  npm_weekly_downloads: 2762324
---

# Microsoft Playwright MCP

Microsoft Playwright MCP exposes Playwright browser automation through the Model Context Protocol, giving agents structured page access instead of screenshot-only workflows. It is a strong fit when you want dependable navigation, form filling, DOM inspection, and test-like automation inside an MCP-compatible client.

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

- https://www.npmjs.com/package/@playwright/mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-playwright-mcp/)
