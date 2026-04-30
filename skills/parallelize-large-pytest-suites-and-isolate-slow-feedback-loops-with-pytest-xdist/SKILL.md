---
title: "Parallelize large pytest suites and isolate slow feedback loops with pytest-xdist"
description: "Fan out Python test execution across workers so slow suites finish faster and bottlenecks show up before they dominate CI time."
verification: "listed"
source: "https://github.com/pytest-dev/pytest-xdist"
author: "pytest-dev"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "pytest-dev/pytest-xdist"
  github_stars: 1832
---

# Parallelize large pytest suites and isolate slow feedback loops with pytest-xdist

Fan out Python test execution across workers so slow suites finish faster and bottlenecks show up before they dominate CI time.

## Prerequisites

Python environment, pytest, pytest-xdist, and a pytest-compatible test suite with enough local or CI worker capacity to parallelize

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install pytest-xdist into the same environment as pytest, then run the target suite with an xdist worker option such as -n auto or another documented distribution mode in local or CI execution.
```

## Documentation

- https://pytest-xdist.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parallelize-large-pytest-suites-and-isolate-slow-feedback-loops-with-pytest-xdist/)
