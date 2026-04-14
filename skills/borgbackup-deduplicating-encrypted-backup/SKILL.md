---
title: "BorgBackup Deduplicating Encrypted Backup Program"
description: "BorgBackup (Borg) is a deduplicating backup program with optional compression and authenticated encryption. It uses content-defined chunking for space-efficient daily backups, making it ideal for automating secure incremental backups to local or remote SSH targets."
verification: security_reviewed
source: "https://github.com/borgbackup/borg"
category:
  - "Runbooks &amp; Diagnostics"
---

# BorgBackup Deduplicating Encrypted Backup Program

BorgBackup (Borg) is a deduplicating backup program with optional compression and authenticated encryption. It uses content-defined chunking for space-efficient daily backups, making it ideal for automating secure incremental backups to local or remote SSH targets.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/borgbackup-deduplicating-encrypted-backup/)
