---
name: "Mirror and back up OpenClaw workspaces to your own storage with openclaw-workspace-sync"
slug: "mirror-and-back-up-openclaw-workspaces-to-your-own-storage-with-openclaw-workspace-sync"
description: "Lets an OpenClaw agent sync its workspace to cloud storage in mailbox, mirror, or bisync mode, and optionally push encrypted full-system backups to an rclone backend."
github_stars: 8
verification: "security_reviewed"
source: "https://github.com/ashbrener/openclaw-workspace-sync"
author: "ashbrener"
publisher_type: "individual"
category: "Integrations & Connectors"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "ashbrener/openclaw-workspace-sync"
  github_stars: 8
  npm_package: "openclaw-workspace-sync"
  npm_weekly_downloads: 295
---

# Mirror and back up OpenClaw workspaces to your own storage with openclaw-workspace-sync

Lets an OpenClaw agent sync its workspace to cloud storage in mailbox, mirror, or bisync mode, and optionally push encrypted full-system backups to an rclone backend.

## Prerequisites

OpenClaw, rclone, supported cloud storage backend

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with openclaw plugins install openclaw-workspace-sync, then run openclaw workspace-sync setup. Manual install is also supported by cloning the repo into ~/.openclaw/extensions and running npm install --omit=dev.
```

## Documentation

- https://github.com/ashbrener/openclaw-workspace-sync

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mirror-and-back-up-openclaw-workspaces-to-your-own-storage-with-openclaw-workspace-sync/)
