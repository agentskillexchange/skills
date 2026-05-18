---
name: "Simplify recently changed code and open low-risk refactor pull requests"
slug: "simplify-recently-changed-code-and-open-low-risk-refactor-pull-requests"
description: "This entry turns GitHub Next's Code Simplifier workflow into a narrow cleanup agent. The agent inspects code changed in the last day, proposes behavior-preserving simplifications, runs validation, and opens small refactor pull requests instead of attempting broad rewrites."
verification: "security_reviewed"
source: "https://github.com/githubnext/agentics/blob/main/docs/code-simplifier.md"
author: "GitHub Next"
publisher_type: "Open Source Project"
category: "Code Quality & Review"
framework: "Multi-Framework"
---

# Simplify recently changed code and open low-risk refactor pull requests

This entry turns GitHub Next's Code Simplifier workflow into a narrow cleanup agent. The agent inspects code changed in the last day, proposes behavior-preserving simplifications, runs validation, and opens small refactor pull requests instead of attempting broad rewrites.

## Prerequisites

GitHub CLI, the gh-aw extension, and repository CI or tests for validation

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
gh extension install github/gh-aw && gh aw add-wizard githubnext/agentics/code-simplifier
```

## Documentation

- https://github.com/githubnext/agentics/blob/main/docs/code-simplifier.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/simplify-recently-changed-code-and-open-low-risk-refactor-pull-requests/)
