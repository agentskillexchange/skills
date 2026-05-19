---
name: "Audit Python dependency declarations for unused, missing, and transitive imports before release"
slug: "audit-python-dependency-declarations-before-release"
description: "Use Deptry when an agent needs to verify that a Python project's declared dependencies still match the imports the code actually uses. The agent scans the codebase, flags unused direct dependencies, missing declarations, and transitive imports that only work by accident, then turns the findings into cleanup commits or release blockers."
github_stars: 1359
verification: "security_reviewed"
source: "https://github.com/osprey-oss/deptry"
author: "Osprey OSS"
publisher_type: "Open Source Project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "osprey-oss/deptry"
  github_stars: 1359
---

# Audit Python dependency declarations for unused, missing, and transitive imports before release

Use Deptry when an agent needs to verify that a Python project's declared dependencies still match the imports the code actually uses. The agent scans the codebase, flags unused direct dependencies, missing declarations, and transitive imports that only work by accident, then turns the findings into cleanup commits or release blockers.

## Prerequisites

Python plus Deptry configured against the target repository

## Installation

Use the upstream install or setup path that matches your environment:
- uv add --dev deptry
- pip install deptry

Requirements and caveats from upstream:
- [![Supported Python versions](https://img.shields.io/pypi/pyversions/deptry)](https://pypi.org/project/deptry/)
- _deptry_ is a command line tool to check for issues with dependencies in a Python project, such as unused or missing
- using [Poetry](https://python-poetry.org/), [pip](https://pip.pypa.io/), [PDM](https://pdm-project.org/), [uv](https://docs.astral.sh/uv/),

Basic usage or getting-started notes:
- To add _deptry_ to your project, run one of the following commands:
- shell
- poetry add --dev deptry

- Source: https://github.com/osprey-oss/deptry
- Extracted from upstream docs: https://raw.githubusercontent.com/osprey-oss/deptry/HEAD/README.md

## Documentation

- https://deptry.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-python-dependency-declarations-before-release/)
