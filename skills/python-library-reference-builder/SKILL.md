---
title: Python Library Reference Builder
description: The Python Library Reference Builder creates comprehensive, searchable
  documentation from Python packages using AST parsing and runtime introspection.
  It combines static analysis via the ast module with dynamic inspection through importlib
  and inspect to capture complete API surfaces including private methods and nested
  classes. The agent extracts docstrings in Google, NumPy, and reStructuredText formats,
  parses type hints from both annotations and docstring type specs, and identifies
  default parameter values. It builds cross-reference maps between classes, showing
  inheritance hierarchies, mixin patterns, and protocol implementations with typing
  module support. Advanced features include automated usage example extraction from
  test files and doctest blocks, deprecation notice tracking across versions, and
  integration with Sphinx autodoc for HTML documentation generation. The agent supports
  virtual environment-specific reference building, comparing API differences between
  package versions, and generating quick-start guides from README files and tutorial
  notebooks. It also indexes exception hierarchies and context manager protocols.
verification: security_reviewed
source: https://agentskillexchange.com/skills/python-library-reference-builder/
category:
- Library &amp; API Reference
framework:
- OpenClaw
---

# Python Library Reference Builder

The Python Library Reference Builder creates comprehensive, searchable documentation from Python packages using AST parsing and runtime introspection. It combines static analysis via the ast module with dynamic inspection through importlib and inspect to capture complete API surfaces including private methods and nested classes. The agent extracts docstrings in Google, NumPy, and reStructuredText formats, parses type hints from both annotations and docstring type specs, and identifies default parameter values. It builds cross-reference maps between classes, showing inheritance hierarchies, mixin patterns, and protocol implementations with typing module support. Advanced features include automated usage example extraction from test files and doctest blocks, deprecation notice tracking across versions, and integration with Sphinx autodoc for HTML documentation generation. The agent supports virtual environment-specific reference building, comparing API differences between package versions, and generating quick-start guides from README files and tutorial notebooks. It also indexes exception hierarchies and context manager protocols.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-library-reference-builder/)
