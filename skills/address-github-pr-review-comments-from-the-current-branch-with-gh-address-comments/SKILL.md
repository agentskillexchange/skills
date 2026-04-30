---
title: "Address GitHub PR review comments from the current branch with gh-address-comments"
description: "Find the open PR for the current branch, gather unresolved review comments, and drive a focused comment-resolution workflow with gh-authenticated context."
verification: "listed"
source: "https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments"
author: "OpenAI"
publisher_type: "organization"
category:
  - "Code Quality & Review"
framework:
  - "Codex"
---

# Address GitHub PR review comments from the current branch with gh-address-comments

Find the open PR for the current branch, gather unresolved review comments, and drive a focused comment-resolution workflow with gh-authenticated context.

## Prerequisites

Codex, GitHub CLI (gh), repository with an open PR, GitHub auth

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Use the curated gh-address-comments skill from the openai/skills catalog, ensure `gh auth status` works in the repository, then run it on the current branch so it can fetch the PR's unresolved comments and guide the selected fixes.
```

## Documentation

- https://raw.githubusercontent.com/openai/skills/main/skills/.curated/gh-address-comments/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/address-github-pr-review-comments-from-the-current-branch-with-gh-address-comments/)
