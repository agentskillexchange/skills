---
title: "Python Library Reference Builder"
description: "The Python Library Reference Builder creates comprehensive, searchable documentation from Python packages using AST parsing and runtime introspection. It combines static analysis via the ast module with dynamic inspection through importlib and inspect to capture complete API surfaces including private methods and nested classes. The agent extracts docstrings in Google, NumPy, and reStructuredText formats, parses type hints from both annotations and docstring type specs, and identifies default parameter values. It builds cross-reference maps between classes, showing inheritance hierarchies, mixin patterns, and protocol implementations with typing module support. Advanced features include automated usage example extraction from test files and doctest blocks, deprecation notice tracking across versions, and integration with Sphinx autodoc for HTML documentation generation. The agent supports virtual environment-specific reference building, comparing API differences between package versions, and generating quick-start guides from README files and tutorial notebooks. It also indexes exception hierarchies and context manager protocols."
source: "https://agentskillexchange.com/skills/python-library-reference-builder/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "OpenClaw"
---

# Python Library Reference Builder

The Python Library Reference Builder creates comprehensive, searchable documentation from Python packages using AST parsing and runtime introspection. It combines static analysis via the ast module with dynamic inspection through importlib and inspect to capture complete API surfaces including private methods and nested classes. The agent extracts docstrings in Google, NumPy, and reStructuredText formats, parses type hints from both annotations and docstring type specs, and identifies default parameter values. It builds cross-reference maps between classes, showing inheritance hierarchies, mixin patterns, and protocol implementations with typing module support. Advanced features include automated usage example extraction from test files and doctest blocks, deprecation notice tracking across versions, and integration with Sphinx autodoc for HTML documentation generation. The agent supports virtual environment-specific reference building, comparing API differences between package versions, and generating quick-start guides from README files and tutorial notebooks. It also indexes exception hierarchies and context manager protocols.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-library-reference-builder/)
