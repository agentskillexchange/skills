---
title: Notion Database Sync Agent
description: Syncs records between Notion databases and external sources using the Notion API (POST /v1/databases/{id}/query), applying field mapping, deduplication by title or unique property, and incremental updates via last_edited_time filtering.
verification: security_reviewed
source: https://github.com/makenotion/notion-sdk-js
category:
- Calendar, Email & Productivity
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: makenotion/notion-sdk-js
  github_stars: 5582
  npm_package: '@notionhq/client'
  npm_weekly_downloads: 1182949
---

# Notion Database Sync Agent

Syncs records between Notion databases and external sources using the Notion API (POST /v1/databases/{id}/query), applying field mapping, deduplication by title or unique property, and incremental updates via last_edited_time filtering.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-database-sync-agent/)
