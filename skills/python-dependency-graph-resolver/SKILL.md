---
name: "Python Dependency Graph Resolver"
description: "Resolves and visualizes Python package dependency graphs using pip, pipdeptree, and the PyPI JSON API. Detects version conflicts, circular dependencies, and vulnerable transitive dependencies."
category: "Library & API Reference"
framework: "Custom Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/python-dependency-graph-resolver/"
---

# Python Dependency Graph Resolver

Resolves and visualizes Python package dependency graphs using pip, pipdeptree, and the PyPI JSON API. Detects version conflicts, circular dependencies, and vulnerable transitive dependencies.

## Overview

The Python Dependency Graph Resolver skill provides comprehensive analysis of Python project dependency trees. It uses pipdeptree for local dependency graph extraction, pip freeze and pip check for installed package verification, and the PyPI JSON API at pypi.org/pypi/{package}/json for upstream metadata retrieval.

The resolver builds a complete dependency graph by recursively walking install_requires and extras_require metadata for each package. It detects version conflicts where two packages require incompatible versions of a shared dependency, identifies circular dependency chains, and flags packages with yanked versions on PyPI. The graph is output as both a DOT format file for Graphviz visualization and a JSON adjacency list for programmatic consumption.

Security analysis queries the PyPI JSON API for each transitive dependency to check for known vulnerabilities referenced in the project URLs and classifiers. The skill also checks package provenance by verifying PEP 740 attestations where available and comparing package hashes against the PyPI Simple API. License compatibility analysis scans classifier metadata across the full dependency tree to identify potential license conflicts between dependencies.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill python-dependency-graph-resolver
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill python-dependency-graph-resolver -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill python-dependency-graph-resolver -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill python-dependency-graph-resolver -a codex
```

### OpenClaw

```bash
clawhub install python-dependency-graph-resolver
```

## Source

- Marketplace: https://agentskillexchange.com/skills/python-dependency-graph-resolver/
