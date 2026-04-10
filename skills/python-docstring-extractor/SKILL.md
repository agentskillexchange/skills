---
name: Python Docstring Extractor
description: Extracts and indexes Python module documentation using ast.parse and
  docstring_parser library. Supports Google, NumPy, and Sphinx docstring formats with
  type hint cross-referencing via typing_inspect.
verification: security_reviewed
source: https://agentskillexchange.com/skills/python-docstring-extractor/
category:
- Library &amp; API Reference
framework:
- Claude Agents
---
# Python Docstring Extractor

The Python Docstring Extractor skill provides comprehensive documentation extraction and indexing for Python codebases. It uses Python's built-in ast.parse module for AST traversal to locate all function, class, and module docstrings, combined with the docstring_parser library for structured parsing of Google-style, NumPy-style, and Sphinx-format docstrings into typed sections.
The skill cross-references extracted documentation with type annotations using typing_inspect for runtime type introspection, resolving complex generics like Optional[List[Dict[str, Any]]], Protocol types, and TypeVar bounds. It generates searchable documentation indices with function signatures, parameter descriptions, return type documentation, and exception specifications.
Advanced features include inheritance chain documentation resolution using inspect.getmro for method resolution order traversal, decorator documentation extraction for @property, @staticmethod, and @classmethod variants, and cross-module reference linking via importlib.util.find_spec. The skill produces Markdown, RST, and JSON output formats compatible with Sphinx, MkDocs, and pdoc3 documentation generators. It handles __all__ exports for public API surface detection and generates deprecation notices from warnings.warn patterns in source code.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-docstring-extractor/)
