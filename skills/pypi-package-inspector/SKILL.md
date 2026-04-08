---
title: PyPI Package Inspector
description: The PyPI Package Inspector skill provides deep analysis of Python packages
  through the PyPI JSON API. It retrieves package metadata including version histories,
  maintainer information, download statistics, and classifiers for any package hosted
  on PyPI. The skill integrates with the libraries.io API for dependency tree analysis,
  identifying transitive dependencies and potential version conflicts. It uses pip-audit
  to scan packages against the Open Source Vulnerability (OSV) database, flagging
  known security issues. Key features include version comparison and changelog extraction,
  license compatibility checking across dependency trees, and wheel availability verification
  for target platforms. The skill generates comprehensive package reports suitable
  for security reviews and dependency upgrade planning, supporting both individual
  package inspection and bulk analysis of requirements.txt files.
verification: security_reviewed
source: https://agentskillexchange.com/skills/pypi-package-inspector/
category:
- Library &amp; API Reference
framework:
- Gemini
---

# PyPI Package Inspector

The PyPI Package Inspector skill provides deep analysis of Python packages through the PyPI JSON API. It retrieves package metadata including version histories, maintainer information, download statistics, and classifiers for any package hosted on PyPI. The skill integrates with the libraries.io API for dependency tree analysis, identifying transitive dependencies and potential version conflicts. It uses pip-audit to scan packages against the Open Source Vulnerability (OSV) database, flagging known security issues. Key features include version comparison and changelog extraction, license compatibility checking across dependency trees, and wheel availability verification for target platforms. The skill generates comprehensive package reports suitable for security reviews and dependency upgrade planning, supporting both individual package inspection and bulk analysis of requirements.txt files.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pypi-package-inspector/)
