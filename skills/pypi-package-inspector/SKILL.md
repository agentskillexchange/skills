---
name: "PyPI Package Inspector"
description: "Queries the PyPI JSON API and the libraries.io API to analyze Python package metadata, dependency trees, and version histories. Uses pip-audit for vulnerability scanning against the OSV database."
category: "Library & API Reference"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pypi-package-inspector/"
---

# PyPI Package Inspector

Queries the PyPI JSON API and the libraries.io API to analyze Python package metadata, dependency trees, and version histories. Uses pip-audit for vulnerability scanning against the OSV database.

## Overview

The PyPI Package Inspector skill provides deep analysis of Python packages through the PyPI JSON API. It retrieves package metadata including version histories, maintainer information, download statistics, and classifiers for any package hosted on PyPI.

The skill integrates with the libraries.io API for dependency tree analysis, identifying transitive dependencies and potential version conflicts. It uses pip-audit to scan packages against the Open Source Vulnerability (OSV) database, flagging known security issues.

Key features include version comparison and changelog extraction, license compatibility checking across dependency trees, and wheel availability verification for target platforms. The skill generates comprehensive package reports suitable for security reviews and dependency upgrade planning, supporting both individual package inspection and bulk analysis of requirements.txt files.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pypi-package-inspector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pypi-package-inspector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pypi-package-inspector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pypi-package-inspector -a codex
```

### OpenClaw

```bash
clawhub install pypi-package-inspector
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pypi-package-inspector/
