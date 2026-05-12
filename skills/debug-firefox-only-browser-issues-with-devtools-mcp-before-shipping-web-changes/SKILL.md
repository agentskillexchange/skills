---
title: "Debug Firefox-only browser issues with DevTools MCP before shipping web changes"
slug: "debug-firefox-only-browser-issues-with-devtools-mcp-before-shipping-web-changes"
description: "Use Firefox DevTools MCP when an agent needs to inspect pages, trace network and console activity, capture screenshots, and automate reproduction steps in Firefox instead of relying on Chrome-first tooling."
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
<p>Use <code>npx firefox-devtools-mcp@latest</code> for the recommended install path, or add it directly to your MCP client config. For Claude Code, run <code>claude mcp add firefox-devtools npx firefox-devtools-mcp@latest</code>. Optional flags like <code>--headless</code>, <code>--viewport</code>, <code>--start-url</code>, and <code>--connect-existing</code> let you tune the Firefox session for debugging or attach to a real browser profile.</p>
```

## Documentation

- https://github.com/mozilla/firefox-devtools-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/debug-firefox-only-browser-issues-with-devtools-mcp-before-shipping-web-changes/)
