---
title: "Todoist Sync API Task Orchestrator"
description: "The Todoist Sync API Task Orchestrator manages complex task workflows through the Todoist Sync API v9&#8217;s incremental synchronization model. It maintains sync_token state for efficient delta updates, sending only changed data through the /sync endpoint&#8217;s commands array for atomic batch operations. Core operations include task creation with items_add commands supporting natural language due dates via date_string, priority levels (p1-p4), and label assignments. The orchestrator handles project hierarchy through project_add and project_move commands, and implements section-based organization via section_add for Kanban-style workflows. Advanced capabilities include recurring task management through Todoist&#8217;s due.string expressions like &#8220;every workday at 9am&#8221;, automatic task dependency chains using item_complete triggers, and bulk operations through command batching with uuid-based idempotency. The skill integrates with Todoist webhooks for event_name-based automation triggers and uses the REST API v2 /tasks endpoint for quick single-item operations when full sync is unnecessary."
source: "https://developer.todoist.com/api/v1/"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Gemini"
---

# Todoist Sync API Task Orchestrator

The Todoist Sync API Task Orchestrator manages complex task workflows through the Todoist Sync API v9&#8217;s incremental synchronization model. It maintains sync_token state for efficient delta updates, sending only changed data through the /sync endpoint&#8217;s commands array for atomic batch operations. Core operations include task creation with items_add commands supporting natural language due dates via date_string, priority levels (p1-p4), and label assignments. The orchestrator handles project hierarchy through project_add and project_move commands, and implements section-based organization via section_add for Kanban-style workflows. Advanced capabilities include recurring task management through Todoist&#8217;s due.string expressions like &#8220;every workday at 9am&#8221;, automatic task dependency chains using item_complete triggers, and bulk operations through command batching with uuid-based idempotency. The skill integrates with Todoist webhooks for event_name-based automation triggers and uses the REST API v2 /tasks endpoint for quick single-item operations when full sync is unnecessary.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/todoist-sync-api-task-orchestrator/)
