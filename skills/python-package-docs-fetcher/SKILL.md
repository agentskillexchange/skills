---
title: Python Package Docs Fetcher
description: The Python Package Docs Fetcher skill provides offline-capable Python
  package documentation retrieval and indexing. It queries the PyPI JSON API for package
  metadata including version history, dependencies, and project URLs. For packages
  hosted on Read the Docs, the skill uses the RTD API v3 to fetch rendered documentation
  pages and convert them to searchable markdown format. It builds a local index using
  whoosh for full-text search across downloaded documentation. The skill also performs
  direct source code analysis using Python ast module parsing to extract function
  signatures, class hierarchies, and type annotations. Combined with pydoc introspection
  on installed packages, it generates comprehensive API reference cards with parameter
  types, return values, and usage examples. Documentation is cached locally with version-aware
  invalidation, reducing API calls for frequently referenced packages. The skill supports
  private PyPI registries, namespace packages, and generates cross-reference links
  between related packages in the documentation index.
verification: security_reviewed
source: https://agentskillexchange.com/skills/python-package-docs-fetcher/
category:
- Library &amp; API Reference
framework:
- OpenClaw
---

# Python Package Docs Fetcher

The Python Package Docs Fetcher skill provides offline-capable Python package documentation retrieval and indexing. It queries the PyPI JSON API for package metadata including version history, dependencies, and project URLs. For packages hosted on Read the Docs, the skill uses the RTD API v3 to fetch rendered documentation pages and convert them to searchable markdown format. It builds a local index using whoosh for full-text search across downloaded documentation. The skill also performs direct source code analysis using Python ast module parsing to extract function signatures, class hierarchies, and type annotations. Combined with pydoc introspection on installed packages, it generates comprehensive API reference cards with parameter types, return values, and usage examples. Documentation is cached locally with version-aware invalidation, reducing API calls for frequently referenced packages. The skill supports private PyPI registries, namespace packages, and generates cross-reference links between related packages in the documentation index.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-package-docs-fetcher/)
