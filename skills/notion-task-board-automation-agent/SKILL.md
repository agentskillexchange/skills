---
title: "Notion Task Board Automation"
description: "Automates Notion database workflows using the Notion API databases.query and pages.create endpoints. Builds filtered views with compound filter objects, manages status property transitions, and syncs with external project trackers."
verification: "security_reviewed"
source: "https://github.com/makenotion/notion-sdk-js"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "makenotion/notion-sdk-js"
  github_stars: 5582
  npm_package: "@notionhq/client"
  npm_weekly_downloads: 1182949
---

# Notion Task Board Automation

The Notion Task Board Automation skill manages project workflows within Notion databases using the official Notion API. It queries databases with POST /v1/databases/{id}/query using compound filter objects that combine property filters with AND/OR logic for complex view generation. The skill creates and updates pages via POST /v1/pages with rich property types including select, multi-select, date ranges, relations, and rollups. It manages status property transitions (Not Started → In Progress → Done) with validation rules and automated timestamp updates on status changes. Advanced features include relation property management for cross-database linking, formula property interpretation for computed fields, and rollup aggregation monitoring. The agent builds sorted views using multi-level sort specifications on database queries. It handles pagination through start_cursor and has_more responses for databases with 100+ items. Block content management supports appending rich text, to-do lists, and embedded content to pages. Integrates with Notion webhooks for real-time change detection and supports database property schema modifications via PATCH /v1/databases/{id}.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/notion-task-board-automation-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/notion-task-board-automation-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/notion-task-board-automation-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-task-board-automation-agent/)
