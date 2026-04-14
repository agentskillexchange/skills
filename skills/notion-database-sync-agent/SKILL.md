---
title: "Notion Database Sync Agent"
description: "Syncs records between Notion databases and external sources using the Notion API (POST /v1/databases/{id}/query), applying field mapping, deduplication by title or unique property, and incremental updates via last_edited_time filtering."
verification: security_reviewed
source: "https://github.com/makenotion/notion-sdk-js"
category:
  - "Calendar, Email &amp; Productivity"
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

This skill queries a Notion database, maps its properties to a target schema, and syncs new/updated records to or from an external system (CSV, Airtable, Google Sheets, or a custom API). Handles Notion property types: title, rich_text, number, select, multi_select, date, checkbox, url, email, relation. Supports bidirectional sync with conflict resolution strategies (last_write_wins or source_wins).

Ideal for CRM backfill, project tracking exports, content pipeline management, and cross-tool data consistency. Not for Notion page content (only database properties). Not for databases with more than 100 relation properties — relation page traversal multiplies API calls significantly. Requires a Notion integration token with database read/write permissions and the integration connected to the target databases.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-database-sync-agent/)
