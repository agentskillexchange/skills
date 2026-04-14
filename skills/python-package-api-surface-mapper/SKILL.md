---
title: "Python Package API Surface Mapper"
description: "Maps the public API surface of Python packages using ast module parsing and importlib introspection. Generates comprehensive reference docs with type annotations from mypy stubs."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/python-package-api-surface-mapper/"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
---

# Python Package API Surface Mapper

The Python Package API Surface Mapper skill analyzes Python packages to produce complete public API documentation. It uses Python ast module to parse source files and extract function signatures, class hierarchies, and module-level constants without executing the code.

The skill leverages importlib.metadata to resolve package dependencies and version constraints. It cross-references type annotations with mypy typeshed stubs and inline type hints to produce fully typed API signatures including generic types and Protocol definitions.

Using the docstring-parser library, the skill extracts and normalizes docstrings from Google, NumPy, and Sphinx formats into a consistent structure. It identifies deprecated APIs via the warnings module usage and PEP 702 deprecation decorators.

Output includes Sphinx RST files ready for ReadTheDocs integration, MkDocs-compatible Markdown via mkdocstrings, and a structured JSON format suitable for IDE autocompletion databases. The skill also generates a changelog of API surface changes between package versions using ast-based diffing.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-package-api-surface-mapper/)
