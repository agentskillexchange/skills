---
title: Notion Database Sync Agent
description: 'Syncs records between Notion databases and external sources using the
  Notion API (POST /v1/databases/{id}/query), applying field mapping, deduplication
  by title or unique property, and incremental updates via last_edited_time filtering.
  This skill queries a Notion database, maps its properties to a target schema, and
  syncs new/updated records to or from an external system (CSV, Airtable, Google Sheets,
  or a custom API). Handles Notion property types: title, rich_text, number, select,
  multi_select, date, checkbox, url, email, relation. Supports bidirectional sync
  with conflict resolution strategies (last_write_wins or source_wins). Ideal for
  CRM backfill, project tracking exports, content pipeline management, and cross-tool
  data consistency. Not for Notion page content (only database properties). Not for
  databases with more than 100 relation properties — relation page traversal multiplies
  API calls significantly. Requires a Notion integration token with database read/write
  permissions and the integration connected to the target databases.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/notion-database-sync-agent/
category:
- Calendar, Email &amp; Productivity
framework:
- Claude Agents
---

# Notion Database Sync Agent

Syncs records between Notion databases and external sources using the Notion API (POST /v1/databases/{id}/query), applying field mapping, deduplication by title or unique property, and incremental updates via last_edited_time filtering. This skill queries a Notion database, maps its properties to a target schema, and syncs new/updated records to or from an external system (CSV, Airtable, Google Sheets, or a custom API). Handles Notion property types: title, rich_text, number, select, multi_select, date, checkbox, url, email, relation. Supports bidirectional sync with conflict resolution strategies (last_write_wins or source_wins). Ideal for CRM backfill, project tracking exports, content pipeline management, and cross-tool data consistency. Not for Notion page content (only database properties). Not for databases with more than 100 relation properties — relation page traversal multiplies API calls significantly. Requires a Notion integration token with database read/write permissions and the integration connected to the target databases.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-database-sync-agent/)
