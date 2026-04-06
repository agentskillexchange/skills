---
name: Python Docstring Linter
description: Validates and auto-generates Python docstrings using the ast module and
  pydocstyle conventions. Supports NumPy, Google, and Sphinx docstring formats with
  type stub integration.
category: "Library &amp; API Reference"
framework: Codex
verification: security_reviewed
source: "https://agentskillexchange.com/skills/python-docstring-linter-ast-pydocstyle/"
---
# Python Docstring Linter

Validates and auto-generates Python docstrings using the ast module and pydocstyle conventions. Supports NumPy, Google, and Sphinx docstring formats with type stub integration.

Python Docstring Linter uses the Python ast module to parse source files and analyze function, class, and module docstrings for completeness and correctness. It enforces pydocstyle conventions (PEP 257) with support for NumPy, Google, and Sphinx docstring formats. The tool cross-references docstring parameter descriptions with actual function signatures and type annotations from both inline hints and stub files (.pyi). Auto-generation mode creates skeleton docstrings from function signatures, including parameter types inferred from mypy type checking results. It validates example code blocks within docstrings by executing them as doctests, reporting failures inline. Integration with Sphinx autodoc ensures generated documentation renders correctly. Batch processing handles entire Python packages with configurable ignore patterns and per-file format overrides. The linter outputs results in SARIF format for GitHub Code Scanning integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill python-docstring-linter-ast-pydocstyle
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill python-docstring-linter-ast-pydocstyle -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill python-docstring-linter-ast-pydocstyle -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill python-docstring-linter-ast-pydocstyle -a codex
```

### OpenClaw

```bash
clawhub install python-docstring-linter-ast-pydocstyle
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-docstring-linter-ast-pydocstyle/)
