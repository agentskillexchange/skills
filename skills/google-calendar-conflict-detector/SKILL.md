---
title: "Google Calendar Conflict Detector"
description: "Detects scheduling conflicts across multiple Google Calendars using the Google Calendar API v3 and the freebusy query endpoint. Posts calendar IDs and a time range to /calendar/v3/freeBusy, parses overlapping busy slots, and returns structured conflict reports. Supports service account authentication via the googleapis Node.js client library."
verification: "security_reviewed"
source: "https://developers.google.com/workspace/calendar/api/guides/overview"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Gemini"
---

# Google Calendar Conflict Detector

This skill detects meeting conflicts across multiple Google Calendars using the Google Calendar API v3. It submits a FreeBusy query to the /calendar/v3/freeBusy endpoint with a list of calendar IDs and a time window, then parses the nested busy arrays to identify overlapping intervals using an interval merge algorithm. Authentication uses service account credentials via the googleapis Node.js client library with the calendar.readonly scope. The skill supports personal calendars, room resources, and shared team calendars. Conflict reports include the conflicting time slot, affected calendar IDs, and suggested open slots within the same day. It integrates with Google Meet by calling the calendar.events.list endpoint to fetch video conference links for affected meetings. Output formats include JSON, Markdown summary, and iCalendar VEVENT objects. Useful for scheduling assistants, automated meeting planners, and executive assistant agents.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/google-calendar-conflict-detector/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/google-calendar-conflict-detector
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/google-calendar-conflict-detector`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-conflict-detector/)
