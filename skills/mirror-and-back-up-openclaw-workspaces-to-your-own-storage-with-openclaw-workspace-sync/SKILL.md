---
title: "Mirror and back up OpenClaw workspaces to your own storage with openclaw-workspace-sync"
description: "Use openclaw-workspace-sync when an OpenClaw agent needs a bounded workspace sync or backup job instead of a generic cloud storage tool listing. The upstream project is explicitly an OpenClaw plugin that installs into OpenClaw, adds openclaw workspace-sync commands, supports mailbox, mirror, and bisync workspace sync modes, and can stream encrypted backups of the wider agent system through rclone-backed storage. This is skill-shaped because the invocation is not use rclone or use cloud storage normally. The agent invokes an OpenClaw-specific operator workflow: set up the plugin, choose a sync mode, move files through the workspace inbox or outbox path, or run encrypted backup and retention flows against configured storage. The scope boundary is OpenClaw workspace synchronization and backup orchestration, not general-purpose storage management."
source: "https://github.com/ashbrener/openclaw-workspace-sync"
verification: "listed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "ashbrener/openclaw-workspace-sync"
  github_stars: 8
  npm_package: "openclaw-workspace-sync"
  npm_weekly_downloads: 295
---

# Mirror and back up OpenClaw workspaces to your own storage with openclaw-workspace-sync

Use openclaw-workspace-sync when an OpenClaw agent needs a bounded workspace sync or backup job instead of a generic cloud storage tool listing. The upstream project is explicitly an OpenClaw plugin that installs into OpenClaw, adds openclaw workspace-sync commands, supports mailbox, mirror, and bisync workspace sync modes, and can stream encrypted backups of the wider agent system through rclone-backed storage. This is skill-shaped because the invocation is not use rclone or use cloud storage normally. The agent invokes an OpenClaw-specific operator workflow: set up the plugin, choose a sync mode, move files through the workspace inbox or outbox path, or run encrypted backup and retention flows against configured storage. The scope boundary is OpenClaw workspace synchronization and backup orchestration, not general-purpose storage management.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mirror-and-back-up-openclaw-workspaces-to-your-own-storage-with-openclaw-workspace-sync/)
