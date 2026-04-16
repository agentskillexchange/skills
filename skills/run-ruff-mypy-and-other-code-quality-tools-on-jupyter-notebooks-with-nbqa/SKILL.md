---
title: "Run Ruff, Mypy, and other code-quality tools on Jupyter notebooks with nbQA"
description: "Apply standard Python formatters, linters, and type checkers to notebook-heavy repositories without manually converting notebooks to scripts."
verification: "listed"
source: "https://github.com/nbQA-dev/nbQA"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "nbQA-dev/nbQA"
  github_stars: 1196
---

# Run Ruff, Mypy, and other code-quality tools on Jupyter notebooks with nbQA

Use nbQA when an agent needs to run existing Python quality tooling against Jupyter notebooks instead of skipping notebooks or converting them by hand. The agent can invoke Ruff, Mypy, Black, or other supported tools across `.ipynb` files and return notebook-specific findings in the same review pass as normal Python code. The boundary is notebook-aware quality enforcement, not a generic notebook platform or a broad Python tooling bundle.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-ruff-mypy-and-other-code-quality-tools-on-jupyter-notebooks-with-nbqa/)
