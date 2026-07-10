---
title: "Synchronize AI coding rules across agent tools with Rulesync"
description: "Use Rulesync to maintain one set of AI coding rules and generate the right configuration files for Claude Code, Cursor, Gemini CLI, and other development agents."
verification: "security_reviewed"
source: "https://github.com/dyoshikawa/rulesync"
author: "dyoshikawa"
publisher_type: "individual"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dyoshikawa/rulesync"
  github_stars: 1217
  npm_package: "rulesync"
  npm_weekly_downloads: 748196
---

# Synchronize AI coding rules across agent tools with Rulesync

Use Rulesync to maintain one set of AI coding rules and generate the right configuration files for Claude Code, Cursor, Gemini CLI, and other development agents.

## Prerequisites

Node.js/npm or Homebrew, Rulesync CLI, target AI coding tools

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `npm install -g rulesync` or `brew install rulesync`, run `rulesync init`, optionally fetch official skills with `rulesync fetch dyoshikawa/rulesync --features skills`, then generate target configs with `rulesync generate --targets "*" --features "*"`.
```

## Documentation

- https://dyoshikawa.github.io/rulesync/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/synchronize-ai-coding-rules-across-agent-tools-with-rulesync/)
