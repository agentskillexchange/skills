---
title: "Mirror and back up OpenClaw workspaces to your own storage with openclaw-workspace-sync"
description: "Lets an OpenClaw agent sync its workspace to cloud storage in mailbox, mirror, or bisync mode, and optionally push encrypted full-system backups to an rclone backend."
verification: "security_reviewed"
source: "https://github.com/ashbrener/openclaw-workspace-sync"
category:
  - "Integrations & Connectors"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "ashbrener/openclaw-workspace-sync"
  github_stars: 8
  npm_package: "openclaw-workspace-sync"
  npm_weekly_downloads: 295
---

# Mirror and back up OpenClaw workspaces to your own storage with openclaw-workspace-sync

Use openclaw-workspace-sync when an OpenClaw agent needs a bounded workspace sync or backup job instead of a generic cloud storage tool listing. The upstream project is explicitly an OpenClaw plugin that installs into OpenClaw, adds openclaw workspace-sync commands, supports mailbox, mirror, and bisync workspace sync modes, and can stream encrypted backups of the wider agent system through rclone-backed storage.

This is skill-shaped because the invocation is not use rclone or use cloud storage normally. The agent invokes an OpenClaw-specific operator workflow: set up the plugin, choose a sync mode, move files through the workspace inbox or outbox path, or run encrypted backup and retention flows against configured storage. The scope boundary is OpenClaw workspace synchronization and backup orchestration, not general-purpose storage management.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/mirror-and-back-up-openclaw-workspaces-to-your-own-storage-with-openclaw-workspace-sync/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/mirror-and-back-up-openclaw-workspaces-to-your-own-storage-with-openclaw-workspace-sync
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/mirror-and-back-up-openclaw-workspaces-to-your-own-storage-with-openclaw-workspace-sync`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mirror-and-back-up-openclaw-workspaces-to-your-own-storage-with-openclaw-workspace-sync/)
