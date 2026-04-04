---
name: "BorgBackup Deduplicating Encrypted Backup Program"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
verification: "listed"
source: "https://github.com/borgbackup/borg"
---

# BorgBackup Deduplicating Encrypted Backup Program

BorgBackup (Borg) is a deduplicating backup program with optional compression and authenticated encryption. It uses content-defined chunking for space-efficient daily backups, making it ideal for automating secure incremental backups to local or remote SSH targets.

## Installation

Install using one of the following methods:

### ClawHub (recommended)
```bash
clawhub install borgbackup-deduplicating-encrypted-backup
```

### Git
```bash
git clone https://github.com/agentskillexchange/skills.git
cp -r skills/skills/borgbackup-deduplicating-encrypted-backup ~/.openclaw/workspace/skills/
```

### Manual Download
Download from the [Agent Skill Exchange](https://agentskillexchange.com/skills/borgbackup-deduplicating-encrypted-backup/) and place in your skills directory.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/borgbackup-deduplicating-encrypted-backup/)
