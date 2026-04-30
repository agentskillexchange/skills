---
title: "Orchestrate stacked Git branches, sync safely, and ship pull requests in order"
description: "Uses Git Town to keep a branch stack healthy by syncing with the main branch, rebasing dependent branches in order, opening or updating pull requests, and cleaning up after merge. Best when an agent needs repeatable multi-branch workflow control instead of improvising long git command chains."
verification: "security_reviewed"
source: "https://github.com/git-town/git-town"
author: "Git Town"
publisher_type: "Open Source Project"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "git-town/git-town"
  github_stars: 3143
---

# Orchestrate stacked Git branches, sync safely, and ship pull requests in order

Uses Git Town to keep a branch stack healthy by syncing with the main branch, rebasing dependent branches in order, opening or updating pull requests, and cleaning up after merge. Best when an agent needs repeatable multi-branch workflow control instead of improvising long git command chains.

## Prerequisites

Git CLI and a Git repository

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
brew install git-town
```

## Documentation

- https://www.git-town.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/orchestrate-stacked-git-branches-sync-safely-and-ship-pull-requests-in-order/)
