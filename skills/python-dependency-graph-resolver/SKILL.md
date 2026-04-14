---
title: "Python Dependency Graph Resolver"
description: "Resolves and visualizes Python package dependency graphs using pip, pipdeptree, and the PyPI JSON API. Detects version conflicts, circular dependencies, and vulnerable transitive dependencies."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/python-dependency-graph-resolver/"
category:
  - "Library &amp; API Reference"
framework:
  - "Custom Agents"
---

# Python Dependency Graph Resolver

The Python Dependency Graph Resolver skill provides comprehensive analysis of Python project dependency trees. It uses pipdeptree for local dependency graph extraction, pip freeze and pip check for installed package verification, and the PyPI JSON API at pypi.org/pypi/{package}/json for upstream metadata retrieval.

The resolver builds a complete dependency graph by recursively walking install_requires and extras_require metadata for each package. It detects version conflicts where two packages require incompatible versions of a shared dependency, identifies circular dependency chains, and flags packages with yanked versions on PyPI. The graph is output as both a DOT format file for Graphviz visualization and a JSON adjacency list for programmatic consumption.

Security analysis queries the PyPI JSON API for each transitive dependency to check for known vulnerabilities referenced in the project URLs and classifiers. The skill also checks package provenance by verifying PEP 740 attestations where available and comparing package hashes against the PyPI Simple API. License compatibility analysis scans classifier metadata across the full dependency tree to identify potential license conflicts between dependencies.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-dependency-graph-resolver/)
