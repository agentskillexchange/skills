---
name: "Python Package API Surface Mapper"
description: "Maps the public API surface of Python packages using ast module parsing and importlib introspection. Generates comprehensive reference docs with type annotations from mypy stubs."
category: "Library &amp; API Reference"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/python-package-api-surface-mapper/"
---
# Python Package API Surface Mapper

Maps the public API surface of Python packages using ast module parsing and importlib introspection. Generates comprehensive reference docs with type annotations from mypy stubs.

## Overview

The Python Package API Surface Mapper skill analyzes Python packages to produce complete public API documentation. It uses Python ast module to parse source files and extract function signatures, class hierarchies, and module-level constants without executing the code.

The skill leverages importlib.metadata to resolve package dependencies and version constraints. It cross-references type annotations with mypy typeshed stubs and inline type hints to produce fully typed API signatures including generic types and Protocol definitions.

Using the docstring-parser library, the skill extracts and normalizes docstrings from Google, NumPy, and Sphinx formats into a consistent structure. It identifies deprecated APIs via the warnings module usage and PEP 702 deprecation decorators.

Output includes Sphinx RST files ready for ReadTheDocs integration, MkDocs-compatible Markdown via mkdocstrings, and a structured JSON format suitable for IDE autocompletion databases. The skill also generates a changelog of API surface changes between package versions using ast-based diffing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill python-package-api-surface-mapper
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill python-package-api-surface-mapper -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill python-package-api-surface-mapper -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill python-package-api-surface-mapper -a codex
```

### OpenClaw

```bash
clawhub install python-package-api-surface-mapper
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-package-api-surface-mapper/)
