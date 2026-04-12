---
title: "Refresh Cookiecutter-based repositories from their upstream template without losing local answers"
slug: "refresh-cookiecutter-based-repositories-from-upstream-template"
verification: "security_reviewed"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
source: "https://github.com/cruft/cruft"
tool_ecosystem:
  github_repo: "cruft/cruft"
  github_stars: 1564
---

# Refresh Cookiecutter-based repositories from their upstream template without losing local answers

Use Cruft when an agent needs to pull new changes from a Cookiecutter template into an existing generated repository without redoing the project from scratch. The agent tracks the template origin, previews the diff, applies the update, and preserves the repository’s saved answers and local customizations as carefully as possible.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/refresh-cookiecutter-based-repositories-from-upstream-template/)
