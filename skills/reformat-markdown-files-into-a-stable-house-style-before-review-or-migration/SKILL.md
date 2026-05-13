---
title: "Reformat Markdown files into a stable house style before review or migration"
slug: "reformat-markdown-files-into-a-stable-house-style-before-review-or-migration"
description: "Runs mdformat to rewrite Markdown into a consistent CommonMark-oriented layout or check mode in CI. Use it when an agent needs deterministic Markdown diffs before review, migration, or bulk cleanup, not when it needs to generate new content or build a docs site."
github_stars: 758
verification: "security_reviewed"
source: "https://github.com/hukkin/mdformat"
author: "Taneli Hukkinen"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "hukkin/mdformat"
  github_stars: 758
---

# Reformat Markdown files into a stable house style before review or migration

Runs mdformat to rewrite Markdown into a consistent CommonMark-oriented layout or check mode in CI. Use it when an agent needs deterministic Markdown diffs before review, migration, or bulk cleanup, not when it needs to generate new content or build a docs site.

## Prerequisites

Python 3, pipx or pip, command line

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pipx install mdformat
```

## Documentation

- https://mdformat.readthedocs.io/en/stable/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reformat-markdown-files-into-a-stable-house-style-before-review-or-migration/)
