---
name: "Notion Workspace Automation Hub"
description: "Orchestrates Notion workspace workflows using Notion API v2 with database queries, page creation, and relation property management. Automates sprint boards, meeting notes, and knowledge base maintenance."
category: "Calendar, Email &amp; Productivity"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/makenotion/notion-sdk-js"
tool_ecosystem:
  tool: notion
  github_repo: makenotion/notion-sdk-js
  github_stars: 5566
  license: MIT
  maintained: true
---
# Notion Workspace Automation Hub

Orchestrates Notion workspace workflows using Notion API v2 with database queries, page creation, and relation property management. Automates sprint boards, meeting notes, and knowledge base maintenance.

## Overview

The Notion Workspace Automation Hub provides comprehensive workspace management through the Notion API (2022-06-28 version). It handles database operations, page lifecycle management, and cross-database relation maintenance for complex workspace architectures.

Database automation includes creating filtered views via the Query Database endpoint with compound filters and sorts, bulk property updates using batch operations, rollup recalculation triggers, and automatic status transitions based on date properties (moving tasks to "Overdue" when due dates pass).

Sprint board management automates sprint creation with templated databases, story point aggregation via rollup properties, velocity calculations from historical sprint data, and burndown chart data generation exported to inline databases. Meeting notes automation creates pages from templates with attendee lookup via the Users API, agenda items pulled from linked databases, and post-meeting action item extraction.

Knowledge base maintenance includes duplicate detection using title similarity matching, orphan page identification (pages with no backlinks), stale content flagging based on last-edited timestamps, and automatic table of contents generation using the Block API to analyze heading structure. Webhook integration via Notion's new webhook system triggers workflows on page property changes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill notion-workspace-automation-hub
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill notion-workspace-automation-hub -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill notion-workspace-automation-hub -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill notion-workspace-automation-hub -a codex
```

### OpenClaw

```bash
clawhub install notion-workspace-automation-hub
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/notion-workspace-automation-hub/)
