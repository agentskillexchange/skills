---
name: "Restic Fast Encrypted Backup Program"
description: "Restic is a fast, secure, and efficient backup program supporting local, SFTP, S3, Azure, GCS, and many other storage backends. Written in Go with 32k+ GitHub stars, it features deduplication, encryption, and snapshot-based incremental backups."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/restic/restic"
---

# Restic Fast Encrypted Backup Program

Restic is a fast, secure, and efficient backup program supporting local, SFTP, S3, Azure, GCS, and many other storage backends. Written in Go with 32k+ GitHub stars, it features deduplication, encryption, and snapshot-based incremental backups.


## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill restic-encrypted-backup-tool
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill restic-encrypted-backup-tool -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill restic-encrypted-backup-tool -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill restic-encrypted-backup-tool -a codex
```

### OpenClaw

```bash
clawhub install restic-encrypted-backup-tool
```

## Overview

Restic is a backup program designed to be fast, efficient, and secure. With over 32,000 GitHub stars and a BSD-2 license, it is one of the most widely adopted open-source backup tools. It supports Linux, macOS, Windows, FreeBSD, and OpenBSD, and can store backups on local disks, SFTP servers, Amazon S3, Google Cloud Storage, Azure Blob Storage, Backblaze B2, and any S3-compatible storage.

Every backup in restic creates an immutable snapshot. Content-defined chunking and deduplication ensure that only new or modified data is stored in each backup, making incremental backups extremely efficient. A typical second backup of a large directory completes in seconds because only changed chunks need to be uploaded. The deduplication operates at the content level, so even renamed or moved files are handled without re-uploading data.

Security is a core design principle. All data is encrypted with AES-256 before leaving the machine, and the encryption key is derived from a user-provided password using scrypt. The repository format ensures that even the storage provider cannot read backup contents. Integrity verification is built in: restic check validates the consistency of the repository, detecting any corruption or tampering.

Restic provides a rich CLI for managing backups. The backup command creates snapshots, restore recovers data, snapshots lists available restore points, diff shows changes between snapshots, and forget combined with prune implements retention policies. Mount allows browsing snapshots as a FUSE filesystem, making it easy to recover individual files without a full restore.

For AI agents managing infrastructure, restic provides reliable automated backup capabilities. An agent can script restic backup with include/exclude patterns, manage retention policies with restic forget –keep-daily 7 –keep-weekly 4 –keep-monthly 6, verify backup integrity with restic check, and restore specific files or directories from any snapshot. The tool installs via package managers, standalone binaries, or go install.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/restic-encrypted-backup-tool/)
