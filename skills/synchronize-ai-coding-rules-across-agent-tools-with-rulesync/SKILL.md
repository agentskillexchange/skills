---
name: "Synchronize AI coding rules across agent tools with Rulesync"
slug: "synchronize-ai-coding-rules-across-agent-tools-with-rulesync"
description: "Use Rulesync to maintain one set of AI coding rules and generate the right configuration files for Claude Code, Cursor, Gemini CLI, and other development agents."
github_stars: 1217
verification: "security_reviewed"
source: "https://github.com/dyoshikawa/rulesync"
author: "dyoshikawa"
publisher_type: "individual"
category: "Developer Tools"
framework: "Multi-Framework"
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

Use the upstream install or setup path that matches your environment:
- npm install -g rulesync
- brew install rulesync

Requirements and caveats from upstream:
- A Node.js CLI tool that automatically generates configuration files for various AI development tools from unified AI rule files. Features selective generation, comprehensive import/export capabilities, and supports ma...
- The tables below show whether each tool supports a given feature (✅ = supported, blank = not supported). A ✅ means the feature is supported in at least one mode (project, global, or simulated) — for example, Codex CLI...

Basic usage or getting-started notes:
- See [Installation docs](https://dyoshikawa.github.io/rulesync/getting-started/installation) for manual install and platform-specific instructions.
- rulesync init
- rulesync fetch dyoshikawa/rulesync --features skills

- Source: https://github.com/dyoshikawa/rulesync
- Extracted from upstream docs: https://raw.githubusercontent.com/dyoshikawa/rulesync/HEAD/README.md

## Documentation

- https://dyoshikawa.github.io/rulesync/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/synchronize-ai-coding-rules-across-agent-tools-with-rulesync/)
