---
title: "PyPI Package Inspector"
description: "The PyPI Package Inspector skill provides deep analysis of Python packages through the PyPI JSON API. It retrieves package metadata including version histories, maintainer information, download statistics, and classifiers for any package hosted on PyPI. The skill integrates with the libraries.io API for dependency tree analysis, identifying transitive dependencies and potential version conflicts. It uses pip-audit to scan packages against the Open Source Vulnerability (OSV) database, flagging known security issues. Key features include version comparison and changelog extraction, license compatibility checking across dependency trees, and wheel availability verification for target platforms. The skill generates comprehensive package reports suitable for security reviews and dependency upgrade planning, supporting both individual package inspection and bulk analysis of requirements.txt files."
source: "https://agentskillexchange.com/skills/pypi-package-inspector/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Gemini"
---

# PyPI Package Inspector

The PyPI Package Inspector skill provides deep analysis of Python packages through the PyPI JSON API. It retrieves package metadata including version histories, maintainer information, download statistics, and classifiers for any package hosted on PyPI. The skill integrates with the libraries.io API for dependency tree analysis, identifying transitive dependencies and potential version conflicts. It uses pip-audit to scan packages against the Open Source Vulnerability (OSV) database, flagging known security issues. Key features include version comparison and changelog extraction, license compatibility checking across dependency trees, and wheel availability verification for target platforms. The skill generates comprehensive package reports suitable for security reviews and dependency upgrade planning, supporting both individual package inspection and bulk analysis of requirements.txt files.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pypi-package-inspector/)
