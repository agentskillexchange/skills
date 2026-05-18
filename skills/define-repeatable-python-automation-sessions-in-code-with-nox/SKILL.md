---
name: "Define repeatable Python automation sessions in code with nox"
slug: "define-repeatable-python-automation-sessions-in-code-with-nox"
description: "Encode test, lint, build, and docs routines as named Python sessions so humans and agents run the same workflow every time."
github_stars: 1513
verification: "security_reviewed"
source: "https://github.com/wntrblm/nox"
author: "Alicia Ramirez"
publisher_type: "individual"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "wntrblm/nox"
  github_stars: 1513
---

# Define repeatable Python automation sessions in code with nox

Encode test, lint, build, and docs routines as named Python sessions so humans and agents run the same workflow every time.

## Prerequisites

Python environment, nox, and a repository with a versioned noxfile defining the intended automation sessions

## Installation

Use the upstream install or setup path that matches your environment:
- pipx install nox

Requirements and caveats from upstream:
- [![PyPI](https://img.shields.io/pypi/v/nox.svg?logo=python)](https://pypi.python.org/pypi/nox)
- *Flexible test automation with Python*
- nox is a command-line tool that automates testing in multiple Python environments, similar to [tox][]. Unlike tox, Nox uses a standard Python file for configuration:

Basic usage or getting-started notes:
- session.run("pytest")
- session.run("flake8", "--import-order-style", "google")
- To install Nox with [pipx][]:

- Source: https://github.com/wntrblm/nox
- Extracted from upstream docs: https://raw.githubusercontent.com/wntrblm/nox/HEAD/README.md

## Documentation

- https://nox.thea.codes/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/define-repeatable-python-automation-sessions-in-code-with-nox/)
