---
title: Python Docstring Linter
description: Python Docstring Linter uses the Python ast module to parse source files
  and analyze function, class, and module docstrings for completeness and correctness.
  It enforces pydocstyle conventions (PEP 257) with support for NumPy, Google, and
  Sphinx docstring formats. The tool cross-references docstring parameter descriptions
  with actual function signatures and type annotations from both inline hints and
  stub files (.pyi). Auto-generation mode creates skeleton docstrings from function
  signatures, including parameter types inferred from mypy type checking results.
  It validates example code blocks within docstrings by executing them as doctests,
  reporting failures inline. Integration with Sphinx autodoc ensures generated documentation
  renders correctly. Batch processing handles entire Python packages with configurable
  ignore patterns and per-file format overrides. The linter outputs results in SARIF
  format for GitHub Code Scanning integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/python-docstring-linter-ast-pydocstyle/
category:
- Library &amp; API Reference
framework:
- Codex
---

# Python Docstring Linter

Python Docstring Linter uses the Python ast module to parse source files and analyze function, class, and module docstrings for completeness and correctness. It enforces pydocstyle conventions (PEP 257) with support for NumPy, Google, and Sphinx docstring formats. The tool cross-references docstring parameter descriptions with actual function signatures and type annotations from both inline hints and stub files (.pyi). Auto-generation mode creates skeleton docstrings from function signatures, including parameter types inferred from mypy type checking results. It validates example code blocks within docstrings by executing them as doctests, reporting failures inline. Integration with Sphinx autodoc ensures generated documentation renders correctly. Batch processing handles entire Python packages with configurable ignore patterns and per-file format overrides. The linter outputs results in SARIF format for GitHub Code Scanning integration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-docstring-linter-ast-pydocstyle/)
