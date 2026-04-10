---
name: "Microsoft Graph Calendar Conflict Resolver"
description: "Resolves scheduling collisions with Microsoft Graph Calendar endpoints like `/me/events`, `/calendarView`, and `findMeetingTimes`. Useful for agents that need to compare attendees, constraints, and availability before proposing a meeting move."
verification: security_reviewed
source: "https://learn.microsoft.com/en-us/graph/"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Claude Agents"
---

# Microsoft Graph Calendar Conflict Resolver

Microsoft Graph Calendar Conflict Resolver helps agents work through the real complexity of calendar scheduling instead of simply listing open slots. It uses Microsoft Graph endpoints such as /me/events, /calendarView, and findMeetingTimes to inspect current bookings, proposed times, and participant availability. That makes it a good fit when a meeting overlaps with higher-priority events, a room or organizer is double-booked, or a reschedule needs to respect multiple attendees and time constraints.
The skill can compare event windows, account for existing holds, and explain why a suggested move works better than the current slot. It is particularly valuable in Outlook-heavy environments where agents need to stay inside Graph’s event model rather than inventing their own scheduling logic. By leaning on real event objects and free/busy-compatible availability, the workflow stays reproducible and easier to audit.
Use this skill when calendar coordination needs more than a basic free/busy lookup and when proposed changes should be backed by Microsoft Graph data rather than guesswork.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-calendar-conflict-resolver/)
