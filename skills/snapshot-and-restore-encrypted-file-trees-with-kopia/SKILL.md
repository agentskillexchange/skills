---
title: "Snapshot and restore encrypted file trees with Kopia"
description: "Use Kopia when an agent needs to create, verify, or restore encrypted incremental snapshots across local, NAS, SFTP, WebDAV, or cloud storage targets."
verification: "listed"
source: "https://github.com/kopia/kopia"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "kopia/kopia"
  github_stars: 13110
---

# Snapshot and restore encrypted file trees with Kopia

Use Kopia when an agent is asked to run an auditable backup or restore workflow for important directories: initialize or connect to a repository, create encrypted snapshots, verify repository health, list snapshots, and restore selected paths. Invoke it instead of using the GUI or ad hoc copy commands when the operator needs repeatable CLI-driven backup, verification, or recovery steps across local, network, or cloud storage. The scope boundary is Kopia’s backup/restore lifecycle for file trees and repositories; this is not a generic cloud storage product, storage SDK, or whole-machine imaging listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/snapshot-and-restore-encrypted-file-trees-with-kopia/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/snapshot-and-restore-encrypted-file-trees-with-kopia
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/snapshot-and-restore-encrypted-file-trees-with-kopia`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/snapshot-and-restore-encrypted-file-trees-with-kopia/)
