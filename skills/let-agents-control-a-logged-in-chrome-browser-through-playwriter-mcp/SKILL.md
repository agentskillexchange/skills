---
name: "Let agents control a logged-in Chrome browser through Playwriter MCP"
slug: "let-agents-control-a-logged-in-chrome-browser-through-playwriter-mcp"
description: "Use Playwriter to give MCP-compatible agents a bounded, stateful Playwright control surface over an operator-approved Chrome session."
github_stars: 3507
verification: "security_reviewed"
source: "https://github.com/remorses/playwriter"
author: "remorses"
publisher_type: "open_source"
category: "Browser Automation"
framework: "MCP"
tool_ecosystem:
  github_repo: "remorses/playwriter"
  github_stars: 3507
  npm_package: "playwriter"
  npm_weekly_downloads: 8482
---

# Let agents control a logged-in Chrome browser through Playwriter MCP

Use Playwriter to give MCP-compatible agents a bounded, stateful Playwright control surface over an operator-approved Chrome session.

## Prerequisites

Playwriter Chrome extension and CLI; MCP-compatible client when using MCP mode; Chrome/Chromium browser session

## Installation

Use the upstream install or setup path that matches your environment:
- npm i -g playwriter
- npx -y skills add remorses/playwriter
- npx -y traforo -p 19988 -t my-machine -- npx -y playwriter serve --token <secret>
- npx -y playwriter serve --host 127.0.0.1

Requirements and caveats from upstream:
- Variables in scope: page, context, state (persists between calls), require, and Node.js globals.

Basic usage or getting-started notes:
- [**Install Extension**](https://chromewebstore.google.com/detail/playwriter-mcp/jfeammnjpkecdekppnclgkkffahnhfhe) from Chrome Web Store
- Click extension icon on a tab → turns green when connected
- Install the CLI and start automating the browser:

- Source: https://github.com/remorses/playwriter
- Extracted from upstream docs: https://raw.githubusercontent.com/remorses/playwriter/HEAD/README.md

## Documentation

- https://playwriter.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/let-agents-control-a-logged-in-chrome-browser-through-playwriter-mcp/)
