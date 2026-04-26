---
title: "Google Calendar Sync Agent"
description: "Synchronizes events across multiple Google Calendar accounts using the Calendar API v3 and OAuth 2.0. Handles recurring events, timezone conversions, and conflict resolution."
verification: "security_reviewed"
source: "https://developers.google.com/calendar/api"
category:
  - "Calendar, Email & Productivity"
framework:
  - "OpenClaw"
---

# Google Calendar Sync Agent

Google Calendar Sync Agent manages bidirectional synchronization across multiple Google Calendar accounts through the Calendar API v3. It uses incremental sync tokens to minimize API quota consumption, processing only changed events since the last sync. The agent handles complex recurring event patterns including RRULE with EXDATE exceptions, properly converting between timezones using the IANA tz database. Conflict resolution supports configurable strategies: last-write-wins, source-priority, or interactive prompting. It manages OAuth 2.0 refresh token rotation across multiple accounts and supports Google Workspace domain-wide delegation for organizational calendars. The tool generates daily agenda summaries, detects double-bookings across synced calendars, and supports color-coding rules based on event source. Push notifications via Google Cloud Pub/Sub enable near-real-time sync.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/google-calendar-sync-agent-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/google-calendar-sync-agent-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/google-calendar-sync-agent-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-sync-agent-2/)
