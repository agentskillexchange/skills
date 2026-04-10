---
title: "Google Calendar Sync Agent"
description: "Synchronizes events across multiple Google Calendar accounts using the Calendar API v3 and OAuth 2.0. Handles recurring events, timezone conversions, and conflict resolution."
slug: "google-calendar-sync-agent-2"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/google-calendar-sync-agent-2/"
listed: true
---

# Google Calendar Sync Agent

Synchronizes events across multiple Google Calendar accounts using the Calendar API v3 and OAuth 2.0. Handles recurring events, timezone conversions, and conflict resolution.

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
clawhub install google-calendar-sync-agent-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Google Calendar Sync Agent manages bidirectional synchronization across multiple Google Calendar accounts through the Calendar API v3. It uses incremental sync tokens to minimize API quota consumption, processing only changed events since the last sync. The agent handles complex recurring event patterns including RRULE with EXDATE exceptions, properly converting between timezones using the IANA tz database. Conflict resolution supports configurable strategies: last-write-wins, source-priority, or interactive prompting. It manages OAuth 2.0 refresh token rotation across multiple accounts and supports Google Workspace domain-wide delegation for organizational calendars. The tool generates daily agenda summaries, detects double-bookings across synced calendars, and supports color-coding rules based on event source. Push notifications via Google Cloud Pub/Sub enable near-real-time sync.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-sync-agent-2/)
