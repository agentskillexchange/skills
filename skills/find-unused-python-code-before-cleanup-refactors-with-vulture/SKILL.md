---
title: "Find unused Python code before cleanup refactors with Vulture"
slug: "find-unused-python-code-before-cleanup-refactors-with-vulture"
description: "Run a dead-code pass on Python repositories before refactors so agents can flag unused functions, classes, imports, and variables instead of deleting blindly."
github_stars: 4521
verification: "security_reviewed"
source: "https://github.com/jendrikseipp/vulture"
author: "jendrikseipp"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "jendrikseipp/vulture"
  github_stars: 4521
---

# Find unused Python code before cleanup refactors with Vulture

Run a dead-code pass on Python repositories before refactors so agents can flag unused functions, classes, imports, and variables instead of deleting blindly.

## Prerequisites

Python 3, pip, Vulture CLI

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install vulture`, then run `vulture path/to/repo` and review the reported unused code before making cleanup edits.
```

## Documentation

- https://github.com/jendrikseipp/vulture

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-unused-python-code-before-cleanup-refactors-with-vulture/)
