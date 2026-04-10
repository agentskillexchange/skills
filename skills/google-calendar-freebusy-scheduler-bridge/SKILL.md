---
name: Google Calendar FreeBusy Scheduler Bridge
description: Coordinates meeting suggestions with the Google Calendar `freeBusy` endpoint,
  Events resource, and conferenceData fields for cleaner scheduling handoffs. Great
  for agents that need to compare availability, hold windows, and meeting metadata
  before creating or moving events.
verification: security_reviewed
source: https://developers.google.com/calendar/api
category:
- Calendar, Email &amp; Productivity
framework:
- Cursor
---
# Google Calendar FreeBusy Scheduler Bridge

Google Calendar FreeBusy Scheduler Bridge gives agents a more dependable scheduling workflow than simply proposing the next open hour on a calendar. It works with the Google Calendar API’s freeBusy endpoint, the Events resource, and conference data fields to compare availability, inspect event metadata, and prepare clean scheduling suggestions. That is useful when multiple people, time zones, and meeting formats all affect whether a slot is actually workable.
The skill can look at current commitments, protected time, and existing event structures before suggesting a hold or a move. It is also helpful when a workflow needs to preserve conference links, attendee lists, and event descriptions rather than treating scheduling as a bare time-range problem. Because the logic is based on Google Calendar’s own availability and event objects, it stays compatible with how the calendar is really used.
Use this skill when agents need to bridge availability checks with event-aware scheduling, especially in teams where meetings are frequently rescheduled and metadata continuity matters.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-freebusy-scheduler-bridge/)
