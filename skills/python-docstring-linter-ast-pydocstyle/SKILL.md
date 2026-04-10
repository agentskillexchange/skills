---
title: "Python Docstring Linter"
description: "Validates and auto-generates Python docstrings using the ast module and pydocstyle conventions. Supports NumPy, Google, and Sphinx docstring formats with type stub integration."
slug: "python-docstring-linter-ast-pydocstyle"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/python-docstring-linter-ast-pydocstyle/"
---

# Python Docstring Linter

Validates and auto-generates Python docstrings using the ast module and pydocstyle conventions. Supports NumPy, Google, and Sphinx docstring formats with type stub integration.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install python-docstring-linter-ast-pydocstyle
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Python Docstring Linter uses the Python ast module to parse source files and analyze function, class, and module docstrings for completeness and correctness. It enforces pydocstyle conventions (PEP 257) with support for NumPy, Google, and Sphinx docstring formats. The tool cross-references docstring parameter descriptions with actual function signatures and type annotations from both inline hints and stub files (.pyi). Auto-generation mode creates skeleton docstrings from function signatures, including parameter types inferred from mypy type checking results. It validates example code blocks within docstrings by executing them as doctests, reporting failures inline. Integration with Sphinx autodoc ensures generated documentation renders correctly. Batch processing handles entire Python packages with configurable ignore patterns and per-file format overrides. The linter outputs results in SARIF format for GitHub Code Scanning integration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-docstring-linter-ast-pydocstyle/)
