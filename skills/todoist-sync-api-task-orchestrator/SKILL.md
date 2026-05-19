---
name: "Todoist Sync API Task Orchestrator"
slug: "todoist-sync-api-task-orchestrator"
description: "Orchestrates complex task workflows using the Todoist Sync API v9 with incremental sync via sync_token. Uses commands array for atomic batch operations on items, projects, and labels."
verification: "security_reviewed"
source: "https://developer.todoist.com/api/v1/"
author: "Doist"
category: "Calendar, Email & Productivity"
framework: "Gemini"
---

# Todoist Sync API Task Orchestrator

Orchestrates complex task workflows using the Todoist Sync API v9 with incremental sync via sync_token. Uses commands array for atomic batch operations on items, projects, and labels.

## Installation

Use the upstream install or setup path that matches your environment:
- npx -y mcp-remote https://ai.todoist.net/mcp

Requirements and caveats from upstream:
- Our Python and JavaScript SDKs streamline working with the Todoist API, and
- Todoist Python SDK
- In order to fetch both types of reminders you must include both resource types in your request, for example: resource_types=["reminders", "reminders_location"] .

Basic usage or getting-started notes:
- Deadlines Example deadline object
- Example: Fetching All Tasks
- placeholder ID with a tmp- prefix — for example

- Source: https://developer.todoist.com/api/v1/

## Documentation

- https://developer.todoist.com/api/v1/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/todoist-sync-api-task-orchestrator/)
