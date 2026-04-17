---
name: Microsoft Outlook Calendar Sync Agent
description: Synchronizes calendar events bidirectionally using the Microsoft Graph
  API /me/calendar/events endpoint. Handles delta queries with deltaToken for incremental
  sync, manages recurrence patterns, and resolves timezone conflicts.
category: Calendar, Email & Productivity
framework: Custom Agents
verification: security_reviewed
source: https://learn.microsoft.com/en-us/graph/outlook-calendar-concept-overview
---
# Microsoft Outlook Calendar Sync Agent
Synchronizes calendar events bidirectionally using the Microsoft Graph API /me/calendar/events endpoint. Handles delta queries with deltaToken for incremental sync, manages recurrence patterns, and resolves timezone conflicts.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ms-outlook-calendar-sync-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/ms-outlook-calendar-sync-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ms-outlook-calendar-sync-agent/)
