---
name: "Lint and autofix agent config files before broken prompts, hooks, or MCP settings derail runs with agnix"
slug: "lint-and-autofix-agent-config-files-before-broken-prompts-hooks-or-mcp-settings-derail-runs-with-agnix"
description: "Validate and optionally autofix SKILL.md, CLAUDE.md, AGENTS.md, hooks, and MCP config files before bad agent metadata or wiring silently breaks a workflow."
github_stars: 179
verification: "security_reviewed"
source: "https://github.com/agent-sh/agnix"
author: "agent-sh"
publisher_type: "open_source"
category: "Security & Verification"
framework: "Multi-Framework"
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

Use the upstream install or setup path that matches your environment:
- $ npx agnix .
- npm install -g agnix
- brew tap agent-sh/agnix && brew install agnix
- cargo install agnix-cli

Requirements and caveats from upstream:
- | **Neovim** | { "agent-sh/agnix", config = function() require("agnix").setup() end } |

Basic usage or getting-started notes:
- console
- Validating: .
- CLAUDE.md:15:1 warning: Generic instruction 'Be helpful and accurate' [fixable]

- Source: https://github.com/agent-sh/agnix
- Extracted from upstream docs: https://raw.githubusercontent.com/agent-sh/agnix/HEAD/README.md

## Documentation

- https://github.com/agent-sh/agnix

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-and-autofix-agent-config-files-before-broken-prompts-hooks-or-mcp-settings-derail-runs-with-agnix/)
