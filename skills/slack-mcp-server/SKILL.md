---
name: "Slack MCP Server"
description: "Agent access to Slack conversations and workspace workflows."
category: "Calendar, Email & Productivity"
framework: "Claude Code"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/slack-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "slack"  # from ase_tool_match
  github_stars: 2900  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2433529  # from ase_npm_downloads
  github_repo: "slackapi/bolt-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Slack MCP Server

Agent access to Slack conversations and workspace workflows.

## Overview

Connects Slack data and messaging workflows to agents for search, retrieval, and communication tasks inside team environments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill slack-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill slack-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill slack-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill slack-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install slack-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/slack-mcp-server/
