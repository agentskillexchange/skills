---
title: "Google Calendar Conflict Detector"
description: "Detects scheduling conflicts across multiple Google Calendars using the Google Calendar API v3 and the freebusy query endpoint. Posts calendar IDs and a time range to /calendar/v3/freeBusy, parses overlapping busy slots, and returns structured conflict reports. Supports service account authentication via the googleapis Node.js client library."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/google-calendar-conflict-detector/"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Gemini"
---

# Google Calendar Conflict Detector

This skill detects meeting conflicts across multiple Google Calendars using the Google Calendar API v3. It submits a FreeBusy query to the /calendar/v3/freeBusy endpoint with a list of calendar IDs and a time window, then parses the nested busy arrays to identify overlapping intervals using an interval merge algorithm. Authentication uses service account credentials via the googleapis Node.js client library with the calendar.readonly scope. The skill supports personal calendars, room resources, and shared team calendars. Conflict reports include the conflicting time slot, affected calendar IDs, and suggested open slots within the same day. It integrates with Google Meet by calling the calendar.events.list endpoint to fetch video conference links for affected meetings. Output formats include JSON, Markdown summary, and iCalendar VEVENT objects. Useful for scheduling assistants, automated meeting planners, and executive assistant agents.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/google-calendar-conflict-detector
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/google-calendar-conflict-detector` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-conflict-detector/)
