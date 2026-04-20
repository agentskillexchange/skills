---
title: "Notion Database Sync Agent"
description: "Syncs records between Notion databases and external sources using the Notion API (POST /v1/databases/{id}/query), applying field mapping, deduplication by title or unique property, and incremental updates via last_edited_time filtering."
verification: security_reviewed
source: "https://github.com/makenotion/notion-sdk-js"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "makenotion/notion-sdk-js"
  github_stars: 5582
  npm_package: "@notionhq/client"
  npm_weekly_downloads: 1182949
---

# Notion Database Sync Agent

Syncs records between Notion databases and external sources using the Notion API (POST /v1/databases/{id}/query), applying field mapping, deduplication by title or unique property, and incremental updates via last_edited_time filtering.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/notion-database-sync-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/notion-database-sync-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/notion-database-sync-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-database-sync-agent/)
