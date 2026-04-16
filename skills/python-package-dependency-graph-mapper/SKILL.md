---
title: "Python Package Dependency Graph Mapper"
description: "Builds dependency graphs for Python packages using the PyPI JSON API and pipdeptree library. Visualizes transitive dependency chains and identifies version conflict risks."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/python-package-dependency-graph-mapper/"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
---

# Python Package Dependency Graph Mapper

The Python Package Dependency Graph Mapper queries the PyPI JSON API (https://pypi.org/pypi/{package}/json) to resolve package metadata and dependency specifiers, then uses the pipdeptree library to construct complete transitive dependency graphs from installed environments or requirements files. It identifies diamond dependency conflicts where two packages require incompatible versions of a shared dependency, and detects yanked package versions that may cause future installation failures. The skill generates interactive dependency visualizations using Graphviz DOT format or Mermaid diagrams suitable for documentation embedding. It calculates dependency depth metrics, identifies packages with excessive transitive dependencies (dependency bloat), and flags packages with no recent PyPI releases (potential maintenance risk). The mapper supports requirements.txt, setup.cfg, pyproject.toml, and Poetry lock file formats for comprehensive Python ecosystem coverage.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-package-dependency-graph-mapper/)
