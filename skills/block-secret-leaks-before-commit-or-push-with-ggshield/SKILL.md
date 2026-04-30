---
title: "Block secret leaks before commit or push with ggshield"
description: "Scan staged changes, commits, or repositories for secrets before they leave the workstation or CI job, instead of relying on a later platform-side catch."
verification: "listed"
source: "https://github.com/GitGuardian/ggshield"
author: "GitGuardian"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "GitGuardian/ggshield"
  github_stars: 1940
---

# Block secret leaks before commit or push with ggshield

Scan staged changes, commits, or repositories for secrets before they leave the workstation or CI job, instead of relying on a later platform-side catch.

## Prerequisites

Python environment or packaged ggshield install, Git, optional GitGuardian API key for full detector coverage

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install ggshield with pipx, pip, or Homebrew, optionally run `ggshield auth login` or set a GitGuardian API key, then invoke checks such as `ggshield secret scan pre-commit`, `ggshield secret scan pre-push`, or `ggshield secret scan repo`.
```

## Documentation

- https://github.com/GitGuardian/ggshield#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/block-secret-leaks-before-commit-or-push-with-ggshield/)
