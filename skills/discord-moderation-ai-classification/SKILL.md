---
title: "Discord Moderation Bot with AI Classification"
description: "Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart."
verification: "security_reviewed"
source: "https://github.com/discordjs/discord.js"
category:
  - "Security & Verification"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "discordjs/discord.js"
  github_stars: 26668
  npm_package: "discord.js"
  npm_weekly_downloads: 563530
---

# Discord Moderation Bot with AI Classification

Listens to Discord gateway events, passing flagged messages to the OpenAI Moderation API and a custom classifier to detect spam and coordinated inauthentic behavior. Issues timeouts via the Discord REST API and logs incidents to a Supabase Postgres table for moderator review. Rule sets are stored in Supabase and hot-reloaded without restart.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/discord-moderation-ai-classification/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/discord-moderation-ai-classification
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/discord-moderation-ai-classification`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/discord-moderation-ai-classification/)
