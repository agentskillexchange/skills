---
name: "Design loop engineering workflows for coding agents"
slug: "design-loop-engineering-workflows-for-coding-agents"
description: "Use Loop Engineering to scaffold, audit, and operate repeatable coding-agent loops with explicit state, budget, readiness, and tool-specific patterns."
github_stars: 6582
verification: "security_reviewed"
source: "https://github.com/cobusgreyling/loop-engineering"
author: "Cobus Greyling"
publisher_type: "independent"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "cobusgreyling/loop-engineering"
  github_stars: 6582
  npm_package: "@cobusgreyling/loop-audit"
  npm_weekly_downloads: 2696
---

# Design loop engineering workflows for coding agents

Use Loop Engineering to scaffold, audit, and operate repeatable coding-agent loops with explicit state, budget, readiness, and tool-specific patterns.

## Prerequisites

Node.js/npm for loop-init, loop-audit, loop-cost, loop-sync, loop-context, loop-worktree, and optional loop-mcp-server; an installed coding agent such as Claude Code, Codex, OpenCode, Grok, or Cursor.

## Installation

Use the upstream install or setup path that matches your environment:
- npx @cobusgreyling/loop-init .
- npx @cobusgreyling/loop-init . --pattern daily-triage --tool grok
- npx @cobusgreyling/loop-cost --pattern daily-triage --level L1
- npx @cobusgreyling/loop-audit . --suggest

Requirements and caveats from upstream:
- cd tools/loop-init && npm ci && npm test && node dist/cli.js /path/to/project --pattern daily-triage --tool grok
- cd tools/loop-audit && npm ci && npm test && node dist/cli.js /path/to/project --suggest

Basic usage or getting-started notes:
- [Getting Started (5 minutes)](#getting-started-5-minutes)
- | [Pattern Picker](docs/pattern-picker.md) | Which loop to run first — **start here if unsure** |
- | [Starters](starters/) | Clone-and-run kits (Grok, Claude Code, Codex, Opencode) |

- Source: https://github.com/cobusgreyling/loop-engineering
- Extracted from upstream docs: https://raw.githubusercontent.com/cobusgreyling/loop-engineering/HEAD/README.md

## Documentation

- https://cobusgreyling.github.io/loop-engineering/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/design-loop-engineering-workflows-for-coding-agents/)
