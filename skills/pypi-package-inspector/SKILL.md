---
title: "PyPI Package Inspector"
description: "Queries the PyPI JSON API and the libraries.io API to analyze Python package metadata, dependency trees, and version histories. Uses pip-audit for vulnerability scanning against the OSV database."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pypi-package-inspector/"
category:
  - "Library &amp; API Reference"
framework:
  - "Gemini"
---

# PyPI Package Inspector

The PyPI Package Inspector skill provides deep analysis of Python packages through the PyPI JSON API. It retrieves package metadata including version histories, maintainer information, download statistics, and classifiers for any package hosted on PyPI.

The skill integrates with the libraries.io API for dependency tree analysis, identifying transitive dependencies and potential version conflicts. It uses pip-audit to scan packages against the Open Source Vulnerability (OSV) database, flagging known security issues.

Key features include version comparison and changelog extraction, license compatibility checking across dependency trees, and wheel availability verification for target platforms. The skill generates comprehensive package reports suitable for security reviews and dependency upgrade planning, supporting both individual package inspection and bulk analysis of requirements.txt files.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pypi-package-inspector/)
