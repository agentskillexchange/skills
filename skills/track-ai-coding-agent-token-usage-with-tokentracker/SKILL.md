---
title: "Track AI coding-agent token usage with TokenTracker"
description: "Use TokenTracker to auto-collect local token, cost, and rate-limit telemetry across Claude Code, Codex, Cursor, Gemini, OpenCode, OpenClaw, and other AI coding tools."
verification: "security_reviewed"
source: "https://github.com/mm7894215/TokenTracker"
author: "TokenTracker contributors"
publisher_type: "open_source"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "mm7894215/TokenTracker"
  github_stars: 959
  npm_package: "tokentracker-cli"
  npm_weekly_downloads: 15297
---

# Track AI coding-agent token usage with TokenTracker

Use TokenTracker to auto-collect local token, cost, and rate-limit telemetry across Claude Code, Codex, Cursor, Gemini, OpenCode, OpenClaw, and other AI coding tools.

## Prerequisites

Node.js 20+, tokentracker-cli or native desktop app, local AI coding tools to monitor, optional sqlite3 for Cursor token reading

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run npx tokentracker-cli for first-time setup, or install globally with npm i -g tokentracker-cli and run tokentracker, tokentracker sync, tokentracker status, or tokentracker doctor to collect and inspect local AI-tool usage.
```

## Documentation

- https://www.tokentracker.cc

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/track-ai-coding-agent-token-usage-with-tokentracker/)
