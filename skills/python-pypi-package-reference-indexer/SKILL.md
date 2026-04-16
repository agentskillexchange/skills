---
title: "Python PyPI Package Reference Indexer"
description: "Indexes Python package documentation using the PyPI JSON API and Read the Docs API. Builds searchable reference catalogs with function signatures, type hints, and usage examples."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/python-pypi-package-reference-indexer/"
category:
  - "Library &amp; API Reference"
framework:
  - "ChatGPT Agents"
---

# Python PyPI Package Reference Indexer

The Python PyPI Package Reference Indexer skill leverages the PyPI JSON API (GET /pypi/{project}/json) to retrieve package metadata including version history, dependency requirements, and project URLs. It fetches documentation from Read the Docs API (GET /api/v3/projects/{slug}/builds/) to locate built documentation artifacts. The skill parses reStructuredText and Sphinx-generated HTML to extract module hierarchies, function signatures with type annotations, class inheritance trees, and docstring content. It constructs a searchable index using inverted document indexing on function names, parameter types, and description keywords. Cross-reference resolution links related functions across packages by matching parameter types and return types. The skill generates markdown reference cards with import statements, minimal usage examples extracted from doctest blocks, and links to full documentation pages. Version comparison highlights API changes between releases using the PyPI release history endpoint.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-pypi-package-reference-indexer/)
