---
name: "Microsoft Graph Calendar Conflict Resolver"
description: "Resolves scheduling collisions with Microsoft Graph Calendar endpoints like `/me/events`, `/calendarView`, and `findMeetingTimes`. Useful for agents that need to compare attendees, constraints, and availability before proposing a meeting move."
category: "Calendar, Email & Productivity"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/microsoft-graph-calendar-conflict-resolver/"
---

# Microsoft Graph Calendar Conflict Resolver

Resolves scheduling collisions with Microsoft Graph Calendar endpoints like `/me/events`, `/calendarView`, and `findMeetingTimes`. Useful for agents that need to compare attendees, constraints, and availability before proposing a meeting move.

## Overview

Microsoft Graph Calendar Conflict Resolver helps agents work through the real complexity of calendar scheduling instead of simply listing open slots. It uses Microsoft Graph endpoints such as `/me/events`, `/calendarView`, and `findMeetingTimes` to inspect current bookings, proposed times, and participant availability. That makes it a good fit when a meeting overlaps with higher-priority events, a room or organizer is double-booked, or a reschedule needs to respect multiple attendees and time constraints.

The skill can compare event windows, account for existing holds, and explain why a suggested move works better than the current slot. It is particularly valuable in Outlook-heavy environments where agents need to stay inside Graph’s event model rather than inventing their own scheduling logic. By leaning on real event objects and free/busy-compatible availability, the workflow stays reproducible and easier to audit.

Use this skill when calendar coordination needs more than a basic free/busy lookup and when proposed changes should be backed by Microsoft Graph data rather than guesswork.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-calendar-conflict-resolver
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-calendar-conflict-resolver -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-calendar-conflict-resolver -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-calendar-conflict-resolver -a codex
```

### OpenClaw

```bash
clawhub install microsoft-graph-calendar-conflict-resolver
```

## Source

- Marketplace: https://agentskillexchange.com/skills/microsoft-graph-calendar-conflict-resolver/
