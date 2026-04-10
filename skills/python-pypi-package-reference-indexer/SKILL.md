---
title: "Python PyPI Package Reference Indexer"
description: "Indexes Python package documentation using the PyPI JSON API and Read the Docs API. Builds searchable reference catalogs with function signatures, type hints, and usage examples."
slug: "python-pypi-package-reference-indexer"
category:
  - "Library &amp; API Reference"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/python-pypi-package-reference-indexer/"
---

# Python PyPI Package Reference Indexer

Indexes Python package documentation using the PyPI JSON API and Read the Docs API. Builds searchable reference catalogs with function signatures, type hints, and usage examples.

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
clawhub install python-pypi-package-reference-indexer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Python PyPI Package Reference Indexer skill leverages the PyPI JSON API (GET /pypi/{project}/json) to retrieve package metadata including version history, dependency requirements, and project URLs. It fetches documentation from Read the Docs API (GET /api/v3/projects/{slug}/builds/) to locate built documentation artifacts. The skill parses reStructuredText and Sphinx-generated HTML to extract module hierarchies, function signatures with type annotations, class inheritance trees, and docstring content. It constructs a searchable index using inverted document indexing on function names, parameter types, and description keywords. Cross-reference resolution links related functions across packages by matching parameter types and return types. The skill generates markdown reference cards with import statements, minimal usage examples extracted from doctest blocks, and links to full documentation pages. Version comparison highlights API changes between releases using the PyPI release history endpoint.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-pypi-package-reference-indexer/)
