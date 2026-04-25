---
title: "Turn ICS calendar invites and feeds into structured events for scheduling automations"
description: "Use node-ical when an agent is handed a raw .ics file or subscription URL and needs normalized event objects, recurrence-aware dates, and timezone-safe fields it can reason over. The skill stops at parsing and structuring calendar data, not acting as a full calendar product."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/node-ical"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  npm_package: "node-ical"
  npm_weekly_downloads: 128582
---

# Turn ICS calendar invites and feeds into structured events for scheduling automations

This skill uses node-ical, an iCalendar and ICS parser for Node.js that turns calendar files and feed URLs into structured event data. It is a good fit for agents that need to read meeting invites, subscribed calendars, or exported schedules and then do something useful with the parsed result. Instead of treating an ICS attachment like opaque text, the agent can extract event names, start and end times, recurrence rules, locations, descriptions, organizers, and other calendar fields in a machine-usable form. The concrete job-to-be-done is calendar parsing for automation. Invoke this skill when the agent already has an .ics file, raw iCalendar payload, or remote calendar URL and needs structured events for scheduling logic, reminder generation, availability summaries, itinerary building, or sync pipelines. node-ical exposes synchronous and asynchronous parsing paths and supports real RFC 5545 calendar data, which makes it useful for inbox assistants, booking workflows, event-ingestion pipelines, and internal scheduling bots that need normalized event objects rather than brittle regex extraction. The scope boundary keeps this skill honest: node-ical parses and normalizes calendar data, but it does not own the calendar, send invitations, manage permissions, or replace Google Calendar, Outlook, or CalDAV systems. It is the right layer when an agent needs to read calendar data safely before another system decides what to do next. Integration points include webhook consumers, email processors, queue workers, booking automations, and schedule sync tools built on Node.js.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/turn-ics-calendar-invites-and-feeds-into-structured-events-for-scheduling-automations/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/turn-ics-calendar-invites-and-feeds-into-structured-events-for-scheduling-automations
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/turn-ics-calendar-invites-and-feeds-into-structured-events-for-scheduling-automations`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-ics-calendar-invites-and-feeds-into-structured-events-for-scheduling-automations/)
