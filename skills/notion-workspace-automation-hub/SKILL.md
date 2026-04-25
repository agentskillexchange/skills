---
title: "Notion Workspace Automation Hub"
description: "Orchestrates Notion workspace workflows using Notion API v2 with database queries, page creation, and relation property management. Automates sprint boards, meeting notes, and knowledge base maintenance."
verification: "security_reviewed"
source: "https://github.com/makenotion/notion-sdk-js"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "makenotion/notion-sdk-js"
  github_stars: 5582
  npm_package: "@notionhq/client"
  npm_weekly_downloads: 1182949
---

# Notion Workspace Automation Hub

The Notion Workspace Automation Hub provides comprehensive workspace management through the Notion API (2022-06-28 version). It handles database operations, page lifecycle management, and cross-database relation maintenance for complex workspace architectures. Database automation includes creating filtered views via the Query Database endpoint with compound filters and sorts, bulk property updates using batch operations, rollup recalculation triggers, and automatic status transitions based on date properties (moving tasks to “Overdue” when due dates pass). Sprint board management automates sprint creation with templated databases, story point aggregation via rollup properties, velocity calculations from historical sprint data, and burndown chart data generation exported to inline databases. Meeting notes automation creates pages from templates with attendee lookup via the Users API, agenda items pulled from linked databases, and post-meeting action item extraction. Knowledge base maintenance includes duplicate detection using title similarity matching, orphan page identification (pages with no backlinks), stale content flagging based on last-edited timestamps, and automatic table of contents generation using the Block API to analyze heading structure. Webhook integration via Notion’s new webhook system triggers workflows on page property changes.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/notion-workspace-automation-hub/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/notion-workspace-automation-hub
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/notion-workspace-automation-hub`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-workspace-automation-hub/)
