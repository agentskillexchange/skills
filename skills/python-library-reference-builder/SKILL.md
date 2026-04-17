---
title: "Python Library Reference Builder"
description: "The Python Library Reference Builder creates comprehensive, searchable documentation from Python packages using AST parsing and runtime introspection. It combines static analysis via the ast module with dynamic inspection through importlib and inspect to capture complete API surfaces including private methods and nested classes.\nThe agent extracts docstrings in Google, NumPy, and reStructuredText formats, parses type hints from both annotations and docstring type specs, and identifies default parameter values. It builds cross-reference maps between classes, showing inheritance hierarchies, mixin patterns, and protocol implementations with typing module support.\nAdvanced features include automated usage example extraction from test files and doctest blocks, deprecation notice tracking across versions, and integration with Sphinx autodoc for HTML documentation generation. The agent supports virtual environment-specific reference building, comparing API differences between package versions, and generating quick-start guides from README files and tutorial notebooks. It also indexes exception hierarchies and context manager protocols."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/python-library-reference-builder/"
framework:
  - "OpenClaw"
---

# Python Library Reference Builder

The Python Library Reference Builder creates comprehensive, searchable documentation from Python packages using AST parsing and runtime introspection. It combines static analysis via the ast module with dynamic inspection through importlib and inspect to capture complete API surfaces including private methods and nested classes.
The agent extracts docstrings in Google, NumPy, and reStructuredText formats, parses type hints from both annotations and docstring type specs, and identifies default parameter values. It builds cross-reference maps between classes, showing inheritance hierarchies, mixin patterns, and protocol implementations with typing module support.
Advanced features include automated usage example extraction from test files and doctest blocks, deprecation notice tracking across versions, and integration with Sphinx autodoc for HTML documentation generation. The agent supports virtual environment-specific reference building, comparing API differences between package versions, and generating quick-start guides from README files and tutorial notebooks. It also indexes exception hierarchies and context manager protocols.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/python-library-reference-builder
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/python-library-reference-builder` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-library-reference-builder/)
