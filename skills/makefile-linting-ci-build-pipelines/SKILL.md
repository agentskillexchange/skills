---
title: "Makefile Linting for CI and Build Pipelines"
slug: "makefile-linting-ci-build-pipelines"
description: "Uses checkmake to inspect Makefiles for style issues, fragile targets, and maintainability problems before build automation breaks in CI. It is a narrow build-script review skill for agents working inside repositories that already rely on make, not a generic build tool listing."
github_stars: 1188
verification: "security_reviewed"
source: "https://github.com/checkmake/checkmake"
author: "checkmake maintainers"
publisher_type: "Open Source Project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "checkmake/checkmake"
  github_stars: 1188
---

# Makefile Linting for CI and Build Pipelines

Uses checkmake to inspect Makefiles for style issues, fragile targets, and maintainability problems before build automation breaks in CI. It is a narrow build-script review skill for agents working inside repositories that already rely on make, not a generic build tool listing.

## Prerequisites

checkmake binary and existing Makefiles

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install checkmake from the project releases or package manager for your platform
```

## Documentation

- https://github.com/checkmake/checkmake

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/makefile-linting-ci-build-pipelines/)
