---
name: "Rclone Cloud Storage Sync and Management CLI"
description: "Rclone is an open-source command-line program to sync files and directories to and from over 70 cloud storage providers including Google Drive, S3, Dropbox, Azure, OneDrive, and Backblaze B2. Often called the Swiss Army knife of cloud storage, it handles copy, sync, mount, and serve operations with encryption support."
category: "Integrations &amp; Connectors"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/rclone/rclone"
tool_ecosystem:
  github_repo: "https://github.com/rclone/rclone"
  github_stars: 56382
  license: "MIT"
---
# Rclone Cloud Storage Sync and Management CLI

Rclone is an open-source command-line program to sync files and directories to and from over 70 cloud storage providers including Google Drive, S3, Dropbox, Azure, OneDrive, and Backblaze B2. Often called the Swiss Army knife of cloud storage, it handles copy, sync, mount, and serve operations with encryption support.

Rclone is a mature, widely-adopted command-line tool for managing files across cloud storage providers. Written in Go and distributed as a single binary, it supports over 70 storage backends and provides a consistent interface for operations that would otherwise require provider-specific tools. With 50,000+ GitHub stars and millions of downloads, Rclone has become the de facto standard for cloud file management from the command line.

Core Operations

Rclone provides several key commands: rclone copy copies files from source to destination, rclone sync makes the destination identical to the source (deleting extras), rclone move moves files, and rclone check verifies file integrity between locations. All operations support bandwidth limiting, minimum/maximum file size filters, pattern-based include/exclude rules, and dry-run mode for previewing changes before execution.

Storage Backends

Rclone connects to Amazon S3 and S3-compatible services (Cloudflare R2, Backblaze B2, MinIO, DigitalOcean Spaces, Wasabi), Google Drive, Google Cloud Storage, Microsoft OneDrive, Azure Blob Storage, Dropbox, Box, SFTP, FTP, HTTP, and dozens more. Each backend is configured through a unified rclone config system that stores credentials locally. Multiple remotes can be configured simultaneously, enabling cross-cloud transfers.

Advanced Features

The rclone mount command exposes any cloud storage as a local filesystem using FUSE, allowing standard file tools to interact with remote files. rclone serve creates HTTP, WebDAV, FTP, SFTP, or DLNA servers backed by any remote. The rclone crypt backend provides client-side encryption that wraps any other remote, encrypting filenames and contents before upload.

Bisync and Deduplication

Rclone supports bidirectional sync with rclone bisync for keeping two locations synchronized in both directions, handling conflicts and deletions. The rclone dedupe command finds and resolves duplicate files on remotes that allow them. Combined with rclone lsjson for machine-readable output and rclone rc for remote control via HTTP API, Rclone provides comprehensive automation capabilities.

Agent Workflow

AI agents use Rclone for backup automation, cross-cloud migration, scheduled sync jobs, and storage management. An agent can configure remotes, run sync operations with specific filters, monitor transfer progress via the RC API, verify data integrity post-transfer, and manage encrypted backups. The JSON output mode and RC HTTP API make Rclone particularly well-suited for programmatic control by agent systems.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill rclone-cloud-storage-sync-management-cli
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill rclone-cloud-storage-sync-management-cli -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill rclone-cloud-storage-sync-management-cli -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill rclone-cloud-storage-sync-management-cli -a codex
```

### OpenClaw

```bash
clawhub install rclone-cloud-storage-sync-management-cli
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rclone-cloud-storage-sync-management-cli/)
