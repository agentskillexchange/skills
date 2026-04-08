---
title: Python Package API Surface Mapper
description: The Python Package API Surface Mapper skill analyzes Python packages
  to produce complete public API documentation. It uses Python ast module to parse
  source files and extract function signatures, class hierarchies, and module-level
  constants without executing the code. The skill leverages importlib.metadata to
  resolve package dependencies and version constraints. It cross-references type annotations
  with mypy typeshed stubs and inline type hints to produce fully typed API signatures
  including generic types and Protocol definitions. Using the docstring-parser library,
  the skill extracts and normalizes docstrings from Google, NumPy, and Sphinx formats
  into a consistent structure. It identifies deprecated APIs via the warnings module
  usage and PEP 702 deprecation decorators. Output includes Sphinx RST files ready
  for ReadTheDocs integration, MkDocs-compatible Markdown via mkdocstrings, and a
  structured JSON format suitable for IDE autocompletion databases. The skill also
  generates a changelog of API surface changes between package versions using ast-based
  diffing.
verification: security_reviewed
source: https://agentskillexchange.com/skills/python-package-api-surface-mapper/
category:
- Library &amp; API Reference
framework:
- Codex
---

# Python Package API Surface Mapper

The Python Package API Surface Mapper skill analyzes Python packages to produce complete public API documentation. It uses Python ast module to parse source files and extract function signatures, class hierarchies, and module-level constants without executing the code. The skill leverages importlib.metadata to resolve package dependencies and version constraints. It cross-references type annotations with mypy typeshed stubs and inline type hints to produce fully typed API signatures including generic types and Protocol definitions. Using the docstring-parser library, the skill extracts and normalizes docstrings from Google, NumPy, and Sphinx formats into a consistent structure. It identifies deprecated APIs via the warnings module usage and PEP 702 deprecation decorators. Output includes Sphinx RST files ready for ReadTheDocs integration, MkDocs-compatible Markdown via mkdocstrings, and a structured JSON format suitable for IDE autocompletion databases. The skill also generates a changelog of API surface changes between package versions using ast-based diffing.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-package-api-surface-mapper/)
