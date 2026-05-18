---
name: "Enforce Python Docstring Coverage Thresholds with interrogate"
slug: "enforce-python-docstring-coverage-thresholds-with-interrogate"
description: "Measure Python docstring coverage and fail a docs-quality gate when code drops below an agreed threshold."
github_stars: 662
verification: "security_reviewed"
source: "https://github.com/econchick/interrogate"
author: "econchick"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "econchick/interrogate"
  github_stars: 662
---

# Enforce Python Docstring Coverage Thresholds with interrogate

Measure Python docstring coverage and fail a docs-quality gate when code drops below an agreed threshold.

## Prerequisites

Python, interrogate, Python source tree

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with pip, then run against your Python package with a threshold appropriate for the repository: pip install interrogate && interrogate -f 80 .
```

## Documentation

- https://interrogate.readthedocs.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-python-docstring-coverage-thresholds-with-interrogate/)
