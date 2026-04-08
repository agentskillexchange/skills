---
title: Google Calendar Sync Agent
description: 'Google Calendar Sync Agent manages bidirectional synchronization across
  multiple Google Calendar accounts through the Calendar API v3. It uses incremental
  sync tokens to minimize API quota consumption, processing only changed events since
  the last sync. The agent handles complex recurring event patterns including RRULE
  with EXDATE exceptions, properly converting between timezones using the IANA tz
  database. Conflict resolution supports configurable strategies: last-write-wins,
  source-priority, or interactive prompting. It manages OAuth 2.0 refresh token rotation
  across multiple accounts and supports Google Workspace domain-wide delegation for
  organizational calendars. The tool generates daily agenda summaries, detects double-bookings
  across synced calendars, and supports color-coding rules based on event source.
  Push notifications via Google Cloud Pub/Sub enable near-real-time sync.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/google-calendar-sync-agent-2/
category:
- Calendar, Email &amp; Productivity
framework:
- OpenClaw
---

# Google Calendar Sync Agent

Google Calendar Sync Agent manages bidirectional synchronization across multiple Google Calendar accounts through the Calendar API v3. It uses incremental sync tokens to minimize API quota consumption, processing only changed events since the last sync. The agent handles complex recurring event patterns including RRULE with EXDATE exceptions, properly converting between timezones using the IANA tz database. Conflict resolution supports configurable strategies: last-write-wins, source-priority, or interactive prompting. It manages OAuth 2.0 refresh token rotation across multiple accounts and supports Google Workspace domain-wide delegation for organizational calendars. The tool generates daily agenda summaries, detects double-bookings across synced calendars, and supports color-coding rules based on event source. Push notifications via Google Cloud Pub/Sub enable near-real-time sync.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-sync-agent-2/)
