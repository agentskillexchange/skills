---
title: "Find and group duplicate files across large trees before cleanup migration or backup with fclones"
description: "Scan large directory trees for duplicate or under-replicated files, then review grouped results before cleanup actions."
verification: listed
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/find-and-group-duplicate-files-across-large-trees-before-cleanup-migration-or-backup-with-fclones
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/find-and-group-duplicate-files-across-large-trees-before-cleanup-migration-or-backup-with-fclones` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/find-and-group-duplicate-files-across-large-trees-before-cleanup-migration-or-backup-with-fclones/)
