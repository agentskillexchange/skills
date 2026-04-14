---
title: "Microsoft Outlook Calendar Sync Agent"
description: "Synchronizes calendar events bidirectionally using the Microsoft Graph API /me/calendar/events endpoint. Handles delta queries with deltaToken for incremental sync, manages recurrence patterns, and resolves timezone conflicts."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ms-outlook-calendar-sync-agent/"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Custom Agents"
---

# Microsoft Outlook Calendar Sync Agent

The Microsoft Outlook Calendar Sync Agent provides bidirectional calendar synchronization using the Microsoft Graph API. It manages events across multiple calendars using /me/calendars and /me/calendar/events endpoints with full CRUD operations.

The skill implements efficient incremental sync using Graph API delta queries (/me/calendarView/delta) with deltaToken and skipToken pagination. Initial sync fetches the complete event set, while subsequent calls retrieve only changes since the last sync point, dramatically reducing API calls and bandwidth.

Recurrence management handles complex patterns including weekly with specific days, monthly by day-of-week, yearly patterns, and exception dates via recurrence.pattern and recurrence.range objects. Timezone handling uses Prefer: outlook.timezone headers and resolves conflicts between organizer and attendee timezones. The agent manages attendee responses, tentative/accepted/declined status tracking, and free/busy conflict detection. Supports room and resource booking through findMeetingTimes API with location constraints. Handles cancelled occurrence management for recurring series.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ms-outlook-calendar-sync-agent/)
