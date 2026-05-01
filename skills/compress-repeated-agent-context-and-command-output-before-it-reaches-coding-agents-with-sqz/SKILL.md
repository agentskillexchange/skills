---
title: "Compress repeated agent context and command output before it reaches coding agents with sqz"
description: "Reduces token burn by compressing command output and deduplicating repeated file reads before they are sent to Claude Code, Codex, Cursor, and related coding-agent tools."
verification: "security_reviewed"
source: "https://github.com/ojuschugh1/sqz"
author: "Ojus Chugh"
publisher_type: "Open Source Maintainer"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ojuschugh1/sqz"
  github_stars: 165
---

# Compress repeated agent context and command output before it reaches coding agents with sqz

Reduces token burn by compressing command output and deduplicating repeated file reads before they are sent to Claude Code, Codex, Cursor, and related coding-agent tools.

## Prerequisites

sqz CLI plus a supported coding-agent client such as Claude Code, Codex, Cursor, Windsurf, Cline, Gemini CLI, or OpenCode

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install via the project installer script or npm, then run sqz init (optionally with --only or --skip) to add the output-compression hooks to the supported agent clients you use.
```

## Documentation

- https://ojuschugh1.github.io/sqz/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compress-repeated-agent-context-and-command-output-before-it-reaches-coding-agents-with-sqz/)
