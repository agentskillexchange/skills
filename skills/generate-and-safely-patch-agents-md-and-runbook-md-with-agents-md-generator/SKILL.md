---
name: "Generate and safely patch AGENTS.md and RUNBOOK.md with AGENTS.md Generator"
slug: "generate-and-safely-patch-agents-md-and-runbook-md-with-agents-md-generator"
description: "Bootstrap and safely update AGENTS.md and RUNBOOK.md without clobbering hand-edited docs, so coding-agent repos keep a clean machine-readable contract."
github_stars: 2
verification: "listed"
source: "https://github.com/markoblogo/AGENTS.md_generator"
author: "markoblogo"
publisher_type: "individual"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "markoblogo/AGENTS.md_generator"
  github_stars: 2
---

# Generate and safely patch AGENTS.md and RUNBOOK.md with AGENTS.md Generator

Bootstrap and safely update AGENTS.md and RUNBOOK.md without clobbering hand-edited docs, so coding-agent repos keep a clean machine-readable contract.

## Prerequisites

Python 3.11+, pipx or pip, Git repository

## Installation

Use the upstream install or setup path that matches your environment:
- pip install -e ".[dev]"
- pipx install git+https://github.com/markoblogo/AGENTS.md_generator.git
- pipx uninstall agentsgen
- python -m pip install -e ".[dev]"

Requirements and caveats from upstream:
- [![Python](https://img.shields.io/badge/python-%3E%3D3.11-blue)](pyproject.toml)
- agentsgen init . --preset cli-python
- **Python library (Poetry + pytest):** [recipes/python-lib/](recipes/python-lib/)

Basic usage or getting-started notes:
- RUNBOOK.md (human-friendly command/run cheatsheet)
- sh
- python3 -m venv .venv

- Source: https://github.com/markoblogo/AGENTS.md_generator
- Extracted from upstream docs: https://raw.githubusercontent.com/markoblogo/AGENTS.md_generator/HEAD/README.md

## Documentation

- https://github.com/markoblogo/AGENTS.md_generator

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-and-safely-patch-agents-md-and-runbook-md-with-agents-md-generator/)
