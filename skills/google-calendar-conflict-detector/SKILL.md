---
title: Google Calendar Conflict Detector
description: This skill detects meeting conflicts across multiple Google Calendars
  using the Google Calendar API v3. It submits a FreeBusy query to the /calendar/v3/freeBusy
  endpoint with a list of calendar IDs and a time window, then parses the nested busy
  arrays to identify overlapping intervals using an interval merge algorithm. Authentication
  uses service account credentials via the googleapis Node.js client library with
  the calendar.readonly scope. The skill supports personal calendars, room resources,
  and shared team calendars. Conflict reports include the conflicting time slot, affected
  calendar IDs, and suggested open slots within the same day. It integrates with Google
  Meet by calling the calendar.events.list endpoint to fetch video conference links
  for affected meetings. Output formats include JSON, Markdown summary, and iCalendar
  VEVENT objects. Useful for scheduling assistants, automated meeting planners, and
  executive assistant agents.
verification: security_reviewed
source: https://agentskillexchange.com/skills/google-calendar-conflict-detector/
category:
- Calendar, Email &amp; Productivity
framework:
- Gemini
---

# Google Calendar Conflict Detector

This skill detects meeting conflicts across multiple Google Calendars using the Google Calendar API v3. It submits a FreeBusy query to the /calendar/v3/freeBusy endpoint with a list of calendar IDs and a time window, then parses the nested busy arrays to identify overlapping intervals using an interval merge algorithm. Authentication uses service account credentials via the googleapis Node.js client library with the calendar.readonly scope. The skill supports personal calendars, room resources, and shared team calendars. Conflict reports include the conflicting time slot, affected calendar IDs, and suggested open slots within the same day. It integrates with Google Meet by calling the calendar.events.list endpoint to fetch video conference links for affected meetings. Output formats include JSON, Markdown summary, and iCalendar VEVENT objects. Useful for scheduling assistants, automated meeting planners, and executive assistant agents.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-conflict-detector/)
