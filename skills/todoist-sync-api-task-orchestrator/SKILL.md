---
name: "Todoist Sync API Task Orchestrator"
description: "Orchestrates complex task workflows using the Todoist Sync API v9 with incremental sync via sync_token. Uses commands array for atomic batch operations on items, projects, and labels."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/todoist-sync-api-task-orchestrator/"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Gemini"
---

# Todoist Sync API Task Orchestrator

The Todoist Sync API Task Orchestrator manages complex task workflows through the Todoist Sync API v9's incremental synchronization model. It maintains sync_token state for efficient delta updates, sending only changed data through the /sync endpoint's commands array for atomic batch operations.
Core operations include task creation with items_add commands supporting natural language due dates via date_string, priority levels (p1-p4), and label assignments. The orchestrator handles project hierarchy through project_add and project_move commands, and implements section-based organization via section_add for Kanban-style workflows.
Advanced capabilities include recurring task management through Todoist's due.string expressions like &#8220;every workday at 9am&#8221;, automatic task dependency chains using item_complete triggers, and bulk operations through command batching with uuid-based idempotency. The skill integrates with Todoist webhooks for event_name-based automation triggers and uses the REST API v2 /tasks endpoint for quick single-item operations when full sync is unnecessary.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/todoist-sync-api-task-orchestrator/)
