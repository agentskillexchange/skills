---
title: "Python PyPI Package Reference Indexer"
description: "Indexes Python package documentation using the PyPI JSON API and Read the Docs API. Builds searchable reference catalogs with function signatures, type hints, and usage examples."
verification: "security_reviewed"
source: "https://docs.pypi.org/"
category:
  - "Library & API Reference"
framework:
  - "ChatGPT Agents"
---

# Python PyPI Package Reference Indexer

The Python PyPI Package Reference Indexer skill leverages the PyPI JSON API (GET /pypi/{project}/json) to retrieve package metadata including version history, dependency requirements, and project URLs. It fetches documentation from Read the Docs API (GET /api/v3/projects/{slug}/builds/) to locate built documentation artifacts. The skill parses reStructuredText and Sphinx-generated HTML to extract module hierarchies, function signatures with type annotations, class inheritance trees, and docstring content. It constructs a searchable index using inverted document indexing on function names, parameter types, and description keywords. Cross-reference resolution links related functions across packages by matching parameter types and return types. The skill generates markdown reference cards with import statements, minimal usage examples extracted from doctest blocks, and links to full documentation pages. Version comparison highlights API changes between releases using the PyPI release history endpoint.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/python-pypi-package-reference-indexer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/python-pypi-package-reference-indexer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/python-pypi-package-reference-indexer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-pypi-package-reference-indexer/)
