---
name: "Debug Firefox-only browser issues with DevTools MCP before shipping web changes"
slug: "debug-firefox-only-browser-issues-with-devtools-mcp-before-shipping-web-changes"
description: "Use Firefox DevTools MCP when an agent needs to inspect pages, trace network and console activity, capture screenshots, and automate reproduction steps in Firefox instead of relying on Chrome-first tooling."
github_stars: 107
verification: "security_reviewed"
source: "https://github.com/mozilla/firefox-devtools-mcp"
author: "Mozilla"
publisher_type: "company"
category: "Browser Automation"
framework: "MCP"
tool_ecosystem:
  github_repo: "mozilla/firefox-devtools-mcp"
  github_stars: 107
  npm_package: "firefox-devtools-mcp"
  npm_weekly_downloads: 2962
---

# Debug Firefox-only browser issues with DevTools MCP before shipping web changes

Use Firefox DevTools MCP when an agent needs to inspect pages, trace network and console activity, capture screenshots, and automate reproduction steps in Firefox instead of relying on Chrome-first tooling.

## Prerequisites

Node.js 20.19+; a local Firefox 100+ installation; an MCP-compatible client such as Claude Code, Claude Desktop, Cursor, or Cline.

## Installation

Use the upstream install or setup path that matches your environment:
- **Note**: This MCP server requires a local Firefox browser installation and cannot run on cloud hosting services like glama.ai. Use npx firefox-devtools-mcp@latest to run locally, or use Docker with the provided Docke...
- Recommended: use npx so you always run the latest published version from npm.
- npm run setup
- npx @modelcontextprotocol/inspector npx firefox-devtools-mcp@latest --start-url https://example.com --headless

Requirements and caveats from upstream:
- Node.js ≥ 20.19.0
- --enable-privileged-context — enable privileged context tools: list/select privileged contexts, evaluate privileged scripts, get/set Firefox prefs, and list extensions. Requires MOZ_REMOTE_ALLOW_SYSTEM_ACCESS=1 (ENABL...

Basic usage or getting-started notes:
- **Use a dedicated Firefox profile.** Never run the server against your regular profile — the agent has access to whatever the browser can reach, including cookies and saved sessions.
- Firefox 100+ installed (auto‑detected, or pass --firefox-path)
- Option A — Claude Code CLI

- Source: https://github.com/mozilla/firefox-devtools-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/mozilla/firefox-devtools-mcp/HEAD/README.md

## Documentation

- https://github.com/mozilla/firefox-devtools-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/debug-firefox-only-browser-issues-with-devtools-mcp-before-shipping-web-changes/)
