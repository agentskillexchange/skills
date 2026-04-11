---
title: "BorgBackup Deduplicating Encrypted Backup Program"
slug: "borgbackup-deduplicating-encrypted-backup"
description: "BorgBackup (Borg) is a deduplicating backup program with optional compression and authenticated encryption. It uses content-defined chunking for space-efficient daily backups, making it ideal for automating secure incremental backups to local or remote SSH targets."
category: "Runbooks &amp; Diagnostics"
framework: "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/borgbackup/borg"
---

# BorgBackup Deduplicating Encrypted Backup Program

BorgBackup (Borg) is a deduplicating backup program with optional compression and authenticated encryption. It uses content-defined chunking for space-efficient daily backups, making it ideal for automating secure incremental backups to local or remote SSH targets.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your skills directory.
2. Install it through your agent platform's skill manager if supported.
3. Add it as a Git submodule or vendored folder in your repo.
4. Copy the files into a local custom skills/workspace directory.
5. Pull it from the Agent Skill Exchange catalog or this GitHub repo.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/borgbackup-deduplicating-encrypted-backup/)
