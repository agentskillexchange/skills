---
title: "Refresh Cookiecutter-based repositories from their upstream template without losing local answers"
description: "Use Cruft when an agent needs to pull new changes from a Cookiecutter template into an existing generated repository without redoing the project from scratch. The agent tracks the template origin, previews the diff, applies the update, and preserves the repository's saved answers and local customizations as carefully as possible."
verification: "security_reviewed"
source: "https://github.com/cruft/cruft"
author: "Cruft maintainers"
publisher_type: "Open Source Project"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "cruft/cruft"
  github_stars: 1564
---

# Refresh Cookiecutter-based repositories from their upstream template without losing local answers

Use Cruft when an agent needs to pull new changes from a Cookiecutter template into an existing generated repository without redoing the project from scratch. The agent tracks the template origin, previews the diff, applies the update, and preserves the repository's saved answers and local customizations as carefully as possible.

## Prerequisites

Python plus Cruft and a repository generated from a Cookiecutter template

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install cruft
```

## Documentation

- https://cruft.github.io/cruft/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/refresh-cookiecutter-based-repositories-from-upstream-template/)
