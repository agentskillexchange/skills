---
title: "Microsoft Graph Calendar Conflict Resolver"
description: "Resolves scheduling collisions with Microsoft Graph Calendar endpoints like `/me/events`, `/calendarView`, and `findMeetingTimes`. Useful for agents that need to compare attendees, constraints, and availability before proposing a meeting move."
verification: "security_reviewed"
source: "https://learn.microsoft.com/en-us/graph/"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Claude Agents"
---

# Microsoft Graph Calendar Conflict Resolver

Microsoft Graph Calendar Conflict Resolver helps agents work through the real complexity of calendar scheduling instead of simply listing open slots. It uses Microsoft Graph endpoints such as /me/events, /calendarView, and findMeetingTimes to inspect current bookings, proposed times, and participant availability. That makes it a good fit when a meeting overlaps with higher-priority events, a room or organizer is double-booked, or a reschedule needs to respect multiple attendees and time constraints. The skill can compare event windows, account for existing holds, and explain why a suggested move works better than the current slot. It is particularly valuable in Outlook-heavy environments where agents need to stay inside Graph’s event model rather than inventing their own scheduling logic. By leaning on real event objects and free/busy-compatible availability, the workflow stays reproducible and easier to audit. Use this skill when calendar coordination needs more than a basic free/busy lookup and when proposed changes should be backed by Microsoft Graph data rather than guesswork.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/microsoft-graph-calendar-conflict-resolver/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/microsoft-graph-calendar-conflict-resolver
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/microsoft-graph-calendar-conflict-resolver`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-calendar-conflict-resolver/)
