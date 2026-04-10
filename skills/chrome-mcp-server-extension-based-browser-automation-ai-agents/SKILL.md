---
title: "Chrome MCP Server Extension-Based Browser Automation for AI Agents"
description: "Chrome MCP Server uses a Chrome extension and local bridge to expose your everyday browser to MCP-compatible agents. It is designed for workflows where an agent should reuse real tabs, existing login state, browser history, bookmarks, and native Chrome APIs instead of launching a separate automation browser."
slug: "chrome-mcp-server-extension-based-browser-automation-ai-agents"
category:
  - "Browser Automation"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/hangwin/mcp-chrome"
tool_ecosystem:
  github_repo: "hangwin/mcp-chrome"
  github_stars: 11157
listed: true
---

# Chrome MCP Server Extension-Based Browser Automation for AI Agents

Chrome MCP Server uses a Chrome extension and local bridge to expose your everyday browser to MCP-compatible agents. It is designed for workflows where an agent should reuse real tabs, existing login state, browser history, bookmarks, and native Chrome APIs instead of launching a separate automation browser.

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
clawhub install chrome-mcp-server-extension-based-browser-automation-ai-agents
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Chrome MCP Server, published from the hangwin/mcp-chrome project, is a browser automation server built around a Chrome extension rather than a separate Playwright-managed browser instance. Its core job-to-be-done is to let an AI assistant operate inside the user’s real Chrome environment, with the tabs, sessions, cookies, bookmarks, and login state already in place. That makes it useful for agents that need to work with authenticated tools, existing browsing context, or cross-tab tasks without rebuilding state from scratch.
The upstream README highlights a broad toolset: browser and tab management, screenshots, network monitoring, content extraction, console capture, form filling, keyboard control, history search, and bookmark operations. It also adds semantic search across tab content through a built-in vector database, which makes the project more than a simple click automation bridge. In practice, that means an agent can search across open tabs, inspect network behavior, read page content, and continue interacting with the same browser session.
Integration requires Node.js and Chrome, plus the project’s bridge package and extension. The documented install path is npm install -g mcp-chrome-bridge, followed by loading the extension and connecting an MCP client over streamable HTTP or stdio. This architecture is a strong fit for Browser Automation skills that prioritize user-session reuse, local control, and wide Chrome-native coverage over isolated headless-browser reproducibility.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chrome-mcp-server-extension-based-browser-automation-ai-agents/)
