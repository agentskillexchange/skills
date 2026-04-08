---
title: Python PyPI Package Reference Indexer
description: The Python PyPI Package Reference Indexer skill leverages the PyPI JSON
  API (GET /pypi/{project}/json) to retrieve package metadata including version history,
  dependency requirements, and project URLs. It fetches documentation from Read the
  Docs API (GET /api/v3/projects/{slug}/builds/) to locate built documentation artifacts.
  The skill parses reStructuredText and Sphinx-generated HTML to extract module hierarchies,
  function signatures with type annotations, class inheritance trees, and docstring
  content. It constructs a searchable index using inverted document indexing on function
  names, parameter types, and description keywords. Cross-reference resolution links
  related functions across packages by matching parameter types and return types.
  The skill generates markdown reference cards with import statements, minimal usage
  examples extracted from doctest blocks, and links to full documentation pages. Version
  comparison highlights API changes between releases using the PyPI release history
  endpoint.
verification: security_reviewed
source: https://agentskillexchange.com/skills/python-pypi-package-reference-indexer/
category:
- Library &amp; API Reference
framework:
- ChatGPT Agents
---

# Python PyPI Package Reference Indexer

The Python PyPI Package Reference Indexer skill leverages the PyPI JSON API (GET /pypi/{project}/json) to retrieve package metadata including version history, dependency requirements, and project URLs. It fetches documentation from Read the Docs API (GET /api/v3/projects/{slug}/builds/) to locate built documentation artifacts. The skill parses reStructuredText and Sphinx-generated HTML to extract module hierarchies, function signatures with type annotations, class inheritance trees, and docstring content. It constructs a searchable index using inverted document indexing on function names, parameter types, and description keywords. Cross-reference resolution links related functions across packages by matching parameter types and return types. The skill generates markdown reference cards with import statements, minimal usage examples extracted from doctest blocks, and links to full documentation pages. Version comparison highlights API changes between releases using the PyPI release history endpoint.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-pypi-package-reference-indexer/)
