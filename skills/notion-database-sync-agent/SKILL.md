---
name: "Notion Database Sync Agent"
slug: "notion-database-sync-agent"
description: "Syncs records between Notion databases and external sources using the Notion API (POST /v1/databases/{id}/query), applying field mapping, deduplication by title or unique property, and incremental updates via last_edited_time filtering."
github_stars: 5582
verification: "listed"
source: "https://github.com/makenotion/notion-sdk-js"
category: "Calendar, Email & Productivity"
framework: "Claude Agents"
tool_ecosystem:
  github_repo: "makenotion/notion-sdk-js"
  github_stars: 5582
  npm_package: "@notionhq/client"
  npm_weekly_downloads: 1182949
---

# Notion Database Sync Agent

Syncs records between Notion databases and external sources using the Notion API (POST /v1/databases/{id}/query), applying field mapping, deduplication by title or unique property, and incremental updates via last_edited_time filtering.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install @notionhq/client
- Make a request to any Notion API endpoint.

Requirements and caveats from upstream:
- const { Client } = require("@notionhq/client")
- const { Client, APIErrorCode } = require("@notionhq/client")
- const { Client, LogLevel } = require("@notionhq/client")

Basic usage or getting-started notes:
- bash
- [![Open Val Town Template](https://stevekrouse-badge.web.val.run/?3)](https://www.val.town/v/charmaine/NotionJsSDK)
- [!NOTE]

- Source: https://github.com/makenotion/notion-sdk-js
- Extracted from upstream docs: https://raw.githubusercontent.com/makenotion/notion-sdk-js/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-database-sync-agent/)
