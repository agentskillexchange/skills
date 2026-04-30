---
title: "Lint and autofix agent config files before broken prompts, hooks, or MCP settings derail runs with agnix"
description: "Validate and optionally autofix SKILL.md, CLAUDE.md, AGENTS.md, hooks, and MCP config files before bad agent metadata or wiring silently breaks a workflow."
verification: "security_reviewed"
source: "https://github.com/agent-sh/agnix"
author: "agent-sh"
publisher_type: "open_source"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "agent-sh/agnix"
  github_stars: 179
  npm_package: "agnix"
  npm_weekly_downloads: 6006
---

# Lint and autofix agent config files before broken prompts, hooks, or MCP settings derail runs with agnix

Validate and optionally autofix SKILL.md, CLAUDE.md, AGENTS.md, hooks, and MCP config files before bad agent metadata or wiring silently breaks a workflow.

## Prerequisites

agnix CLI

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
npm install -g agnix
# or
brew tap agent-sh/agnix && brew install agnix
# or
cargo install agnix-cli
```

## Documentation

- https://github.com/agent-sh/agnix

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-and-autofix-agent-config-files-before-broken-prompts-hooks-or-mcp-settings-derail-runs-with-agnix/)
