---
title: "BorgBackup Deduplicating Encrypted Backup Program"
description: "Overview\nBorgBackup (short: Borg) is an open source deduplicating backup program written in Python with performance-critical code in C/Cython. It provides efficient, secure backups using content-defined chunking combined with 256-bit authenticated encryption (AES-OCB or chacha20-poly1305).\nHow It Works\nBorg splits every file into variable-length chunks and stores only chunks that have never been seen before. Deduplication considers all chunks in the repository regardless of source machine, previous backup, or file. This means renaming or moving files does not break deduplication, and small changes to large files only store the new chunks.\nKey Features\n\nSpace-efficient storage: Content-defined chunking deduplicates across all archives in a repository, regardless of file name, timestamp, or position within a file.\nAuthenticated encryption: All data can be protected with AES-256-OCB or chacha20-poly1305 client-side encryption, ensuring confidentiality and integrity.\nCompression: Supports lz4 (fast), zstd (flexible range), zlib (medium), and lzma (high compression).\nRemote backups over SSH: Store data on any remote host accessible via SSH. When Borg is installed on the remote host, transfers are significantly faster than SSHFS or NFS.\nMountable archives: Backup archives are mountable as FUSE filesystems for easy browsing and selective restores.\nCross-platform: Single-file binaries for Linux, macOS, FreeBSD, and experimental support for WSL and Cygwin.\n\nAgent Integration\nAgents can use the borg CLI to automate backup creation, pruning, and monitoring. Typical workflows include scheduling daily borg create commands, running borg check for repository integrity, borg prune for retention management, and borg list or borg info for backup inventory and status reporting. The tool outputs structured data suitable for parsing in automation scripts.\nInstallation\npip install borgbackup\n# Or use standalone binary from GitHub releases\n# Or via system package manager: apt install borgbackup\nExample Usage\n# Initialize a new encrypted repository\nborg repo-create -e repokey-aes-ocb /path/to/repo\n\n# Create a backup\nborg create /path/to/repo::backup-{now} ~/Documents\n\n# List archives\nborg list /path/to/repo\n\n# Restore files\nborg extract /path/to/repo::backup-name\n\n# Prune old backups (keep 7 daily, 4 weekly)\nborg prune --keep-daily 7 --keep-weekly 4 /path/to/repo"
verification: security_reviewed
source: "https://github.com/borgbackup/borg"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "borgbackup/borg"
  github_stars: 13199
---

# BorgBackup Deduplicating Encrypted Backup Program

Overview
BorgBackup (short: Borg) is an open source deduplicating backup program written in Python with performance-critical code in C/Cython. It provides efficient, secure backups using content-defined chunking combined with 256-bit authenticated encryption (AES-OCB or chacha20-poly1305).
How It Works
Borg splits every file into variable-length chunks and stores only chunks that have never been seen before. Deduplication considers all chunks in the repository regardless of source machine, previous backup, or file. This means renaming or moving files does not break deduplication, and small changes to large files only store the new chunks.
Key Features

Space-efficient storage: Content-defined chunking deduplicates across all archives in a repository, regardless of file name, timestamp, or position within a file.
Authenticated encryption: All data can be protected with AES-256-OCB or chacha20-poly1305 client-side encryption, ensuring confidentiality and integrity.
Compression: Supports lz4 (fast), zstd (flexible range), zlib (medium), and lzma (high compression).
Remote backups over SSH: Store data on any remote host accessible via SSH. When Borg is installed on the remote host, transfers are significantly faster than SSHFS or NFS.
Mountable archives: Backup archives are mountable as FUSE filesystems for easy browsing and selective restores.
Cross-platform: Single-file binaries for Linux, macOS, FreeBSD, and experimental support for WSL and Cygwin.

Agent Integration
Agents can use the borg CLI to automate backup creation, pruning, and monitoring. Typical workflows include scheduling daily borg create commands, running borg check for repository integrity, borg prune for retention management, and borg list or borg info for backup inventory and status reporting. The tool outputs structured data suitable for parsing in automation scripts.
Installation
pip install borgbackup
# Or use standalone binary from GitHub releases
# Or via system package manager: apt install borgbackup
Example Usage
# Initialize a new encrypted repository
borg repo-create -e repokey-aes-ocb /path/to/repo

# Create a backup
borg create /path/to/repo::backup-{now} ~/Documents

# List archives
borg list /path/to/repo

# Restore files
borg extract /path/to/repo::backup-name

# Prune old backups (keep 7 daily, 4 weekly)
borg prune --keep-daily 7 --keep-weekly 4 /path/to/repo

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/borgbackup-deduplicating-encrypted-backup
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/borgbackup-deduplicating-encrypted-backup` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/borgbackup-deduplicating-encrypted-backup/)
