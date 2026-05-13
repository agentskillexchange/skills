---
title: "Run one formatter plan across a mixed-language repo and keep generated edits predictable with treefmt"
slug: "run-one-formatter-plan-across-a-mixed-language-repo-and-keep-generated-edits-predictable-with-treefmt"
description: "Use treefmt when an agent needs one repo-level formatting plan across multiple languages instead of stitching formatter commands together ad hoc."
github_stars: 977
verification: "security_reviewed"
source: "https://github.com/numtide/treefmt"
author: "Numtide"
publisher_type: "company"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "numtide/treefmt"
  github_stars: 977
  npm_package: "treefmt"
  npm_weekly_downloads: 18627
---

# Run one formatter plan across a mixed-language repo and keep generated edits predictable with treefmt

Use treefmt when an agent needs one repo-level formatting plan across multiple languages instead of stitching formatter commands together ad hoc.

## Prerequisites

treefmt, the underlying language formatters you plan to invoke, a repository-level treefmt configuration file, and shell access.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install treefmt with the method documented by the project, add a treefmt configuration file that points at the language formatters your repo uses, install those formatter binaries, then run treefmt over the repository in local or CI workflows.
```

## Documentation

- https://treefmt.com/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-one-formatter-plan-across-a-mixed-language-repo-and-keep-generated-edits-predictable-with-treefmt/)
