---
title: "Install focused Claude Code workflow plugins from Claude Night Market"
description: "Review and install only the Claude Night Market plugins needed for a specific Claude Code workflow, such as PR prep, code review, TDD gates, or spec-driven development."
verification: "security_reviewed"
source: "https://github.com/athola/claude-night-market"
author: "athola"
publisher_type: "open_source_project"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "athola/claude-night-market"
  github_stars: 291
---

# Install focused Claude Code workflow plugins from Claude Night Market

Review and install only the Claude Night Market plugins needed for a specific Claude Code workflow, such as PR prep, code review, TDD gates, or spec-driven development.

## Prerequisites

Claude Code 2.1.16 or newer, Python 3.9 or newer for hooks, optional opkg or npx skills installer

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
In Claude Code, run /plugin marketplace add athola/claude-night-market, then install only the needed plugins, for example /plugin install sanctum@claude-night-market, /plugin install pensive@claude-night-market, or /plugin install spec-kit@claude-night-market. Alternative full install: npx skills add athola/claude-night-market.
```

## Documentation

- https://athola.github.io/claude-night-market

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/install-focused-claude-code-workflow-plugins-from-claude-night-market/)
