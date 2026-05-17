---
title: "Google Calendar Conflict Detector"
slug: "google-calendar-conflict-detector"
description: "Detects scheduling conflicts across multiple Google Calendars using the Google Calendar API v3 and the freebusy query endpoint. Posts calendar IDs and a time range to /calendar/v3/freeBusy, parses overlapping busy slots, and returns structured conflict reports. Supports service account authentication via the googleapis Node.js client library."
verification: "security_reviewed"
source: "https://developers.google.com/workspace/calendar/api/guides/overview"
author: "Google"
category: "Calendar, Email & Productivity"
framework: "Gemini"
---

# Google Calendar Conflict Detector

Detects scheduling conflicts across multiple Google Calendars using the Google Calendar API v3 and the freebusy query endpoint. Posts calendar IDs and a time range to /calendar/v3/freeBusy, parses overlapping busy slots, and returns structured conflict reports. Supports service account authentication via the googleapis Node.js client library.

## Prerequisites

Google account, Google Cloud project, Google Calendar API enabled, and OAuth 2.0 credentials

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Create a Google Cloud project, enable the Google Calendar API, configure OAuth 2.0 credentials, then authorize your app against the Calendar API.
```

## Documentation

- https://developers.google.com/workspace/calendar/api/guides/overview

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-conflict-detector/)
