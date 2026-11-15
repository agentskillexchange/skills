---
name: "Vercel Agent Browser"
slug: "vercel-agent-browser"
description: "Vercel Agent Browser is a browser automation CLI built specifically for AI agents. It gives agents a fast, scriptable way to open pages, inspect accessibility snapshots, click elements, fill forms, capture screenshots, and manage browser state from the command line."
github_stars: 29072
verification: "security_reviewed"
source: "https://github.com/vercel-labs/agent-browser"
author: "Vercel Labs"
publisher_type: "Company"
category: "Browser Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "vercel-labs/agent-browser"
  github_stars: 29072
  npm_package: "agent-browser"
  npm_weekly_downloads: 601908
---

# Vercel Agent Browser

Vercel Agent Browser is a browser automation CLI built specifically for AI agents. It gives agents a fast, scriptable way to open pages, inspect accessibility snapshots, click elements, fill forms, capture screenshots, and manage browser state from the command line.

## Prerequisites

Node.js, Chrome or Chrome for Testing

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g agent-browser
- npm install agent-browser
- brew install agent-browser
- cargo install agent-browser

Requirements and caveats from upstream:
- **Options:** --name <name> (filter role by accessible name), --exact (require exact text match)
- By default, alert and beforeunload dialogs are automatically accepted so they never block the agent. confirm and prompt dialogs still require explicit handling. Use --no-auto-dialog (or AGENT_BROWSER_NO_AUTO_DIALOG=1)...

Basic usage or getting-started notes:
- ### Global Installation (recommended)
- Installs the native Rust binary:
- bash

- Source: https://github.com/vercel-labs/agent-browser
- Extracted from upstream docs: https://raw.githubusercontent.com/vercel-labs/agent-browser/HEAD/README.md

## Documentation

- https://agent-browser.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vercel-agent-browser/)
