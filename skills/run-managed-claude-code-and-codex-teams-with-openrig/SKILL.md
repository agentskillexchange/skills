---
name: "Run managed Claude Code and Codex teams with OpenRig"
slug: "run-managed-claude-code-and-codex-teams-with-openrig"
description: "Use OpenRig when an operator wants persistent tmux-backed Claude Code and Codex seats, YAML-defined team topology, shared TUI visibility, queue handoffs, recovery, and agent-to-agent coordination from one local control plane."
github_stars: 1357
verification: "security_reviewed"
source: "https://github.com/mvschwarz/openrig"
author: "mvschwarz"
publisher_type: "open_source"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "mvschwarz/openrig"
  github_stars: 1357
  npm_package: "@openrig/cli"
  npm_weekly_downloads: 2494
---

# Run managed Claude Code and Codex teams with OpenRig

Use OpenRig when an operator wants persistent tmux-backed Claude Code and Codex seats, YAML-defined team topology, shared TUI visibility, queue handoffs, recovery, and agent-to-agent coordination from one local control plane.

## Prerequisites

OpenRig CLI, Node.js 20/22/24, tmux, macOS or Linux, authenticated Codex and optional Claude Code or supported terminal harnesses

## Installation

Install or set up from the source-backed instructions:

Install with npm install -g @openrig/cli. Review rig setup --dry-run before applying setup, confirm tmux and authenticated agent CLIs are available, then run rig up first-project --cwd . --plan, rig up first-project --cwd ., and rig tui --shared from the target repository.

- Source: https://github.com/mvschwarz/openrig

## Documentation

- https://openrig.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-managed-claude-code-and-codex-teams-with-openrig/)
