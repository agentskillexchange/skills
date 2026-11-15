---
name: "Install focused Claude Code workflow plugins from Claude Night Market"
slug: "install-focused-claude-code-workflow-plugins-from-claude-night-market"
description: "Review and install only the Claude Night Market plugins needed for a specific Claude Code workflow, such as PR prep, code review, TDD gates, or spec-driven development."
github_stars: 291
verification: "security_reviewed"
source: "https://github.com/athola/claude-night-market"
author: "athola"
publisher_type: "open_source_project"
category: "Developer Tools"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "athola/claude-night-market"
  github_stars: 291
---

# Install focused Claude Code workflow plugins from Claude Night Market

Review and install only the Claude Night Market plugins needed for a specific Claude Code workflow, such as PR prep, code review, TDD gates, or spec-driven development.

## Prerequisites

Claude Code 2.1.16 or newer, Python 3.9 or newer for hooks, optional opkg or npx skills installer

## Installation

Use the upstream install or setup path that matches your environment:
- npx skills add athola/claude-night-market (installs all plugins at once).
- make create-plugin NAME=my-plugin
- make validate
- make lint && make test

Requirements and caveats from upstream:
- Requires **Claude Code 2.1.16+** and **Python 3.9+** for hooks.
- A depends on B). Dashed arrows mark optional
- | **parseltongue** | Domain | Python: testing, performance, async patterns, packaging | 4 | 3 |

Basic usage or getting-started notes:
- [Quick Start](#quick-start)
- See [Requirements](#requirements) for details.
- bash

- Source: https://github.com/athola/claude-night-market
- Extracted from upstream docs: https://raw.githubusercontent.com/athola/claude-night-market/HEAD/README.md

## Documentation

- https://athola.github.io/claude-night-market

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/install-focused-claude-code-workflow-plugins-from-claude-night-market/)
