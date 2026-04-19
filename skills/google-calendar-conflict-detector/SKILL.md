---
title: "Google Calendar Conflict Detector"
description: "This skill detects meeting conflicts across multiple Google Calendars using the Google Calendar API v3. It submits a FreeBusy query to the /calendar/v3/freeBusy endpoint with a list of calendar IDs and a time window, then parses the nested busy arrays to identify overlapping intervals using an interval merge algorithm. Authentication uses service account credentials via the googleapis Node.js client library with the calendar.readonly scope. The skill supports personal calendars, room resources, and shared team calendars. Conflict reports include the conflicting time slot, affected calendar IDs, and suggested open slots within the same day. It integrates with Google Meet by calling the calendar.events.list endpoint to fetch video conference links for affected meetings. Output formats include JSON, Markdown summary, and iCalendar VEVENT objects. Useful for scheduling assistants, automated meeting planners, and executive assistant agents."
source: "https://developers.google.com/workspace/calendar/api/guides/overview"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Gemini"
---

# Google Calendar Conflict Detector

This skill detects meeting conflicts across multiple Google Calendars using the Google Calendar API v3. It submits a FreeBusy query to the /calendar/v3/freeBusy endpoint with a list of calendar IDs and a time window, then parses the nested busy arrays to identify overlapping intervals using an interval merge algorithm. Authentication uses service account credentials via the googleapis Node.js client library with the calendar.readonly scope. The skill supports personal calendars, room resources, and shared team calendars. Conflict reports include the conflicting time slot, affected calendar IDs, and suggested open slots within the same day. It integrates with Google Meet by calling the calendar.events.list endpoint to fetch video conference links for affected meetings. Output formats include JSON, Markdown summary, and iCalendar VEVENT objects. Useful for scheduling assistants, automated meeting planners, and executive assistant agents.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-conflict-detector/)
