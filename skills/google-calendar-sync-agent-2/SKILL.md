---
title: "Google Calendar Sync Agent"
description: "Google Calendar Sync Agent manages bidirectional synchronization across multiple Google Calendar accounts through the Calendar API v3. It uses incremental sync tokens to minimize API quota consumption, processing only changed events since the last sync. The agent handles complex recurring event patterns including RRULE with EXDATE exceptions, properly converting between timezones using the IANA tz database. Conflict resolution supports configurable strategies: last-write-wins, source-priority, or interactive prompting. It manages OAuth 2.0 refresh token rotation across multiple accounts and supports Google Workspace domain-wide delegation for organizational calendars. The tool generates daily agenda summaries, detects double-bookings across synced calendars, and supports color-coding rules based on event source. Push notifications via Google Cloud Pub/Sub enable near-real-time sync."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/google-calendar-sync-agent-2/"
framework:
  - "OpenClaw"
---

# Google Calendar Sync Agent

Google Calendar Sync Agent manages bidirectional synchronization across multiple Google Calendar accounts through the Calendar API v3. It uses incremental sync tokens to minimize API quota consumption, processing only changed events since the last sync. The agent handles complex recurring event patterns including RRULE with EXDATE exceptions, properly converting between timezones using the IANA tz database. Conflict resolution supports configurable strategies: last-write-wins, source-priority, or interactive prompting. It manages OAuth 2.0 refresh token rotation across multiple accounts and supports Google Workspace domain-wide delegation for organizational calendars. The tool generates daily agenda summaries, detects double-bookings across synced calendars, and supports color-coding rules based on event source. Push notifications via Google Cloud Pub/Sub enable near-real-time sync.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/google-calendar-sync-agent-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/google-calendar-sync-agent-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-sync-agent-2/)
