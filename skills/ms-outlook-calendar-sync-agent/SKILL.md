---
title: "Microsoft Outlook Calendar Sync Agent"
description: "The Microsoft Outlook Calendar Sync Agent provides bidirectional calendar synchronization using the Microsoft Graph API. It manages events across multiple calendars using /me/calendars and /me/calendar/events endpoints with full CRUD operations. The skill implements efficient incremental sync using Graph API delta queries ( /me/calendarView/delta ) with deltaToken and skipToken pagination. Initial sync fetches the complete event set, while subsequent calls retrieve only changes since the last sync point, dramatically reducing API calls and bandwidth. Recurrence management handles complex patterns including weekly with specific days, monthly by day-of-week, yearly patterns, and exception dates via recurrence.pattern and recurrence.range objects. Timezone handling uses Prefer: outlook.timezone headers and resolves conflicts between organizer and attendee timezones. The agent manages attendee responses, tentative/accepted/declined status tracking, and free/busy conflict detection. Supports room and resource booking through findMeetingTimes API with location constraints. Handles cancelled occurrence management for recurring series."
source: "https://learn.microsoft.com/en-us/graph/outlook-calendar-concept-overview"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Custom Agents"
---

# Microsoft Outlook Calendar Sync Agent

The Microsoft Outlook Calendar Sync Agent provides bidirectional calendar synchronization using the Microsoft Graph API. It manages events across multiple calendars using /me/calendars and /me/calendar/events endpoints with full CRUD operations. The skill implements efficient incremental sync using Graph API delta queries ( /me/calendarView/delta ) with deltaToken and skipToken pagination. Initial sync fetches the complete event set, while subsequent calls retrieve only changes since the last sync point, dramatically reducing API calls and bandwidth. Recurrence management handles complex patterns including weekly with specific days, monthly by day-of-week, yearly patterns, and exception dates via recurrence.pattern and recurrence.range objects. Timezone handling uses Prefer: outlook.timezone headers and resolves conflicts between organizer and attendee timezones. The agent manages attendee responses, tentative/accepted/declined status tracking, and free/busy conflict detection. Supports room and resource booking through findMeetingTimes API with location constraints. Handles cancelled occurrence management for recurring series.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ms-outlook-calendar-sync-agent/)
