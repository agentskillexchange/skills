---
title: "Format shell scripts into a stable house style before review with shfmt"
slug: "format-shell-scripts-into-a-stable-house-style-before-review-with-shfmt"
description: "Normalize Bash, POSIX shell, and Zsh scripts before review or CI so style noise stops hiding the real changes."
github_stars: 8700
verification: "security_reviewed"
source: "https://github.com/mvdan/sh"
author: "mvdan"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "mvdan/sh"
  github_stars: 8700
---

# Format shell scripts into a stable house style before review with shfmt

Normalize Bash, POSIX shell, and Zsh scripts before review or CI so style noise stops hiding the real changes.

## Prerequisites

Go or packaged shfmt binary, shell script files, optional CI or pre-commit integration

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install shfmt from the upstream Go, package manager, or container instructions, then run it against target shell files such as `shfmt -w script.sh` or in batch across a repository.
```

## Documentation

- https://pkg.go.dev/mvdan.cc/sh/v3

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/format-shell-scripts-into-a-stable-house-style-before-review-with-shfmt/)
