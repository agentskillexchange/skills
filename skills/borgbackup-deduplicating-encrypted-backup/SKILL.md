---
name: "BorgBackup Deduplicating Encrypted Backup Program"
description: "BorgBackup (Borg) is a deduplicating backup program with optional compression and authenticated encryption. It uses content-defined chunking for space-efficient daily backups, making it ideal for automating secure incremental backups to local or remote SSH targets."
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/borgbackup/borg"
---
# BorgBackup Deduplicating Encrypted Backup Program

BorgBackup (Borg) is a deduplicating backup program with optional compression and authenticated encryption. It uses content-defined chunking for space-efficient daily backups, making it ideal for automating secure incremental backups to local or remote SSH targets.

## Overview

Overview

BorgBackup (short: Borg) is an open source deduplicating backup program written in Python with performance-critical code in C/Cython. It provides efficient, secure backups using content-defined chunking combined with 256-bit authenticated encryption (AES-OCB or chacha20-poly1305).

How It Works

Borg splits every file into variable-length chunks and stores only chunks that have never been seen before. Deduplication considers all chunks in the repository regardless of source machine, previous backup, or file. This means renaming or moving files does not break deduplication, and small changes to large files only store the new chunks.

Key Features

- Space-efficient storage: Content-defined chunking deduplicates across all archives in a repository, regardless of file name, timestamp, or position within a file.

- Authenticated encryption: All data can be protected with AES-256-OCB or chacha20-poly1305 client-side encryption, ensuring confidentiality and integrity.

- Compression: Supports lz4 (fast), zstd (flexible range), zlib (medium), and lzma (high compression).

- Remote backups over SSH: Store data on any remote host accessible via SSH. When Borg is installed on the remote host, transfers are significantly faster than SSHFS or NFS.

- Mountable archives: Backup archives are mountable as FUSE filesystems for easy browsing and selective restores.

- Cross-platform: Single-file binaries for Linux, macOS, FreeBSD, and experimental support for WSL and Cygwin.

Agent Integration

Agents can use the `borg` CLI to automate backup creation, pruning, and monitoring. Typical workflows include scheduling daily `borg create` commands, running `borg check` for repository integrity, `borg prune` for retention management, and `borg list` or `borg info` for backup inventory and status reporting. The tool outputs structured data suitable for parsing in automation scripts.

Installation
``pip install borgbackup
# Or use standalone binary from GitHub releases
# Or via system package manager: apt install borgbackup``

Example Usage
``# Initialize a new encrypted repository
borg repo-create -e repokey-aes-ocb /path/to/repo

# Create a backup
borg create /path/to/repo::backup-{now} ~/Documents

# List archives
borg list /path/to/repo

# Restore files
borg extract /path/to/repo::backup-name

# Prune old backups (keep 7 daily, 4 weekly)
borg prune --keep-daily 7 --keep-weekly 4 /path/to/repo``

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill borgbackup-deduplicating-encrypted-backup
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill borgbackup-deduplicating-encrypted-backup -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill borgbackup-deduplicating-encrypted-backup -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill borgbackup-deduplicating-encrypted-backup -a codex
```

### OpenClaw

```bash
clawhub install borgbackup-deduplicating-encrypted-backup
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/borgbackup-deduplicating-encrypted-backup/)
