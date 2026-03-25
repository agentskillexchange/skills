---
name: "Agent Browser Operator"
description: "Interactive browser skill for logged-in flows, dynamic pages, and session-aware site operations."
category: "Browser Automation"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/agent-browser-operator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "playwright"  # from ase_tool_match
  github_stars: 84938  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "microsoft/playwright"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Agent Browser Operator

Interactive browser skill for logged-in flows, dynamic pages, and session-aware site operations.

## Overview

Agent Browser Operator handles interactive, session-aware browser tasks where simple scraping is not enough. It is built for logged-in flows, dynamic page interactions, form filling, and multi-step site navigation that requires a real browser context.

Best for

logged-in admin workflows (WordPress, dashboards, internal tools)

multi-step form submission and interactive page flows

extracting data from JavaScript-rendered or authentication-gated pages

How it differs from MCP browser tools

Unlike MCP-based browser connectors (Playwright MCP, Browser MCP, Browserbase), Agent Browser Operator works through OpenClaw’s native browser tool with direct session context. It is best for tasks that need the agent’s own authenticated session rather than a standalone browser-as-a-service.

Install notes

Enable the browser tool in OpenClaw. For managed mode, install Chrome or Chromium on the host. For relay mode, use the OpenClaw Browser Relay Chrome extension.

**Source:** OpenClaw browser tool documentation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill agent-browser-operator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill agent-browser-operator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill agent-browser-operator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill agent-browser-operator -a codex
```

### OpenClaw

```bash
clawhub install agent-browser-operator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/agent-browser-operator/
