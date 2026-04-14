---
title: "Google Calendar Sync & Conflict Resolver"
description: "Bidirectional calendar synchronization using Google Calendar API v3 with OAuth 2.0. Detects scheduling conflicts across multiple calendars, suggests optimal meeting times using FreeBusy API queries."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/google-calendar-sync-conflict-resolver/"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "OpenClaw"
---

# Google Calendar Sync & Conflict Resolver

The Google Calendar Sync & Conflict Resolver provides intelligent calendar management through the Google Calendar API v3. It monitors multiple calendar sources for changes using push notifications via the Calendar Watch API and synchronizes events bidirectionally with conflict detection.

Conflict resolution uses the FreeBusy API to query availability across all connected calendars, identifying overlapping events and suggesting alternative time slots based on configurable preferences (preferred hours, buffer time between meetings, maximum daily meeting load). The suggestion engine considers attendee availability across organizations using cross-domain FreeBusy queries.

Event synchronization handles complex scenarios including recurring event modifications (single instance vs. series changes), timezone conversions using the IANA timezone database, all-day event normalization, and attachment syncing via Google Drive API. Delta sync uses incremental sync tokens to minimize API quota usage.

The skill includes natural language event creation using the Events.quickAdd endpoint, smart scheduling that respects working hours and focus time blocks, and automated RSVP management based on configurable rules (auto-accept from certain organizers, auto-decline during focus blocks).

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-sync-conflict-resolver/)
