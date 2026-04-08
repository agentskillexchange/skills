---
title: "BorgBackup Deduplicating Encrypted Backup Program"
slug: "borgbackup-deduplicating-encrypted-backup"
description: "BorgBackup (Borg) is a deduplicating backup program with optional compression and authenticated encryption. It uses content-defined chunking for space-efficient daily backups, making it ideal for automating secure incremental backups to local or remote SSH targets."
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/borgbackup/borg"
---

# BorgBackup Deduplicating Encrypted Backup Program

BorgBackup (Borg) is a deduplicating backup program with optional compression and authenticated encryption. It uses content-defined chunking for space-efficient daily backups, making it ideal for automating secure incremental backups to local or remote SSH targets.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/borgbackup-deduplicating-encrypted-backup/)
