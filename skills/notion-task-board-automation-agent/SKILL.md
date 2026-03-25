---
name: "Notion Task Board Automation"
description: "Automates Notion database workflows using the Notion API databases.query and pages.create endpoints. Builds filtered views with compound filter objects, manages status property transitions, and syncs with external project trackers."
category: "Calendar, Email & Productivity"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/notion-task-board-automation-agent/"
tool_ecosystem:
  tool: "notion"
  github_stars: 5562
  npm_weekly_downloads: 1084242
  github_repo: "makenotion/notion-sdk-js"
  license: "MIT"
  maintained: true
---

# Notion Task Board Automation

Automates Notion database workflows using the Notion API databases.query and pages.create endpoints. Builds filtered views with compound filter objects, manages status property transitions, and syncs with external project trackers.

## Overview

The Notion Task Board Automation skill manages project workflows within Notion databases using the official Notion API. It queries databases with `POST /v1/databases/{id}/query` using compound filter objects that combine property filters with AND/OR logic for complex view generation.

The skill creates and updates pages via `POST /v1/pages` with rich property types including select, multi-select, date ranges, relations, and rollups. It manages status property transitions (Not Started → In Progress → Done) with validation rules and automated timestamp updates on status changes.

Advanced features include relation property management for cross-database linking, formula property interpretation for computed fields, and rollup aggregation monitoring. The agent builds sorted views using multi-level sort specifications on database queries. It handles pagination through `start_cursor` and `has_more` responses for databases with 100+ items. Block content management supports appending rich text, to-do lists, and embedded content to pages. Integrates with Notion webhooks for real-time change detection and supports database property schema modifications via `PATCH /v1/databases/{id}`.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill notion-task-board-automation-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill notion-task-board-automation-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill notion-task-board-automation-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill notion-task-board-automation-agent -a codex
```

### OpenClaw

```bash
clawhub install notion-task-board-automation-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/notion-task-board-automation-agent/
