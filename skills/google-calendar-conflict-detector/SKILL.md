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

Detects scheduling conflicts across multiple Google Calendars using the Google Calendar API v3 and the freebusy query endpoint. Posts calendar IDs and a time range to /calendar/v3/freeBusy, parses overlapping busy slots, and returns structured conflict reports. Supports service account authentication via the googleapis Node.js client library.

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
