---
title: "Python Package Dependency Graph Mapper"
description: "The Python Package Dependency Graph Mapper queries the PyPI JSON API (https://pypi.org/pypi/{package}/json) to resolve package metadata and dependency specifiers, then uses the pipdeptree library to construct complete transitive dependency graphs from installed environments or requirements files. It identifies diamond dependency conflicts where two packages require incompatible versions of a shared dependency, and detects yanked package versions that may cause future installation failures. The skill generates interactive dependency visualizations using Graphviz DOT format or Mermaid diagrams suitable for documentation embedding. It calculates dependency depth metrics, identifies packages with excessive transitive dependencies (dependency bloat), and flags packages with no recent PyPI releases (potential maintenance risk). The mapper supports requirements.txt, setup.cfg, pyproject.toml, and Poetry lock file formats for comprehensive Python ecosystem coverage."
source: "https://agentskillexchange.com/skills/python-package-dependency-graph-mapper/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
---

# Python Package Dependency Graph Mapper

The Python Package Dependency Graph Mapper queries the PyPI JSON API (https://pypi.org/pypi/{package}/json) to resolve package metadata and dependency specifiers, then uses the pipdeptree library to construct complete transitive dependency graphs from installed environments or requirements files. It identifies diamond dependency conflicts where two packages require incompatible versions of a shared dependency, and detects yanked package versions that may cause future installation failures. The skill generates interactive dependency visualizations using Graphviz DOT format or Mermaid diagrams suitable for documentation embedding. It calculates dependency depth metrics, identifies packages with excessive transitive dependencies (dependency bloat), and flags packages with no recent PyPI releases (potential maintenance risk). The mapper supports requirements.txt, setup.cfg, pyproject.toml, and Poetry lock file formats for comprehensive Python ecosystem coverage.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-package-dependency-graph-mapper/)
