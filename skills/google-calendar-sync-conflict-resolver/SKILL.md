---
title: "Google Calendar Sync & Conflict Resolver"
description: "Bidirectional calendar synchronization using Google Calendar API v3 with OAuth 2.0. Detects scheduling conflicts across multiple calendars, suggests optimal meeting times using FreeBusy API queries."
slug: "google-calendar-sync-conflict-resolver"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/google-calendar-sync-conflict-resolver/"
---

# Google Calendar Sync & Conflict Resolver

Bidirectional calendar synchronization using Google Calendar API v3 with OAuth 2.0. Detects scheduling conflicts across multiple calendars, suggests optimal meeting times using FreeBusy API queries.

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
clawhub install google-calendar-sync-conflict-resolver
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Google Calendar Sync & Conflict Resolver provides intelligent calendar management through the Google Calendar API v3. It monitors multiple calendar sources for changes using push notifications via the Calendar Watch API and synchronizes events bidirectionally with conflict detection.
Conflict resolution uses the FreeBusy API to query availability across all connected calendars, identifying overlapping events and suggesting alternative time slots based on configurable preferences (preferred hours, buffer time between meetings, maximum daily meeting load). The suggestion engine considers attendee availability across organizations using cross-domain FreeBusy queries.
Event synchronization handles complex scenarios including recurring event modifications (single instance vs. series changes), timezone conversions using the IANA timezone database, all-day event normalization, and attachment syncing via Google Drive API. Delta sync uses incremental sync tokens to minimize API quota usage.
The skill includes natural language event creation using the Events.quickAdd endpoint, smart scheduling that respects working hours and focus time blocks, and automated RSVP management based on configurable rules (auto-accept from certain organizers, auto-decline during focus blocks).

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-sync-conflict-resolver/)
