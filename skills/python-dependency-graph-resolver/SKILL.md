---
title: "Python Dependency Graph Resolver"
description: "The Python Dependency Graph Resolver skill provides comprehensive analysis of Python project dependency trees. It uses pipdeptree for local dependency graph extraction, pip freeze and pip check for installed package verification, and the PyPI JSON API at pypi.org/pypi/{package}/json for upstream metadata retrieval.\nThe resolver builds a complete dependency graph by recursively walking install_requires and extras_require metadata for each package. It detects version conflicts where two packages require incompatible versions of a shared dependency, identifies circular dependency chains, and flags packages with yanked versions on PyPI. The graph is output as both a DOT format file for Graphviz visualization and a JSON adjacency list for programmatic consumption.\nSecurity analysis queries the PyPI JSON API for each transitive dependency to check for known vulnerabilities referenced in the project URLs and classifiers. The skill also checks package provenance by verifying PEP 740 attestations where available and comparing package hashes against the PyPI Simple API. License compatibility analysis scans classifier metadata across the full dependency tree to identify potential license conflicts between dependencies."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/python-dependency-graph-resolver/"
framework:
  - "Custom Agents"
---

# Python Dependency Graph Resolver

The Python Dependency Graph Resolver skill provides comprehensive analysis of Python project dependency trees. It uses pipdeptree for local dependency graph extraction, pip freeze and pip check for installed package verification, and the PyPI JSON API at pypi.org/pypi/{package}/json for upstream metadata retrieval.
The resolver builds a complete dependency graph by recursively walking install_requires and extras_require metadata for each package. It detects version conflicts where two packages require incompatible versions of a shared dependency, identifies circular dependency chains, and flags packages with yanked versions on PyPI. The graph is output as both a DOT format file for Graphviz visualization and a JSON adjacency list for programmatic consumption.
Security analysis queries the PyPI JSON API for each transitive dependency to check for known vulnerabilities referenced in the project URLs and classifiers. The skill also checks package provenance by verifying PEP 740 attestations where available and comparing package hashes against the PyPI Simple API. License compatibility analysis scans classifier metadata across the full dependency tree to identify potential license conflicts between dependencies.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/python-dependency-graph-resolver
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/python-dependency-graph-resolver` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-dependency-graph-resolver/)
