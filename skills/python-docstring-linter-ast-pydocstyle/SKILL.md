---
title: "Python Docstring Linter"
description: "Validates and auto-generates Python docstrings using the ast module and pydocstyle conventions. Supports NumPy, Google, and Sphinx docstring formats with type stub integration."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/python-docstring-linter-ast-pydocstyle/"
category:
  - "Library & API Reference"
framework:
  - "Codex"
---

# Python Docstring Linter

Python Docstring Linter uses the Python ast module to parse source files and analyze function, class, and module docstrings for completeness and correctness. It enforces pydocstyle conventions (PEP 257) with support for NumPy, Google, and Sphinx docstring formats. The tool cross-references docstring parameter descriptions with actual function signatures and type annotations from both inline hints and stub files (.pyi). Auto-generation mode creates skeleton docstrings from function signatures, including parameter types inferred from mypy type checking results. It validates example code blocks within docstrings by executing them as doctests, reporting failures inline. Integration with Sphinx autodoc ensures generated documentation renders correctly. Batch processing handles entire Python packages with configurable ignore patterns and per-file format overrides. The linter outputs results in SARIF format for GitHub Code Scanning integration.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-docstring-linter-ast-pydocstyle/)
