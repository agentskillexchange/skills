---
title: "Microsoft Outlook Calendar Sync Agent"
description: "Synchronizes calendar events bidirectionally using the Microsoft Graph API /me/calendar/events endpoint. Handles delta queries with deltaToken for incremental sync, manages recurrence patterns, and resolves timezone conflicts."
verification: security_reviewed
source: "https://learn.microsoft.com/en-us/graph/outlook-calendar-concept-overview"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Custom Agents"
---

# Microsoft Outlook Calendar Sync Agent

The Microsoft Outlook Calendar Sync Agent provides bidirectional calendar synchronization using the Microsoft Graph API. It manages events across multiple calendars using /me/calendars and /me/calendar/events endpoints with full CRUD operations.

The skill implements efficient incremental sync using Graph API delta queries (/me/calendarView/delta) with deltaToken and skipToken pagination. Initial sync fetches the complete event set, while subsequent calls retrieve only changes since the last sync point, dramatically reducing API calls and bandwidth.

Recurrence management handles complex patterns including weekly with specific days, monthly by day-of-week, yearly patterns, and exception dates via recurrence.pattern and recurrence.range objects. Timezone handling uses Prefer: outlook.timezone headers and resolves conflicts between organizer and attendee timezones. The agent manages attendee responses, tentative/accepted/declined status tracking, and free/busy conflict detection. Supports room and resource booking through findMeetingTimes API with location constraints. Handles cancelled occurrence management for recurring series.

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
