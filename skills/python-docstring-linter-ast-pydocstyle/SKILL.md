---
title: "Python Docstring Linter"
description: "Validates and auto-generates Python docstrings using the ast module and pydocstyle conventions. Supports NumPy, Google, and Sphinx docstring formats with type stub integration."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/python-docstring-linter-ast-pydocstyle/"
category:
  - "Library & API Reference"
framework:
  - "Codex"
---

# Python Docstring Linter

Python Docstring Linter uses the Python ast module to parse source files and analyze function, class, and module docstrings for completeness and correctness. It enforces pydocstyle conventions (PEP 257) with support for NumPy, Google, and Sphinx docstring formats. The tool cross-references docstring parameter descriptions with actual function signatures and type annotations from both inline hints and stub files (.pyi). Auto-generation mode creates skeleton docstrings from function signatures, including parameter types inferred from mypy type checking results. It validates example code blocks within docstrings by executing them as doctests, reporting failures inline. Integration with Sphinx autodoc ensures generated documentation renders correctly. Batch processing handles entire Python packages with configurable ignore patterns and per-file format overrides. The linter outputs results in SARIF format for GitHub Code Scanning integration.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/python-docstring-linter-ast-pydocstyle
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/python-docstring-linter-ast-pydocstyle` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-docstring-linter-ast-pydocstyle/)
