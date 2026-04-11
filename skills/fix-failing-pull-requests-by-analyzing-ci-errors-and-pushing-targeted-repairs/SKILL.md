---
title: "Fix failing pull requests by analyzing CI errors and pushing targeted repairs"
description: "Use GitHub Next’s pr-fix workflow when a pull request is blocked on failing checks and the likely repair is machine-doable. The agent inspects CI failures, traces the root cause, applies a focused fix on the PR branch, and leaves the result in reviewable Git history."
slug: fix-failing-pull-requests-by-analyzing-ci-errors-and-pushing-targeted-repairs
verification: listed
source: "https://github.com/githubnext/agentics/blob/main/docs/pr-fix.md"
category:
- "Runbooks & Diagnostics"
framework:
- "Multi-Framework"
---
# Fix failing pull requests by analyzing CI errors and pushing targeted repairs

Use GitHub Next’s pr-fix workflow when a pull request is blocked on failing checks and the likely repair is machine-doable. The agent inspects CI failures, traces the root cause, applies a focused fix on the PR branch, and leaves the result in reviewable Git history.

## Installation

You can install this skill in any of these ways:

1. Browse and install from Agent Skill Exchange.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule in your skills workspace.
4. Install it with your preferred agent skill or package manager if your setup supports that.
5. Copy the `SKILL.md` into an existing skill folder and adapt any referenced assets as needed.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fix-failing-pull-requests-by-analyzing-ci-errors-and-pushing-targeted-repairs/)
