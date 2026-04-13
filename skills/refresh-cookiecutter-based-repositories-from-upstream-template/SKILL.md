---
title: "Refresh Cookiecutter-based repositories from their upstream template without losing local answers"
description: "Use Cruft when an agent needs to pull new changes from a Cookiecutter template into an existing generated repository without redoing the project from scratch. The agent tracks the template origin, previews the diff, applies the update, and preserves the repository’s saved answers and local customizations as carefully as possible."
verification: "security_reviewed"
source: "https://github.com/cruft/cruft"
category: ["Templates &amp; Workflows"]
framework: ["Multi-Framework"]
tool_ecosystem:
  github_repo: "cruft/cruft"
  github_stars: 1564
---

# Refresh Cookiecutter-based repositories from their upstream template without losing local answers

Use Cruft when an agent needs to pull new changes from a Cookiecutter template into an existing generated repository without redoing the project from scratch. The agent tracks the template origin, previews the diff, applies the update, and preserves the repository’s saved answers and local customizations as carefully as possible.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/refresh-cookiecutter-based-repositories-from-upstream-template/)
