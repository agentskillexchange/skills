---
title: "Microsoft Outlook Calendar Sync Agent"
description: "Synchronizes calendar events bidirectionally using the Microsoft Graph API /me/calendar/events endpoint. Handles delta queries with deltaToken for incremental sync, manages recurrence patterns, and resolves timezone conflicts."
slug: "ms-outlook-calendar-sync-agent"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ms-outlook-calendar-sync-agent/"
---

# Microsoft Outlook Calendar Sync Agent

Synchronizes calendar events bidirectionally using the Microsoft Graph API /me/calendar/events endpoint. Handles delta queries with deltaToken for incremental sync, manages recurrence patterns, and resolves timezone conflicts.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install ms-outlook-calendar-sync-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Microsoft Outlook Calendar Sync Agent provides bidirectional calendar synchronization using the Microsoft Graph API. It manages events across multiple calendars using /me/calendars and /me/calendar/events endpoints with full CRUD operations.
The skill implements efficient incremental sync using Graph API delta queries (/me/calendarView/delta) with deltaToken and skipToken pagination. Initial sync fetches the complete event set, while subsequent calls retrieve only changes since the last sync point, dramatically reducing API calls and bandwidth.
Recurrence management handles complex patterns including weekly with specific days, monthly by day-of-week, yearly patterns, and exception dates via recurrence.pattern and recurrence.range objects. Timezone handling uses Prefer: outlook.timezone headers and resolves conflicts between organizer and attendee timezones. The agent manages attendee responses, tentative/accepted/declined status tracking, and free/busy conflict detection. Supports room and resource booking through findMeetingTimes API with location constraints. Handles cancelled occurrence management for recurring series.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ms-outlook-calendar-sync-agent/)
