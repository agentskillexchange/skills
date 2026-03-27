---
name: "Google Calendar FreeBusy Scheduler Bridge"
description: "Coordinates meeting suggestions with the Google Calendar `freeBusy` endpoint, Events resource, and conferenceData fields for cleaner scheduling handoffs. Great for agents that need to compare availability, hold windows, and meeting metadata before creating or moving events."
category: "Calendar, Email & Productivity"
framework: "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/google-calendar-freebusy-scheduler-bridge/"
---

# Google Calendar FreeBusy Scheduler Bridge

Coordinates meeting suggestions with the Google Calendar `freeBusy` endpoint, Events resource, and conferenceData fields for cleaner scheduling handoffs. Great for agents that need to compare availability, hold windows, and meeting metadata before creating or moving events.

## Overview

Google Calendar FreeBusy Scheduler Bridge gives agents a more dependable scheduling workflow than simply proposing the next open hour on a calendar. It works with the Google Calendar API’s `freeBusy` endpoint, the Events resource, and conference data fields to compare availability, inspect event metadata, and prepare clean scheduling suggestions. That is useful when multiple people, time zones, and meeting formats all affect whether a slot is actually workable.

The skill can look at current commitments, protected time, and existing event structures before suggesting a hold or a move. It is also helpful when a workflow needs to preserve conference links, attendee lists, and event descriptions rather than treating scheduling as a bare time-range problem. Because the logic is based on Google Calendar’s own availability and event objects, it stays compatible with how the calendar is really used.

Use this skill when agents need to bridge availability checks with event-aware scheduling, especially in teams where meetings are frequently rescheduled and metadata continuity matters.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill google-calendar-freebusy-scheduler-bridge
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill google-calendar-freebusy-scheduler-bridge -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill google-calendar-freebusy-scheduler-bridge -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill google-calendar-freebusy-scheduler-bridge -a codex
```

### OpenClaw

```bash
clawhub install google-calendar-freebusy-scheduler-bridge
```

## Source

- Marketplace: https://agentskillexchange.com/skills/google-calendar-freebusy-scheduler-bridge/
