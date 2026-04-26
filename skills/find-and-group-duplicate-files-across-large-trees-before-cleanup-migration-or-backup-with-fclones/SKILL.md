---
title: "Find and group duplicate files across large trees before cleanup migration or backup with fclones"
description: "Scan large directory trees for duplicate or under-replicated files, then review grouped results before cleanup actions."
verification: "listed"
source: "https://github.com/pkolaczk/fclones"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pkolaczk/fclones"
  github_stars: 2707
---

# Find and group duplicate files across large trees before cleanup migration or backup with fclones

Use fclones when an agent needs a bounded dedupe workflow on a real filesystem: scan a tree, group duplicate files, and hand back reviewable groups before deletion, linking, migration, or backup cleanup. The skill is narrower than a general file manager or storage platform listing.

Invoke it instead of ad hoc shell scripting when the job is specifically duplicate-file discovery with large-tree performance and explicit review boundaries. The workflow stays operator-shaped around reporting and cleanup preparation, not broad storage administration.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/find-and-group-duplicate-files-across-large-trees-before-cleanup-migration-or-backup-with-fclones/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/find-and-group-duplicate-files-across-large-trees-before-cleanup-migration-or-backup-with-fclones
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/find-and-group-duplicate-files-across-large-trees-before-cleanup-migration-or-backup-with-fclones`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-and-group-duplicate-files-across-large-trees-before-cleanup-migration-or-backup-with-fclones/)
