---
title: "Python PyPI Package Reference Indexer"
description: "The Python PyPI Package Reference Indexer skill leverages the PyPI JSON API (GET /pypi/{project}/json) to retrieve package metadata including version history, dependency requirements, and project URLs. It fetches documentation from Read the Docs API (GET /api/v3/projects/{slug}/builds/) to locate built documentation artifacts. The skill parses reStructuredText and Sphinx-generated HTML to extract module hierarchies, function signatures with type annotations, class inheritance trees, and docstring content. It constructs a searchable index using inverted document indexing on function names, parameter types, and description keywords. Cross-reference resolution links related functions across packages by matching parameter types and return types. The skill generates markdown reference cards with import statements, minimal usage examples extracted from doctest blocks, and links to full documentation pages. Version comparison highlights API changes between releases using the PyPI release history endpoint."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/python-pypi-package-reference-indexer/"
framework:
  - "ChatGPT Agents"
---

# Python PyPI Package Reference Indexer

The Python PyPI Package Reference Indexer skill leverages the PyPI JSON API (GET /pypi/{project}/json) to retrieve package metadata including version history, dependency requirements, and project URLs. It fetches documentation from Read the Docs API (GET /api/v3/projects/{slug}/builds/) to locate built documentation artifacts. The skill parses reStructuredText and Sphinx-generated HTML to extract module hierarchies, function signatures with type annotations, class inheritance trees, and docstring content. It constructs a searchable index using inverted document indexing on function names, parameter types, and description keywords. Cross-reference resolution links related functions across packages by matching parameter types and return types. The skill generates markdown reference cards with import statements, minimal usage examples extracted from doctest blocks, and links to full documentation pages. Version comparison highlights API changes between releases using the PyPI release history endpoint.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/python-pypi-package-reference-indexer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/python-pypi-package-reference-indexer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-pypi-package-reference-indexer/)
