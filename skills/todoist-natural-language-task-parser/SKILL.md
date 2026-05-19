---
name: "Todoist Natural Language Task Parser"
slug: "todoist-natural-language-task-parser"
description: "Parses natural language task descriptions into structured Todoist API v2 task objects with due dates, priority levels, and project assignments. Uses the Todoist Sync API for batch task creation and supports recurring date patterns via the RRule specification."
verification: "security_reviewed"
source: "https://developer.todoist.com/api/v1/"
author: "Doist"
category: "Calendar, Email & Productivity"
framework: "MCP"
---

# Todoist Natural Language Task Parser

Parses natural language task descriptions into structured Todoist API v2 task objects with due dates, priority levels, and project assignments. Uses the Todoist Sync API for batch task creation and supports recurring date patterns via the RRule specification.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/todoist-natural-language-task-parser/)
