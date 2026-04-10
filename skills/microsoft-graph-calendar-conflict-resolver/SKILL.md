---
title: "Microsoft Graph Calendar Conflict Resolver"
description: "Resolves scheduling collisions with Microsoft Graph Calendar endpoints like `/me/events`, `/calendarView`, and `findMeetingTimes`. Useful for agents that need to compare attendees, constraints, and availability before proposing a meeting move."
slug: "microsoft-graph-calendar-conflict-resolver"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://learn.microsoft.com/en-us/graph/"
listed: true
---

# Microsoft Graph Calendar Conflict Resolver

Resolves scheduling collisions with Microsoft Graph Calendar endpoints like `/me/events`, `/calendarView`, and `findMeetingTimes`. Useful for agents that need to compare attendees, constraints, and availability before proposing a meeting move.

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
clawhub install microsoft-graph-calendar-conflict-resolver
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Microsoft Graph Calendar Conflict Resolver helps agents work through the real complexity of calendar scheduling instead of simply listing open slots. It uses Microsoft Graph endpoints such as /me/events, /calendarView, and findMeetingTimes to inspect current bookings, proposed times, and participant availability. That makes it a good fit when a meeting overlaps with higher-priority events, a room or organizer is double-booked, or a reschedule needs to respect multiple attendees and time constraints.
The skill can compare event windows, account for existing holds, and explain why a suggested move works better than the current slot. It is particularly valuable in Outlook-heavy environments where agents need to stay inside Graph’s event model rather than inventing their own scheduling logic. By leaning on real event objects and free/busy-compatible availability, the workflow stays reproducible and easier to audit.
Use this skill when calendar coordination needs more than a basic free/busy lookup and when proposed changes should be backed by Microsoft Graph data rather than guesswork.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-calendar-conflict-resolver/)
