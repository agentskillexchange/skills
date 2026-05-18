---
name: "Catch common misspellings in code and docs before review churn with codespell"
slug: "catch-common-misspellings-in-code-and-docs-before-review-churn-with-codespell"
description: "Run a fast typo pass across source files and documentation so common misspellings are fixed before they spread through reviews and releases."
github_stars: 2356
verification: "listed"
source: "https://github.com/codespell-project/codespell"
author: "codespell-project"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "codespell-project/codespell"
  github_stars: 2356
---

# Catch common misspellings in code and docs before review churn with codespell

Run a fast typo pass across source files and documentation so common misspellings are fixed before they spread through reviews and releases.

## Prerequisites

Python 3.9+ and the codespell CLI in a checked-out repository or docs tree.

## Installation

Use the upstream install or setup path that matches your environment:
- You can use pip to install codespell with e.g.:
- pip install codespell
- pip install --upgrade pip setuptools setuptools_scm wheel
- pip install -e ".[dev]"

Requirements and caveats from upstream:
- Python 3.9 or above.
- When ignoring false positives, note that spelling errors are *case-insensitive* but words to ignore are *case-sensitive*. For example, the dictionary entry wrod will also match the typo Wrod, but to ignore it you must...
- Some situation might require ignoring a specific word in a specific location. This can be achieved by adding a comment in the source code.

Basic usage or getting-started notes:
- ------------
- .. code-block:: sh
- -----

- Source: https://github.com/codespell-project/codespell
- Extracted from upstream docs: https://raw.githubusercontent.com/codespell-project/codespell/HEAD/README.rst

## Documentation

- https://github.com/codespell-project/codespell

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/catch-common-misspellings-in-code-and-docs-before-review-churn-with-codespell/)
