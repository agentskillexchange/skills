---
name: "Python Package Dependency Graph Mapper"
description: "Builds dependency graphs for Python packages using the PyPI JSON API and pipdeptree library. Visualizes transitive dependency chains and identifies version conflict risks."
category: "Library & API Reference"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/python-package-dependency-graph-mapper/"
---
# Python Package Dependency Graph Mapper

Builds dependency graphs for Python packages using the PyPI JSON API and pipdeptree library. Visualizes transitive dependency chains and identifies version conflict risks.

## Overview

The Python Package Dependency Graph Mapper queries the PyPI JSON API (https://pypi.org/pypi/{package}/json) to resolve package metadata and dependency specifiers, then uses the pipdeptree library to construct complete transitive dependency graphs from installed environments or requirements files. It identifies diamond dependency conflicts where two packages require incompatible versions of a shared dependency, and detects yanked package versions that may cause future installation failures. The skill generates interactive dependency visualizations using Graphviz DOT format or Mermaid diagrams suitable for documentation embedding. It calculates dependency depth metrics, identifies packages with excessive transitive dependencies (dependency bloat), and flags packages with no recent PyPI releases (potential maintenance risk). The mapper supports requirements.txt, setup.cfg, pyproject.toml, and Poetry lock file formats for comprehensive Python ecosystem coverage.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill python-package-dependency-graph-mapper
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill python-package-dependency-graph-mapper -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill python-package-dependency-graph-mapper -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill python-package-dependency-graph-mapper -a codex
```

### OpenClaw

```bash
clawhub install python-package-dependency-graph-mapper
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/python-package-dependency-graph-mapper/)
