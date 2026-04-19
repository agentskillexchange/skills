---
title: "Microsoft Playwright MCP"
description: "Microsoft Playwright MCP is the official Playwright MCP server from Microsoft. It wraps the Playwright browser automation stack behind the Model Context Protocol so an agent can open pages, inspect structured accessibility snapshots, click elements, fill forms, and move through multi-step web tasks without relying on raw screenshots alone. That makes it useful for coding assistants, support agents, QA helpers, and internal automation workflows where repeatability matters more than visual guesswork. The upstream project is designed for MCP-capable clients such as VS Code, Cursor, Windsurf, Claude Desktop, Goose, Codex, and other tools that can launch stdio-based MCP servers. The standard setup shown by the maintainer uses npx @playwright/mcp@latest , and the package targets Node.js 18 or newer. Because it is built by the Playwright team, it also plugs naturally into the wider Playwright ecosystem for browser installs, debugging, and consistent cross-browser behavior. This skill is best used when an agent needs reliable browser automation against modern sites: logging into dashboards, validating flows, collecting data from pages, reproducing UI bugs, or stepping through user journeys in a deterministic way. It maps cleanly to the MCP framework and the Browser Automation category because the core job-to-be-done is browser control through a maintained MCP server with a published npm package, active repository, and current release activity."
source: "https://github.com/microsoft/playwright-mcp"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "microsoft/playwright-mcp"
  github_stars: 30794
  npm_package: "@playwright/mcp"
  npm_weekly_downloads: 2762324
---

# Microsoft Playwright MCP

Microsoft Playwright MCP is the official Playwright MCP server from Microsoft. It wraps the Playwright browser automation stack behind the Model Context Protocol so an agent can open pages, inspect structured accessibility snapshots, click elements, fill forms, and move through multi-step web tasks without relying on raw screenshots alone. That makes it useful for coding assistants, support agents, QA helpers, and internal automation workflows where repeatability matters more than visual guesswork. The upstream project is designed for MCP-capable clients such as VS Code, Cursor, Windsurf, Claude Desktop, Goose, Codex, and other tools that can launch stdio-based MCP servers. The standard setup shown by the maintainer uses npx @playwright/mcp@latest , and the package targets Node.js 18 or newer. Because it is built by the Playwright team, it also plugs naturally into the wider Playwright ecosystem for browser installs, debugging, and consistent cross-browser behavior. This skill is best used when an agent needs reliable browser automation against modern sites: logging into dashboards, validating flows, collecting data from pages, reproducing UI bugs, or stepping through user journeys in a deterministic way. It maps cleanly to the MCP framework and the Browser Automation category because the core job-to-be-done is browser control through a maintained MCP server with a published npm package, active repository, and current release activity.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-playwright-mcp/)
