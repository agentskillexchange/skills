---
title: "Turn ICS calendar invites and feeds into structured events for scheduling automations"
description: "This skill uses node-ical , an iCalendar and ICS parser for Node.js that turns calendar files and feed URLs into structured event data. It is a good fit for agents that need to read meeting invites, subscribed calendars, or exported schedules and then do something useful with the parsed result. Instead of treating an ICS attachment like opaque text, the agent can extract event names, start and end times, recurrence rules, locations, descriptions, organizers, and other calendar fields in a machine-usable form. The concrete job-to-be-done is calendar parsing for automation. Invoke this skill when the agent already has an .ics file, raw iCalendar payload, or remote calendar URL and needs structured events for scheduling logic, reminder generation, availability summaries, itinerary building, or sync pipelines. node-ical exposes synchronous and asynchronous parsing paths and supports real RFC 5545 calendar data, which makes it useful for inbox assistants, booking workflows, event-ingestion pipelines, and internal scheduling bots that need normalized event objects rather than brittle regex extraction. The scope boundary keeps this skill honest: node-ical parses and normalizes calendar data, but it does not own the calendar, send invitations, manage permissions, or replace Google Calendar, Outlook, or CalDAV systems. It is the right layer when an agent needs to read calendar data safely before another system decides what to do next. Integration points include webhook consumers, email processors, queue workers, booking automations, and schedule sync tools built on Node.js."
source: "https://www.npmjs.com/package/node-ical"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  npm_package: "node-ical"
  npm_weekly_downloads: 128582
---

# Turn ICS calendar invites and feeds into structured events for scheduling automations

This skill uses node-ical , an iCalendar and ICS parser for Node.js that turns calendar files and feed URLs into structured event data. It is a good fit for agents that need to read meeting invites, subscribed calendars, or exported schedules and then do something useful with the parsed result. Instead of treating an ICS attachment like opaque text, the agent can extract event names, start and end times, recurrence rules, locations, descriptions, organizers, and other calendar fields in a machine-usable form. The concrete job-to-be-done is calendar parsing for automation. Invoke this skill when the agent already has an .ics file, raw iCalendar payload, or remote calendar URL and needs structured events for scheduling logic, reminder generation, availability summaries, itinerary building, or sync pipelines. node-ical exposes synchronous and asynchronous parsing paths and supports real RFC 5545 calendar data, which makes it useful for inbox assistants, booking workflows, event-ingestion pipelines, and internal scheduling bots that need normalized event objects rather than brittle regex extraction. The scope boundary keeps this skill honest: node-ical parses and normalizes calendar data, but it does not own the calendar, send invitations, manage permissions, or replace Google Calendar, Outlook, or CalDAV systems. It is the right layer when an agent needs to read calendar data safely before another system decides what to do next. Integration points include webhook consumers, email processors, queue workers, booking automations, and schedule sync tools built on Node.js.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-ics-calendar-invites-and-feeds-into-structured-events-for-scheduling-automations/)
