---
title: "Python PyPI Package Reference Indexer"
description: "Indexes Python package documentation using the PyPI JSON API and Read the Docs API. Builds searchable reference catalogs with function signatures, type hints, and usage examples."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/python-pypi-package-reference-indexer/"
category:
  - "Library &amp; API Reference"
framework:
  - "ChatGPT Agents"
---

# Python PyPI Package Reference Indexer

The Python PyPI Package Reference Indexer skill leverages the PyPI JSON API (GET /pypi/{project}/json) to retrieve package metadata including version history, dependency requirements, and project URLs. It fetches documentation from Read the Docs API (GET /api/v3/projects/{slug}/builds/) to locate built documentation artifacts. The skill parses reStructuredText and Sphinx-generated HTML to extract module hierarchies, function signatures with type annotations, class inheritance trees, and docstring content. It constructs a searchable index using inverted document indexing on function names, parameter types, and description keywords. Cross-reference resolution links related functions across packages by matching parameter types and return types. The skill generates markdown reference cards with import statements, minimal usage examples extracted from doctest blocks, and links to full documentation pages. Version comparison highlights API changes between releases using the PyPI release history endpoint.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-pypi-package-reference-indexer/)
