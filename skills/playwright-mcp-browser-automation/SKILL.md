---
name: "Playwright MCP Browser Automation"
slug: "playwright-mcp-browser-automation"
description: "Official Playwright-powered browser control for agent workflows."
github_stars: 32694
verification: "security_reviewed"
source: "https://github.com/microsoft/playwright-mcp"
author: "Microsoft"
publisher_type: "company"
category: "Browser Automation"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "microsoft/playwright-mcp"
  github_stars: 32694
  npm_package: "@playwright/mcp"
  npm_weekly_downloads: 2184986
---

# Playwright MCP Browser Automation

Official Playwright-powered browser control for agent workflows.

## Prerequisites

Node.js, Playwright, MCP client or host environment

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-mcp-browser-automation/)
