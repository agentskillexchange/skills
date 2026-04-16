---
title: "Chrome MCP Server Extension-Based Browser Automation for AI Agents"
description: "Chrome MCP Server uses a Chrome extension and local bridge to expose your everyday browser to MCP-compatible agents. It is designed for workflows where an agent should reuse real tabs, existing login state, browser history, bookmarks, and native Chrome APIs instead of launching a separate automation browser."
verification: "security_reviewed"
source: "https://github.com/hangwin/mcp-chrome"
category:
  - "Browser Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hangwin/mcp-chrome"
  github_stars: 11177
---

# Chrome MCP Server Extension-Based Browser Automation for AI Agents

Chrome MCP Server, published from the hangwin/mcp-chrome project, is a browser automation server built around a Chrome extension rather than a separate Playwright-managed browser instance. Its core job-to-be-done is to let an AI assistant operate inside the user’s real Chrome environment, with the tabs, sessions, cookies, bookmarks, and login state already in place. That makes it useful for agents that need to work with authenticated tools, existing browsing context, or cross-tab tasks without rebuilding state from scratch.


The upstream README highlights a broad toolset: browser and tab management, screenshots, network monitoring, content extraction, console capture, form filling, keyboard control, history search, and bookmark operations. It also adds semantic search across tab content through a built-in vector database, which makes the project more than a simple click automation bridge. In practice, that means an agent can search across open tabs, inspect network behavior, read page content, and continue interacting with the same browser session.


Integration requires Node.js and Chrome, plus the project’s bridge package and extension. The documented install path is npm install -g mcp-chrome-bridge, followed by loading the extension and connecting an MCP client over streamable HTTP or stdio. This architecture is a strong fit for Browser Automation skills that prioritize user-session reuse, local control, and wide Chrome-native coverage over isolated headless-browser reproducibility.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chrome-mcp-server-extension-based-browser-automation-ai-agents/)
