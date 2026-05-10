---
title: "Automatically rerun flaky pytest cases with bounded retry rules before intermittent failures block merges with pytest-rerunfailures"
slug: "automatically-rerun-flaky-pytest-cases-with-bounded-retry-rules-before-intermittent-failures-block-merges-with-pytest-rerunfailures"
description: "Add controlled retries to pytest runs so agents can contain flaky tests and report final failures without rerunning whole suites by hand."
github_stars: 458
verification: "security_reviewed"
source: "https://github.com/pytest-dev/pytest-rerunfailures"
author: "pytest-dev"
publisher_type: "organization"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "pytest-dev/pytest-rerunfailures"
  github_stars: 458
  npm_package: "pytest-rerunfailures"
---

# Automatically rerun flaky pytest cases with bounded retry rules before intermittent failures block merges with pytest-rerunfailures

Add controlled retries to pytest runs so agents can contain flaky tests and report final failures without rerunning whole suites by hand.

## Prerequisites

Python, pytest, and the pytest-rerunfailures plugin

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install pytest-rerunfailures`, then run pytest with retry flags such as `--reruns` and optional delay settings, or add the plugin configuration to your existing pytest and CI setup.
```

## Documentation

- https://pytest-rerunfailures.readthedocs.io/stable/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/automatically-rerun-flaky-pytest-cases-with-bounded-retry-rules-before-intermittent-failures-block-merges-with-pytest-rerunfailures/)
