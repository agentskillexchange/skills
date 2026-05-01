---
title: "Run profile-based restic backups and verification checks with resticprofile"
description: "Execute named restic backup profiles with repeatable backup, retention, prune, check, and restore steps instead of hand-running one-off commands."
verification: "listed"
source: "https://github.com/creativeprojects/resticprofile"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "creativeprojects/resticprofile"
  github_stars: 1275
---

# Run profile-based restic backups and verification checks with resticprofile

Use resticprofile when an agent needs to run a repeatable backup runbook around restic using named profiles for backup, retention, prune, check, or restore operations. The agent can select the right profile, execute the matching workflow, and report the outcome without rebuilding the command set from scratch each time. The boundary is profile-driven restic operations and verification, not a generic backup platform or broad storage product listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-profile-based-restic-backups-and-verification-checks-with-resticprofile/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-profile-based-restic-backups-and-verification-checks-with-resticprofile
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-profile-based-restic-backups-and-verification-checks-with-resticprofile`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-profile-based-restic-backups-and-verification-checks-with-resticprofile/)
