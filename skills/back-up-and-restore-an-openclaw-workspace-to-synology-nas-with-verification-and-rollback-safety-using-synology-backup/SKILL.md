---
name: "Back up and restore an OpenClaw workspace to Synology NAS with verification and rollback safety using Synology Backup"
slug: "back-up-and-restore-an-openclaw-workspace-to-synology-nas-with-verification-and-rollback-safety-using-synology-backup"
description: "Protect an OpenClaw workspace with repeatable Synology NAS backups, integrity checks, and safer restores instead of ad hoc file copying."
github_stars: 1
verification: "listed"
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

Basic usage or getting-started notes:
- | backup.sh [--dry-run] | Run incremental backup |
- bash
- clawhub install synology-backup

- Source: https://github.com/pfrederiksen/synology-backup
- Extracted from upstream docs: https://raw.githubusercontent.com/pfrederiksen/synology-backup/HEAD/README.md

## Documentation

- https://github.com/pfrederiksen/synology-backup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/back-up-and-restore-an-openclaw-workspace-to-synology-nas-with-verification-and-rollback-safety-using-synology-backup/)
