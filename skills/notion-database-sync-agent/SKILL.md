---
name: "Notion Database Sync Agent"
description: "Syncs records between Notion databases and external sources using the Notion API (POST /v1/databases/{id}/query), applying field mapping, deduplication by title or unique property, and incremental updates via last_edited_time filtering."
category: "Calendar, Email & Productivity"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/notion-database-sync-agent/"
---
# Notion Database Sync Agent

Syncs records between Notion databases and external sources using the Notion API (POST /v1/databases/{id}/query), applying field mapping, deduplication by title or unique property, and incremental updates via last_edited_time filtering.

Syncs records between Notion databases and external sources using the Notion API (POST /v1/databases/{id}/query), applying field mapping, deduplication by title or unique property, and incremental updates via last_edited_time filtering.



This skill queries a Notion database, maps its properties to a target schema, and syncs new/updated records to or from an external system (CSV, Airtable, Google Sheets, or a custom API). Handles Notion property types: title, rich_text, number, select, multi_select, date, checkbox, url, email, relation. Supports bidirectional sync with conflict resolution strategies (last_write_wins or source_wins).



Ideal for CRM backfill, project tracking exports, content pipeline management, and cross-tool data consistency. Not for Notion page content (only database properties). Not for databases with more than 100 relation properties — relation page traversal multiplies API calls significantly. Requires a Notion integration token with database read/write permissions and the integration connected to the target databases.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill notion-database-sync-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill notion-database-sync-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill notion-database-sync-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill notion-database-sync-agent -a codex
```

### OpenClaw

```bash
clawhub install notion-database-sync-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-database-sync-agent/)
