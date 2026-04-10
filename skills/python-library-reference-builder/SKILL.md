---
title: "Python Library Reference Builder"
description: "Generates searchable Python library references using ast module for source parsing and Sphinx autodoc integration. Extracts docstrings, type hints, and usage examples from installed packages via importlib."
slug: "python-library-reference-builder"
category:
  - "Library &amp; API Reference"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/python-library-reference-builder/"
---

# Python Library Reference Builder

Generates searchable Python library references using ast module for source parsing and Sphinx autodoc integration. Extracts docstrings, type hints, and usage examples from installed packages via importlib.

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
clawhub install python-library-reference-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Python Library Reference Builder creates comprehensive, searchable documentation from Python packages using AST parsing and runtime introspection. It combines static analysis via the ast module with dynamic inspection through importlib and inspect to capture complete API surfaces including private methods and nested classes.
The agent extracts docstrings in Google, NumPy, and reStructuredText formats, parses type hints from both annotations and docstring type specs, and identifies default parameter values. It builds cross-reference maps between classes, showing inheritance hierarchies, mixin patterns, and protocol implementations with typing module support.
Advanced features include automated usage example extraction from test files and doctest blocks, deprecation notice tracking across versions, and integration with Sphinx autodoc for HTML documentation generation. The agent supports virtual environment-specific reference building, comparing API differences between package versions, and generating quick-start guides from README files and tutorial notebooks. It also indexes exception hierarchies and context manager protocols.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-library-reference-builder/)
