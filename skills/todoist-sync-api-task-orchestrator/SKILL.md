---
title: "Todoist Sync API Task Orchestrator"
description: "Orchestrates complex task workflows using the Todoist Sync API v9 with incremental sync via sync_token. Uses commands array for atomic batch operations on items, projects, and labels."
slug: "todoist-sync-api-task-orchestrator"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/todoist-sync-api-task-orchestrator/"
listed: true
---

# Todoist Sync API Task Orchestrator

Orchestrates complex task workflows using the Todoist Sync API v9 with incremental sync via sync_token. Uses commands array for atomic batch operations on items, projects, and labels.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install todoist-sync-api-task-orchestrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Todoist Sync API Task Orchestrator manages complex task workflows through the Todoist Sync API v9’s incremental synchronization model. It maintains sync_token state for efficient delta updates, sending only changed data through the /sync endpoint’s commands array for atomic batch operations.
Core operations include task creation with items_add commands supporting natural language due dates via date_string, priority levels (p1-p4), and label assignments. The orchestrator handles project hierarchy through project_add and project_move commands, and implements section-based organization via section_add for Kanban-style workflows.
Advanced capabilities include recurring task management through Todoist’s due.string expressions like “every workday at 9am”, automatic task dependency chains using item_complete triggers, and bulk operations through command batching with uuid-based idempotency. The skill integrates with Todoist webhooks for event_name-based automation triggers and uses the REST API v2 /tasks endpoint for quick single-item operations when full sync is unnecessary.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/todoist-sync-api-task-orchestrator/)
