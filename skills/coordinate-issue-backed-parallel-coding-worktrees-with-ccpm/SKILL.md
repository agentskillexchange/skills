---
title: "Coordinate issue-backed parallel coding worktrees with CCPM"
description: "Use CCPM when an agent team needs one issue-backed workflow that turns plans into GitHub issues, isolates execution in worktrees, and keeps parallel coding runs reviewable instead of relying on ad hoc chat memory."
verification: "security_reviewed"
source: "https://github.com/automazeio/ccpm"
author: "automazeio"
publisher_type: "company"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "automazeio/ccpm"
  github_stars: 7995
---

# Coordinate issue-backed parallel coding worktrees with CCPM

Use CCPM when an agent team needs one issue-backed workflow that turns plans into GitHub issues, isolates execution in worktrees, and keeps parallel coding runs reviewable instead of relying on ad hoc chat memory.

## Prerequisites

GitHub Issues, git worktrees, a repo using an agent-skills-compatible coding harness, and an operator willing to manage work through issue-backed phases instead of ad hoc chat.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install CCPM from the GitHub repo or supported agent-skills harness, connect it to a repository with GitHub Issues enabled, generate or refine the project plan into issues, then let each issue run in its own worktree so agent execution and review stay isolated and traceable.
```

## Documentation

- https://github.com/automazeio/ccpm

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/coordinate-issue-backed-parallel-coding-worktrees-with-ccpm/)
