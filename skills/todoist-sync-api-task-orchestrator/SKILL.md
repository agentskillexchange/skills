---
title: "Todoist Sync API Task Orchestrator"
description: "Orchestrates complex task workflows using the Todoist Sync API v9 with incremental sync via sync_token. Uses commands array for atomic batch operations on items, projects, and labels."
verification: security_reviewed
source: "https://developer.todoist.com/api/v1/"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Gemini"
---

# Todoist Sync API Task Orchestrator

The Todoist Sync API Task Orchestrator manages complex task workflows through the Todoist Sync API v9’s incremental synchronization model. It maintains sync_token state for efficient delta updates, sending only changed data through the /sync endpoint’s commands array for atomic batch operations.

Core operations include task creation with items_add commands supporting natural language due dates via date_string, priority levels (p1-p4), and label assignments. The orchestrator handles project hierarchy through project_add and project_move commands, and implements section-based organization via section_add for Kanban-style workflows.

Advanced capabilities include recurring task management through Todoist’s due.string expressions like “every workday at 9am”, automatic task dependency chains using item_complete triggers, and bulk operations through command batching with uuid-based idempotency. The skill integrates with Todoist webhooks for event_name-based automation triggers and uses the REST API v2 /tasks endpoint for quick single-item operations when full sync is unnecessary.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/todoist-sync-api-task-orchestrator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/todoist-sync-api-task-orchestrator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/todoist-sync-api-task-orchestrator/)
