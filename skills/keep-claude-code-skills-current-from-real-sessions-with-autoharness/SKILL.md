---
name: "Keep Claude Code skills current from real sessions with Autoharness"
slug: "keep-claude-code-skills-current-from-real-sessions-with-autoharness"
description: "Install Autoharness so Claude Code can distill, merge, update, and retire native skills from real operator sessions without a daemon or benchmark loop."
github_stars: 1400
verification: "security_reviewed"
source: "https://github.com/tigerless-labs/autoharness"
author: "Tigerless Labs"
publisher_type: "organization"
category: "Developer Tools"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "tigerless-labs/autoharness"
  github_stars: 1400
---

# Keep Claude Code skills current from real sessions with Autoharness

Install Autoharness so Claude Code can distill, merge, update, and retire native skills from real operator sessions without a daemon or benchmark loop.

## Prerequisites

Claude Code with plugin support, Python 3.11+, GitHub access to the Autoharness plugin marketplace

## Installation

Install or set up from the source-backed instructions:

In Claude Code, run `/plugin marketplace add tigerless-labs/autoharness`, then `/plugin install autoharness@autoharness`, and finally `/reload-plugins` or restart Claude Code. Autoharness then watches eligible sessions and writes learned skills under `.claude/skills/`; use `/learn` when you want to distill the current session on demand.

- Source: https://github.com/tigerless-labs/autoharness

## Documentation

- https://github.com/tigerless-labs/autoharness

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keep-claude-code-skills-current-from-real-sessions-with-autoharness/)
