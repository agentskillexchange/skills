---
title: "Enforce source-controlled AI checks in CI before merging risky changes with Continue CLI"
description: "Lets an agent define repo-native AI review checks as markdown files and run them as repeatable pull request status checks in CI."
verification: "security_reviewed"
source: "https://github.com/continuedev/continue"
author: "Continue Dev"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "continuedev/continue"
  github_stars: 32622
---

# Enforce source-controlled AI checks in CI before merging risky changes with Continue CLI

Lets an agent define repo-native AI review checks as markdown files and run them as repeatable pull request status checks in CI.

## Prerequisites

Continue CLI, GitHub or CI system, repository checkout

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Continue CLI with curl or npm, then define checks in .continue/checks/ and run them in CI.
```

## Documentation

- https://docs.continue.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-source-controlled-ai-checks-in-ci-before-merging-risky-changes-with-continue-cli/)
