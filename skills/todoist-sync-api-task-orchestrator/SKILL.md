---
title: Todoist Sync API Task Orchestrator
description: The Todoist Sync API Task Orchestrator manages complex task workflows
  through the Todoist Sync API v9’s incremental synchronization model. It maintains
  sync_token state for efficient delta updates, sending only changed data through
  the /sync endpoint’s commands array for atomic batch operations. Core operations
  include task creation with items_add commands supporting natural language due dates
  via date_string, priority levels (p1-p4), and label assignments. The orchestrator
  handles project hierarchy through project_add and project_move commands, and implements
  section-based organization via section_add for Kanban-style workflows. Advanced
  capabilities include recurring task management through Todoist’s due.string expressions
  like “every workday at 9am”, automatic task dependency chains using item_complete
  triggers, and bulk operations through command batching with uuid-based idempotency.
  The skill integrates with Todoist webhooks for event_name-based automation triggers
  and uses the REST API v2 /tasks endpoint for quick single-item operations when full
  sync is unnecessary.
verification: security_reviewed
source: https://agentskillexchange.com/skills/todoist-sync-api-task-orchestrator/
category:
- Calendar, Email &amp; Productivity
framework:
- Gemini
---

# Todoist Sync API Task Orchestrator

The Todoist Sync API Task Orchestrator manages complex task workflows through the Todoist Sync API v9’s incremental synchronization model. It maintains sync_token state for efficient delta updates, sending only changed data through the /sync endpoint’s commands array for atomic batch operations. Core operations include task creation with items_add commands supporting natural language due dates via date_string, priority levels (p1-p4), and label assignments. The orchestrator handles project hierarchy through project_add and project_move commands, and implements section-based organization via section_add for Kanban-style workflows. Advanced capabilities include recurring task management through Todoist’s due.string expressions like “every workday at 9am”, automatic task dependency chains using item_complete triggers, and bulk operations through command batching with uuid-based idempotency. The skill integrates with Todoist webhooks for event_name-based automation triggers and uses the REST API v2 /tasks endpoint for quick single-item operations when full sync is unnecessary.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/todoist-sync-api-task-orchestrator/)
