---
name: "Python Library Reference Builder"
description: "Generates searchable Python library references using ast module for source parsing and Sphinx autodoc integration. Extracts docstrings, type hints, and usage examples from installed packages via importlib."
category: "Library & API Reference"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/python-library-reference-builder/"
---

# Python Library Reference Builder

Generates searchable Python library references using ast module for source parsing and Sphinx autodoc integration. Extracts docstrings, type hints, and usage examples from installed packages via importlib.

## Overview

The Python Library Reference Builder creates comprehensive, searchable documentation from Python packages using AST parsing and runtime introspection. It combines static analysis via the ast module with dynamic inspection through importlib and inspect to capture complete API surfaces including private methods and nested classes.

The agent extracts docstrings in Google, NumPy, and reStructuredText formats, parses type hints from both annotations and docstring type specs, and identifies default parameter values. It builds cross-reference maps between classes, showing inheritance hierarchies, mixin patterns, and protocol implementations with typing module support.

Advanced features include automated usage example extraction from test files and doctest blocks, deprecation notice tracking across versions, and integration with Sphinx autodoc for HTML documentation generation. The agent supports virtual environment-specific reference building, comparing API differences between package versions, and generating quick-start guides from README files and tutorial notebooks. It also indexes exception hierarchies and context manager protocols.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill python-library-reference-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill python-library-reference-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill python-library-reference-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill python-library-reference-builder -a codex
```

### OpenClaw

```bash
clawhub install python-library-reference-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/python-library-reference-builder/
