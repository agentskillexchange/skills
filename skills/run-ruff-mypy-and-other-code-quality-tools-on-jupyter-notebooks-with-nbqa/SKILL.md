---
name: "Run Ruff, Mypy, and other code-quality tools on Jupyter notebooks with nbQA"
slug: "run-ruff-mypy-and-other-code-quality-tools-on-jupyter-notebooks-with-nbqa"
description: "Apply standard Python formatters, linters, and type checkers to notebook-heavy repositories without manually converting notebooks to scripts."
github_stars: 1196
verification: "listed"
source: "https://github.com/nbQA-dev/nbQA"
author: "nbQA-dev"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "nbQA-dev/nbQA"
  github_stars: 1196
---

# Run Ruff, Mypy, and other code-quality tools on Jupyter notebooks with nbQA

Apply standard Python formatters, linters, and type checkers to notebook-heavy repositories without manually converting notebooks to scripts.

## Prerequisites

Python 3, pip, nbQA, Jupyter notebooks, underlying QA tools such as Ruff or Mypy

## Installation

Use the upstream install or setup path that matches your environment:
- $ python -m pip install -U nbqa
- $ python -m pip install -U "nbqa[toolchain]"

Requirements and caveats from upstream:
- In your [virtual environment](https://realpython.com/python-virtual-environments-a-primer/), run (note: the $ is not part of the command):
- Format .md files saved via [Jupytext](https://github.com/mwouts/jupytext) (requires jupytext to be installed):
- See [command-line examples](https://nbqa.readthedocs.io/en/latest/examples.html) for examples involving [doctest](https://docs.python.org/3/library/doctest.html), [flake8](https://flake8.pycqa.org/en/latest/), [mypy](...

Basic usage or getting-started notes:
- Run ruff, isort, pyupgrade, mypy, pylint, flake8, black, blacken-docs, and more on Jupyter Notebooks
- Here's an example of how to set up some pre-commit hooks: put this in your .pre-commit-config.yaml file (see [usage as pre-commit hook](https://nbqa.readthedocs.io/en/latest/pre-commit.html))
- https://github.com/DataS-DHSC/os-maps-example

- Source: https://github.com/nbQA-dev/nbQA
- Extracted from upstream docs: https://raw.githubusercontent.com/nbQA-dev/nbQA/HEAD/README.md

## Documentation

- https://nbqa.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-ruff-mypy-and-other-code-quality-tools-on-jupyter-notebooks-with-nbqa/)
