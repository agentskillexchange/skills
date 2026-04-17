---
title: "Microsoft Playwright MCP"
description: "Microsoft Playwright MCP is the official Playwright MCP server from Microsoft. It wraps the Playwright browser automation stack behind the Model Context Protocol so an agent can open pages, inspect structured accessibility snapshots, click elements, fill forms, and move through multi-step web tasks without relying on raw screenshots alone. That makes it useful for coding assistants, support agents, QA helpers, and internal automation workflows where repeatability matters more than visual guesswork.\nThe upstream project is designed for MCP-capable clients such as VS Code, Cursor, Windsurf, Claude Desktop, Goose, Codex, and other tools that can launch stdio-based MCP servers. The standard setup shown by the maintainer uses npx @playwright/mcp@latest, and the package targets Node.js 18 or newer. Because it is built by the Playwright team, it also plugs naturally into the wider Playwright ecosystem for browser installs, debugging, and consistent cross-browser behavior.\nThis skill is best used when an agent needs reliable browser automation against modern sites: logging into dashboards, validating flows, collecting data from pages, reproducing UI bugs, or stepping through user journeys in a deterministic way. It maps cleanly to the MCP framework and the Browser Automation category because the core job-to-be-done is browser control through a maintained MCP server with a published npm package, active repository, and current release activity."
verification: security_reviewed
source: "https://github.com/microsoft/playwright-mcp"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "microsoft/playwright-mcp"
  github_stars: 30794
  ase_npm_package: "@playwright/mcp"
  npm_weekly_downloads: 2762324
---

# Microsoft Playwright MCP

Microsoft Playwright MCP is the official Playwright MCP server from Microsoft. It wraps the Playwright browser automation stack behind the Model Context Protocol so an agent can open pages, inspect structured accessibility snapshots, click elements, fill forms, and move through multi-step web tasks without relying on raw screenshots alone. That makes it useful for coding assistants, support agents, QA helpers, and internal automation workflows where repeatability matters more than visual guesswork.
The upstream project is designed for MCP-capable clients such as VS Code, Cursor, Windsurf, Claude Desktop, Goose, Codex, and other tools that can launch stdio-based MCP servers. The standard setup shown by the maintainer uses npx @playwright/mcp@latest, and the package targets Node.js 18 or newer. Because it is built by the Playwright team, it also plugs naturally into the wider Playwright ecosystem for browser installs, debugging, and consistent cross-browser behavior.
This skill is best used when an agent needs reliable browser automation against modern sites: logging into dashboards, validating flows, collecting data from pages, reproducing UI bugs, or stepping through user journeys in a deterministic way. It maps cleanly to the MCP framework and the Browser Automation category because the core job-to-be-done is browser control through a maintained MCP server with a published npm package, active repository, and current release activity.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/microsoft-playwright-mcp
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/microsoft-playwright-mcp` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-playwright-mcp/)
