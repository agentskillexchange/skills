---
title: "Back up and restore an OpenClaw workspace to Synology NAS with verification and rollback safety using Synology Backup"
slug: "back-up-and-restore-an-openclaw-workspace-to-synology-nas-with-verification-and-rollback-safety-using-synology-backup"
description: "Protect an OpenClaw workspace with repeatable Synology NAS backups, integrity checks, and safer restores instead of ad hoc file copying."
verification: "security_reviewed"
source: "https://github.com/pfrederiksen/synology-backup"
author: "pfrederiksen"
publisher_type: "individual"
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "pfrederiksen/synology-backup"
  github_stars: 1
---

# Back up and restore an OpenClaw workspace to Synology NAS with verification and rollback safety using Synology Backup

Protect an OpenClaw workspace with repeatable Synology NAS backups, integrity checks, and safer restores instead of ad hoc file copying.

## Prerequisites

OpenClaw, Synology NAS, SMB or SSH/rsync connectivity, rsync and optionally cifs-utils, backup credentials or SSH keys

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `clawhub install synology-backup`, install the documented system dependencies such as rsync and optionally cifs-utils, create the Synology backup config and credentials described in the README, then test with the dry-run backup flow before scheduling live backups.
```

## Documentation

- https://github.com/pfrederiksen/synology-backup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/back-up-and-restore-an-openclaw-workspace-to-synology-nas-with-verification-and-rollback-safety-using-synology-backup/)
