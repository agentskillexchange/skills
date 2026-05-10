---
title: "Find and group duplicate files across large trees before cleanup migration or backup with fclones"
slug: "find-and-group-duplicate-files-across-large-trees-before-cleanup-migration-or-backup-with-fclones"
description: "Scan large directory trees for duplicate or under-replicated files, then review grouped results before cleanup actions."
github_stars: 2707
verification: "security_reviewed"
source: "https://github.com/pkolaczk/fclones"
author: "pkolaczk"
publisher_type: "individual"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "pkolaczk/fclones"
  github_stars: 2707
---

# Find and group duplicate files across large trees before cleanup migration or backup with fclones

Scan large directory trees for duplicate or under-replicated files, then review grouped results before cleanup actions.

## Prerequisites

fclones CLI and access to the directory trees being audited

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install from crates.io with `cargo install fclones` or use the project release binaries, then run `fclones group <path>` to produce reviewable duplicate groups before any cleanup action.
```

## Documentation

- https://github.com/pkolaczk/fclones

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-and-group-duplicate-files-across-large-trees-before-cleanup-migration-or-backup-with-fclones/)
