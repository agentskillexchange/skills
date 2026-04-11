---
title: "Fix failing pull requests by analyzing CI errors and pushing targeted repairs"
description: "Use GitHub Next’s pr-fix workflow when a pull request is blocked on failing checks and the likely repair is machine-doable. The agent inspects CI failures, traces the root cause, applies a focused fix on the PR branch, and leaves the result in reviewable Git history."
verification: "listed"
source: "https://github.com/githubnext/agentics/blob/main/docs/pr-fix.md"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
---

# Fix failing pull requests by analyzing CI errors and pushing targeted repairs

Use GitHub Next’s pr-fix workflow when a pull request is blocked on failing checks and the likely repair is machine-doable. The agent inspects CI failures, traces the root cause, applies a focused fix on the PR branch, and leaves the result in reviewable Git history.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fix-failing-pull-requests-by-analyzing-ci-errors-and-pushing-targeted-repairs/)
