---
title: "BorgBackup Deduplicating Encrypted Backup Program"
description: "BorgBackup (Borg) is a deduplicating backup program with optional compression and authenticated encryption. It uses content-defined chunking for space-efficient daily backups, making it ideal for automating secure incremental backups to local or remote SSH targets."
verification: "security_reviewed"
source: "https://github.com/borgbackup/borg"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
---

# BorgBackup Deduplicating Encrypted Backup Program

BorgBackup (Borg) is a deduplicating backup program with optional compression and authenticated encryption. It uses content-defined chunking for space-efficient daily backups, making it ideal for automating secure incremental backups to local or remote SSH targets.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/borgbackup-deduplicating-encrypted-backup/)
