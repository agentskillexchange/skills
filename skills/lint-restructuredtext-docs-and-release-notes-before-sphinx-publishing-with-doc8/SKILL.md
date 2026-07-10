---
title: "Lint reStructuredText docs and release notes before Sphinx publishing with doc8"
description: "Catch structural and line-style problems in reStructuredText docs before release notes and Sphinx pages go out broken or noisy."
verification: "security_reviewed"
source: "https://github.com/PyCQA/doc8"
author: "PyCQA"
publisher_type: "organization"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "PyCQA/doc8"
  github_stars: 176
---

# Lint reStructuredText docs and release notes before Sphinx publishing with doc8

Catch structural and line-style problems in reStructuredText docs before release notes and Sphinx pages go out broken or noisy.

## Prerequisites

Python and the doc8 CLI in a repository with reStructuredText or plain-text documentation.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with pip install doc8, then run doc8 docs/ or point it at the relevant documentation paths. Optional configuration can live in pyproject.toml, setup.cfg, or another supported config file.
```

## Documentation

- https://doc8.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-restructuredtext-docs-and-release-notes-before-sphinx-publishing-with-doc8/)
