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

## Usage and Verification

Use a disposable project and non-sensitive test sessions first. After reload, check that Claude Code lists the plugin and that `python3` is available. Work through a small repeatable task and inspect `.claude/autoharness/` for session bookkeeping. Default reflection occurs after multiple turns, so no new skill after a single turn is not a failure.

If a skill is created, inspect its `SKILL.md`, `.ledger.jsonl`, and referenced evidence under `.claude/skills/`. Compare the learned procedure with the actual test session and review the project diff. Also inspect the global `~/.claude/skills/` location when learning was not project-specific. A usage counter indicates recall, not correctness; verify the procedure on another safe task before relying on it.

The plugin reads session material and may write learned instructions. Keep credentials and confidential examples out of the pilot, review generated evidence for sensitive content, and require approval before sharing learned files. Uninstalling the plugin does not remove its generated skills or state; review those separately rather than deleting unrelated user skills. See the upstream walkthrough and uninstall guidance below.

## Documentation

- https://github.com/tigerless-labs/autoharness

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keep-claude-code-skills-current-from-real-sessions-with-autoharness/)
