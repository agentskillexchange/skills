---
name: Python Package Docs Fetcher
description: Retrieves and indexes Python package documentation from PyPI metadata
  API and Read the Docs API. Uses ast module parsing and pydoc introspection to extract
  function signatures, docstrings, and type hints for offline reference.
verification: security_reviewed
source: https://agentskillexchange.com/skills/python-package-docs-fetcher/
category:
- Library &amp; API Reference
framework:
- OpenClaw
---
# Python Package Docs Fetcher

The Python Package Docs Fetcher skill provides offline-capable Python package documentation retrieval and indexing. It queries the PyPI JSON API for package metadata including version history, dependencies, and project URLs.
For packages hosted on Read the Docs, the skill uses the RTD API v3 to fetch rendered documentation pages and convert them to searchable markdown format. It builds a local index using whoosh for full-text search across downloaded documentation.
The skill also performs direct source code analysis using Python ast module parsing to extract function signatures, class hierarchies, and type annotations. Combined with pydoc introspection on installed packages, it generates comprehensive API reference cards with parameter types, return values, and usage examples.
Documentation is cached locally with version-aware invalidation, reducing API calls for frequently referenced packages. The skill supports private PyPI registries, namespace packages, and generates cross-reference links between related packages in the documentation index.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-package-docs-fetcher/)
