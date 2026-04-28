---
title: Microsoft Graph Calendar Conflict Resolver
description: Resolves scheduling collisions with Microsoft Graph Calendar endpoints
  like `/me/events`, `/calendarView`, and `findMeetingTimes`. Useful for agents that
  need to compare attendees, constraints, and availability before proposing a meeting
  move.
verification: security_reviewed
source: https://learn.microsoft.com/en-us/graph/
category:
- Calendar, Email & Productivity
framework:
- Claude Agents
---

# Microsoft Graph Calendar Conflict Resolver

Resolves scheduling collisions with Microsoft Graph Calendar endpoints like `/me/events`, `/calendarView`, and `findMeetingTimes`. Useful for agents that need to compare attendees, constraints, and availability before proposing a meeting move.

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
