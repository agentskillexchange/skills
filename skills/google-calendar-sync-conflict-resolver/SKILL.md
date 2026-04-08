---
title: Google Calendar Sync & Conflict Resolver
description: The Google Calendar Sync & Conflict Resolver provides intelligent calendar
  management through the Google Calendar API v3. It monitors multiple calendar sources
  for changes using push notifications via the Calendar Watch API and synchronizes
  events bidirectionally with conflict detection. Conflict resolution uses the FreeBusy
  API to query availability across all connected calendars, identifying overlapping
  events and suggesting alternative time slots based on configurable preferences (preferred
  hours, buffer time between meetings, maximum daily meeting load). The suggestion
  engine considers attendee availability across organizations using cross-domain FreeBusy
  queries. Event synchronization handles complex scenarios including recurring event
  modifications (single instance vs. series changes), timezone conversions using the
  IANA timezone database, all-day event normalization, and attachment syncing via
  Google Drive API. Delta sync uses incremental sync tokens to minimize API quota
  usage. The skill includes natural language event creation using the Events.quickAdd
  endpoint, smart scheduling that respects working hours and focus time blocks, and
  automated RSVP management based on configurable rules (auto-accept from certain
  organizers, auto-decline during focus blocks).
verification: security_reviewed
source: https://agentskillexchange.com/skills/google-calendar-sync-conflict-resolver/
category:
- Calendar, Email &amp; Productivity
framework:
- OpenClaw
---

# Google Calendar Sync & Conflict Resolver

The Google Calendar Sync & Conflict Resolver provides intelligent calendar management through the Google Calendar API v3. It monitors multiple calendar sources for changes using push notifications via the Calendar Watch API and synchronizes events bidirectionally with conflict detection. Conflict resolution uses the FreeBusy API to query availability across all connected calendars, identifying overlapping events and suggesting alternative time slots based on configurable preferences (preferred hours, buffer time between meetings, maximum daily meeting load). The suggestion engine considers attendee availability across organizations using cross-domain FreeBusy queries. Event synchronization handles complex scenarios including recurring event modifications (single instance vs. series changes), timezone conversions using the IANA timezone database, all-day event normalization, and attachment syncing via Google Drive API. Delta sync uses incremental sync tokens to minimize API quota usage. The skill includes natural language event creation using the Events.quickAdd endpoint, smart scheduling that respects working hours and focus time blocks, and automated RSVP management based on configurable rules (auto-accept from certain organizers, auto-decline during focus blocks).

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-sync-conflict-resolver/)
