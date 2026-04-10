---
title: "Python Package Dependency Graph Mapper"
description: "Builds dependency graphs for Python packages using the PyPI JSON API and pipdeptree library. Visualizes transitive dependency chains and identifies version conflict risks."
slug: "python-package-dependency-graph-mapper"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/python-package-dependency-graph-mapper/"
listed: true
---

# Python Package Dependency Graph Mapper

Builds dependency graphs for Python packages using the PyPI JSON API and pipdeptree library. Visualizes transitive dependency chains and identifies version conflict risks.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install python-package-dependency-graph-mapper
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Python Package Dependency Graph Mapper queries the PyPI JSON API (https://pypi.org/pypi/{package}/json) to resolve package metadata and dependency specifiers, then uses the pipdeptree library to construct complete transitive dependency graphs from installed environments or requirements files. It identifies diamond dependency conflicts where two packages require incompatible versions of a shared dependency, and detects yanked package versions that may cause future installation failures. The skill generates interactive dependency visualizations using Graphviz DOT format or Mermaid diagrams suitable for documentation embedding. It calculates dependency depth metrics, identifies packages with excessive transitive dependencies (dependency bloat), and flags packages with no recent PyPI releases (potential maintenance risk). The mapper supports requirements.txt, setup.cfg, pyproject.toml, and Poetry lock file formats for comprehensive Python ecosystem coverage.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-package-dependency-graph-mapper/)
