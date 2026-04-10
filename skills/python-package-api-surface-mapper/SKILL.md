---
title: "Python Package API Surface Mapper"
description: "Maps the public API surface of Python packages using ast module parsing and importlib introspection. Generates comprehensive reference docs with type annotations from mypy stubs."
slug: "python-package-api-surface-mapper"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/python-package-api-surface-mapper/"
listed: true
---

# Python Package API Surface Mapper

Maps the public API surface of Python packages using ast module parsing and importlib introspection. Generates comprehensive reference docs with type annotations from mypy stubs.

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
clawhub install python-package-api-surface-mapper
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Python Package API Surface Mapper skill analyzes Python packages to produce complete public API documentation. It uses Python ast module to parse source files and extract function signatures, class hierarchies, and module-level constants without executing the code.
The skill leverages importlib.metadata to resolve package dependencies and version constraints. It cross-references type annotations with mypy typeshed stubs and inline type hints to produce fully typed API signatures including generic types and Protocol definitions.
Using the docstring-parser library, the skill extracts and normalizes docstrings from Google, NumPy, and Sphinx formats into a consistent structure. It identifies deprecated APIs via the warnings module usage and PEP 702 deprecation decorators.
Output includes Sphinx RST files ready for ReadTheDocs integration, MkDocs-compatible Markdown via mkdocstrings, and a structured JSON format suitable for IDE autocompletion databases. The skill also generates a changelog of API surface changes between package versions using ast-based diffing.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-package-api-surface-mapper/)
