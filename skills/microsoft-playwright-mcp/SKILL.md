---
title: "Microsoft Playwright MCP"
description: "Microsoft Playwright MCP exposes Playwright browser automation through the Model Context Protocol, giving agents structured page access instead of screenshot-only workflows. It is a strong fit when you want dependable navigation, form filling, DOM inspection, and test-like automation inside an MCP-compatible client."
slug: "microsoft-playwright-mcp"
category:
  - "Browser Automation"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/microsoft/playwright-mcp"
listed: true
---

# Microsoft Playwright MCP

Microsoft Playwright MCP exposes Playwright browser automation through the Model Context Protocol, giving agents structured page access instead of screenshot-only workflows. It is a strong fit when you want dependable navigation, form filling, DOM inspection, and test-like automation inside an MCP-compatible client.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install microsoft-playwright-mcp
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Microsoft Playwright MCP is the official Playwright MCP server from Microsoft. It wraps the Playwright browser automation stack behind the Model Context Protocol so an agent can open pages, inspect structured accessibility snapshots, click elements, fill forms, and move through multi-step web tasks without relying on raw screenshots alone. That makes it useful for coding assistants, support agents, QA helpers, and internal automation workflows where repeatability matters more than visual guesswork.
The upstream project is designed for MCP-capable clients such as VS Code, Cursor, Windsurf, Claude Desktop, Goose, Codex, and other tools that can launch stdio-based MCP servers. The standard setup shown by the maintainer uses npx @playwright/mcp@latest, and the package targets Node.js 18 or newer. Because it is built by the Playwright team, it also plugs naturally into the wider Playwright ecosystem for browser installs, debugging, and consistent cross-browser behavior.
This skill is best used when an agent needs reliable browser automation against modern sites: logging into dashboards, validating flows, collecting data from pages, reproducing UI bugs, or stepping through user journeys in a deterministic way. It maps cleanly to the MCP framework and the Browser Automation category because the core job-to-be-done is browser control through a maintained MCP server with a published npm package, active repository, and current release activity.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-playwright-mcp/)
