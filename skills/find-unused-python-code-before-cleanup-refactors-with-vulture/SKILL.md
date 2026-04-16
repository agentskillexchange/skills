---
title: "Find unused Python code before cleanup refactors with Vulture"
description: "Run a dead-code pass on Python repositories before refactors so agents can flag unused functions, classes, imports, and variables instead of deleting blindly."
verification: "listed"
source: "https://github.com/jendrikseipp/vulture"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jendrikseipp/vulture"
  github_stars: 4521
---

# Find unused Python code before cleanup refactors with Vulture

Use Vulture when an agent is preparing a Python cleanup, migration, or repo-slimming pass and needs a focused list of likely unused code first. The agent can scan the project, review suspicious dead-code findings, and hand back a triage list before any destructive edits happen. The boundary is a pre-refactor dead-code review loop for Python, not a generic Python toolkit or broad linting platform listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-unused-python-code-before-cleanup-refactors-with-vulture/)
