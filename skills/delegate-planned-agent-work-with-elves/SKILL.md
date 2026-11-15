---
name: "Delegate planned agent work with Elves"
slug: "delegate-planned-agent-work-with-elves"
description: "Use Elves to hand a bounded development or research plan to a separate Claude Code or Codex worker while preserving run files, worktree safety, review gates, and human merge authority."
github_stars: 188
verification: "security_reviewed"
source: "https://github.com/aigorahub/elves"
author: "aigorahub"
publisher_type: "community"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "aigorahub/elves"
  github_stars: 188
---

# Delegate planned agent work with Elves

Use Elves to hand a bounded development or research plan to a separate Claude Code or Codex worker while preserving run files, worktree safety, review gates, and human merge authority.

## Prerequisites

Claude Code or Codex, Python 3, git, optional GitHub CLI or configured worker adapters

## Installation

Install for the host agent you use:

- ELVES_TMP="$(mktemp -d)"
- git clone https://github.com/aigorahub/elves.git "$ELVES_TMP/elves"
- python3 "$ELVES_TMP/elves/scripts/sync_installed_skills.py" --apply --target claude

For Codex, use the same clone and sync script with the Codex target:

- python3 "$ELVES_TMP/elves/scripts/sync_installed_skills.py" --apply --target codex

Prerequisites: Claude Code or Codex, Python 3, and git. To validate the install, run the upstream doctor from the installed skill directory:

- python3 ~/.claude/skills/elves/scripts/install_doctor.py --startup

- Source: https://github.com/aigorahub/elves
- Extracted from upstream docs: https://raw.githubusercontent.com/aigorahub/elves/HEAD/README.md

## Documentation

- https://aigorahub.github.io/elves/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/delegate-planned-agent-work-with-elves/)
