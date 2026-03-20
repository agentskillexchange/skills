---
name: Python Package Docs Fetcher
description: Retrieves and indexes Python package documentation from PyPI metadata API and Read the Docs API. Uses ast module parsing and pydoc introspection to extract function signatures, docstrings, and type hi
category: Library & API Reference
framework: OpenClaw
verification: security_reviewed
rating: 4.8
reviews: 78
source: https://agentskillexchange.com/skill/python-package-docs-fetcher/
---

# Python Package Docs Fetcher

Retrieves and indexes Python package documentation from PyPI metadata API and Read the Docs API. Uses ast module parsing and pydoc introspection to extract function signatures, docstrings, and type hints for offline reference.

## Overview

The Python Package Docs Fetcher skill provides offline-capable Python package documentation retrieval and indexing. It queries the PyPI JSON API for package metadata including version history, dependencies, and project URLs.
For packages hosted on Read the Docs, the skill uses the RTD API v3 to fetch rendered documentation pages and convert them to searchable markdown format. It builds a local index using whoosh for full-text search across downloaded documentation.
The skill also performs direct source code analysis using Python ast module parsing to extract function signatures, class hierarchies, and type annotations. Combined with pydoc introspection on installed packages, it generates comprehensive API reference cards with parameter types, return values, and usage examples.
Documentation is cached locally with version-aware invalidation, reducing API calls for frequently referenced packages. The skill supports private PyPI registries, namespace packages, and generates cross-reference links between related packages in the documentation index.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill python-package-docs-fetcher
```

### OpenClaw

```bash
openclaw install python-package-docs-fetcher
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Library & API Reference |
| Framework | OpenClaw |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (78 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/python-package-docs-fetcher/)*
