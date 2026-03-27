---
name: "Todoist Sync API Task Orchestrator"
description: "Orchestrates complex task workflows using the Todoist Sync API v9 with incremental sync via sync_token. Uses commands array for atomic batch operations on items, projects, and labels."
category: "Calendar, Email & Productivity"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/todoist-sync-api-task-orchestrator/"
---

# Todoist Sync API Task Orchestrator

Orchestrates complex task workflows using the Todoist Sync API v9 with incremental sync via sync_token. Uses commands array for atomic batch operations on items, projects, and labels.

## Overview

The Todoist Sync API Task Orchestrator manages complex task workflows through the Todoist Sync API v9’s incremental synchronization model. It maintains sync_token state for efficient delta updates, sending only changed data through the /sync endpoint’s commands array for atomic batch operations.

Core operations include task creation with items_add commands supporting natural language due dates via date_string, priority levels (p1-p4), and label assignments. The orchestrator handles project hierarchy through project_add and project_move commands, and implements section-based organization via section_add for Kanban-style workflows.

Advanced capabilities include recurring task management through Todoist’s due.string expressions like “every workday at 9am”, automatic task dependency chains using item_complete triggers, and bulk operations through command batching with uuid-based idempotency. The skill integrates with Todoist webhooks for event_name-based automation triggers and uses the REST API v2 /tasks endpoint for quick single-item operations when full sync is unnecessary.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill todoist-sync-api-task-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill todoist-sync-api-task-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill todoist-sync-api-task-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill todoist-sync-api-task-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install todoist-sync-api-task-orchestrator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/todoist-sync-api-task-orchestrator/
