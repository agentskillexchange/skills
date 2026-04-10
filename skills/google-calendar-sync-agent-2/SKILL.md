---
name: "Google Calendar Sync Agent"
description: "Synchronizes events across multiple Google Calendar accounts using the Calendar API v3 and OAuth 2.0. Handles recurring events, timezone conversions, and conflict resolution."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/google-calendar-sync-agent-2/"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "OpenClaw"
---

# Google Calendar Sync Agent

Google Calendar Sync Agent manages bidirectional synchronization across multiple Google Calendar accounts through the Calendar API v3. It uses incremental sync tokens to minimize API quota consumption, processing only changed events since the last sync. The agent handles complex recurring event patterns including RRULE with EXDATE exceptions, properly converting between timezones using the IANA tz database. Conflict resolution supports configurable strategies: last-write-wins, source-priority, or interactive prompting. It manages OAuth 2.0 refresh token rotation across multiple accounts and supports Google Workspace domain-wide delegation for organizational calendars. The tool generates daily agenda summaries, detects double-bookings across synced calendars, and supports color-coding rules based on event source. Push notifications via Google Cloud Pub/Sub enable near-real-time sync.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-sync-agent-2/)
