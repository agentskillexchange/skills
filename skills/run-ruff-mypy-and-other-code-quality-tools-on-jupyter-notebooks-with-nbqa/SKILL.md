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

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-ruff-mypy-and-other-code-quality-tools-on-jupyter-notebooks-with-nbqa/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-ruff-mypy-and-other-code-quality-tools-on-jupyter-notebooks-with-nbqa
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-ruff-mypy-and-other-code-quality-tools-on-jupyter-notebooks-with-nbqa`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-ruff-mypy-and-other-code-quality-tools-on-jupyter-notebooks-with-nbqa/)
