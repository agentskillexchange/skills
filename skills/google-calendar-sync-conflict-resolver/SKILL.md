---
title: "Google Calendar Sync &#038; Conflict Resolver"
description: "The Google Calendar Sync &#038; Conflict Resolver provides intelligent calendar management through the Google Calendar API v3. It monitors multiple calendar sources for changes using push notifications via the Calendar Watch API and synchronizes events bidirectionally with conflict detection. Conflict resolution uses the FreeBusy API to query availability across all connected calendars, identifying overlapping events and suggesting alternative time slots based on configurable preferences (preferred hours, buffer time between meetings, maximum daily meeting load). The suggestion engine considers attendee availability across organizations using cross-domain FreeBusy queries. Event synchronization handles complex scenarios including recurring event modifications (single instance vs. series changes), timezone conversions using the IANA timezone database, all-day event normalization, and attachment syncing via Google Drive API. Delta sync uses incremental sync tokens to minimize API quota usage. The skill includes natural language event creation using the Events.quickAdd endpoint, smart scheduling that respects working hours and focus time blocks, and automated RSVP management based on configurable rules (auto-accept from certain organizers, auto-decline during focus blocks)."
source: "https://agentskillexchange.com/skills/google-calendar-sync-conflict-resolver/"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "OpenClaw"
---

# Google Calendar Sync &#038; Conflict Resolver

The Google Calendar Sync &#038; Conflict Resolver provides intelligent calendar management through the Google Calendar API v3. It monitors multiple calendar sources for changes using push notifications via the Calendar Watch API and synchronizes events bidirectionally with conflict detection. Conflict resolution uses the FreeBusy API to query availability across all connected calendars, identifying overlapping events and suggesting alternative time slots based on configurable preferences (preferred hours, buffer time between meetings, maximum daily meeting load). The suggestion engine considers attendee availability across organizations using cross-domain FreeBusy queries. Event synchronization handles complex scenarios including recurring event modifications (single instance vs. series changes), timezone conversions using the IANA timezone database, all-day event normalization, and attachment syncing via Google Drive API. Delta sync uses incremental sync tokens to minimize API quota usage. The skill includes natural language event creation using the Events.quickAdd endpoint, smart scheduling that respects working hours and focus time blocks, and automated RSVP management based on configurable rules (auto-accept from certain organizers, auto-decline during focus blocks).

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-sync-conflict-resolver/)
