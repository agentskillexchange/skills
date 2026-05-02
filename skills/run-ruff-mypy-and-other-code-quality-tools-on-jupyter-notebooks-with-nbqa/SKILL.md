---
title: "Run Ruff, Mypy, and other code-quality tools on Jupyter notebooks with nbQA"
description: "Apply standard Python formatters, linters, and type checkers to notebook-heavy repositories without manually converting notebooks to scripts."
verification: "listed"
source: "https://github.com/nbQA-dev/nbQA"
author: "nbQA-dev"
publisher_type: "organization"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "nbQA-dev/nbQA"
  github_stars: 1196
---

# Run Ruff, Mypy, and other code-quality tools on Jupyter notebooks with nbQA

Apply standard Python formatters, linters, and type checkers to notebook-heavy repositories without manually converting notebooks to scripts.

## Prerequisites

Python 3, pip, nbQA, Jupyter notebooks, underlying QA tools such as Ruff or Mypy

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install nbqa` plus the linters or formatters you want to run, then invoke commands like `nbqa ruff .` or `nbqa mypy notebook.ipynb`.
```

## Documentation

- https://nbqa.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-ruff-mypy-and-other-code-quality-tools-on-jupyter-notebooks-with-nbqa/)
