---
title: "Map Python import graphs to explain coupling before refactors or package splits with pydeps"
description: "Generate Python module dependency graphs so refactors and package splits start from an actual import map instead of guesswork."
verification: "listed"
source: "https://github.com/thebjorn/pydeps"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "thebjorn/pydeps"
  github_stars: 2076
---

# Map Python import graphs to explain coupling before refactors or package splits with pydeps

Use pydeps when an agent needs to inspect how Python modules depend on each other before a refactor, extraction, or architecture review. It is most useful when the real task is to surface import cycles, noisy coupling, or hidden dependency paths and hand back a graph or dependency report. This is not just a package listing because the boundary is a specific analysis workflow: run dependency discovery against a target package, tune scope and noise, and produce a graph that explains coupling. That is a concrete operator task with a clear before-and-after artifact.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/map-python-import-graphs-to-explain-coupling-before-refactors-or-package-splits-with-pydeps/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/map-python-import-graphs-to-explain-coupling-before-refactors-or-package-splits-with-pydeps
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/map-python-import-graphs-to-explain-coupling-before-refactors-or-package-splits-with-pydeps`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/map-python-import-graphs-to-explain-coupling-before-refactors-or-package-splits-with-pydeps/)
