---
name: "Python PyPI Package Reference Indexer"
description: "Indexes Python package documentation using the PyPI JSON API and Read the Docs API. Builds searchable reference catalogs with function signatures, type hints, and usage examples."
category: "Library &amp; API Reference"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/python-pypi-package-reference-indexer/"
---
# Python PyPI Package Reference Indexer

Indexes Python package documentation using the PyPI JSON API and Read the Docs API. Builds searchable reference catalogs with function signatures, type hints, and usage examples.

## Overview

The Python PyPI Package Reference Indexer skill leverages the PyPI JSON API (GET /pypi/{project}/json) to retrieve package metadata including version history, dependency requirements, and project URLs. It fetches documentation from Read the Docs API (GET /api/v3/projects/{slug}/builds/) to locate built documentation artifacts. The skill parses reStructuredText and Sphinx-generated HTML to extract module hierarchies, function signatures with type annotations, class inheritance trees, and docstring content. It constructs a searchable index using inverted document indexing on function names, parameter types, and description keywords. Cross-reference resolution links related functions across packages by matching parameter types and return types. The skill generates markdown reference cards with import statements, minimal usage examples extracted from doctest blocks, and links to full documentation pages. Version comparison highlights API changes between releases using the PyPI release history endpoint.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill python-pypi-package-reference-indexer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill python-pypi-package-reference-indexer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill python-pypi-package-reference-indexer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill python-pypi-package-reference-indexer -a codex
```

### OpenClaw

```bash
clawhub install python-pypi-package-reference-indexer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-pypi-package-reference-indexer/)
