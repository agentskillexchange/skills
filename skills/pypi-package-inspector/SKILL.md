---
title: "PyPI Package Inspector"
description: "Queries the PyPI JSON API and the libraries.io API to analyze Python package metadata, dependency trees, and version histories. Uses pip-audit for vulnerability scanning against the OSV database."
verification: "security_reviewed"
source: "https://pypi.org/"
category:
  - "Library & API Reference"
framework:
  - "Gemini"
---

# PyPI Package Inspector

The PyPI Package Inspector skill provides deep analysis of Python packages through the PyPI JSON API. It retrieves package metadata including version histories, maintainer information, download statistics, and classifiers for any package hosted on PyPI.

The skill integrates with the libraries.io API for dependency tree analysis, identifying transitive dependencies and potential version conflicts. It uses pip-audit to scan packages against the Open Source Vulnerability (OSV) database, flagging known security issues.

Key features include version comparison and changelog extraction, license compatibility checking across dependency trees, and wheel availability verification for target platforms. The skill generates comprehensive package reports suitable for security reviews and dependency upgrade planning, supporting both individual package inspection and bulk analysis of requirements.txt files.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/pypi-package-inspector/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pypi-package-inspector
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/pypi-package-inspector`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pypi-package-inspector/)
