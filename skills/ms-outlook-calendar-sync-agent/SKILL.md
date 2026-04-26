---
title: "Microsoft Outlook Calendar Sync Agent"
description: "Synchronizes calendar events bidirectionally using the Microsoft Graph API /me/calendar/events endpoint. Handles delta queries with deltaToken for incremental sync, manages recurrence patterns, and resolves timezone conflicts."
verification: "security_reviewed"
source: "https://learn.microsoft.com/en-us/graph/outlook-calendar-concept-overview"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Custom Agents"
---

# Microsoft Outlook Calendar Sync Agent

Synchronizes calendar events bidirectionally using the Microsoft Graph API /me/calendar/events endpoint. Handles delta queries with deltaToken for incremental sync, manages recurrence patterns, and resolves timezone conflicts.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/ms-outlook-calendar-sync-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ms-outlook-calendar-sync-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/ms-outlook-calendar-sync-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ms-outlook-calendar-sync-agent/)
