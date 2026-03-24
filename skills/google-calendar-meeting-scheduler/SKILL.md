---
name: "Google Calendar Meeting Scheduler"
description: "Queries Google Calendar API to find free/busy windows across multiple attendees using FreeBusy queries. Creates events with Meet links via events.insert with conferenceData and sends invites via the attendees field. Handles timezone normalization using pytz."
category: "Calendar, Email & Productivity"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/google-calendar-meeting-scheduler/"
---

# Google Calendar Meeting Scheduler

Queries Google Calendar API to find free/busy windows across multiple attendees using FreeBusy queries. Creates events with Meet links via events.insert with conferenceData and sends invites via the attendees field. Handles timezone normalization using pytz.

## Overview

Queries Google Calendar API to find free/busy windows across multiple attendees using FreeBusy queries. Creates events with Meet links via events.insert with conferenceData and sends invites via the attendees field. Handles timezone normalization using pytz.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill google-calendar-meeting-scheduler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill google-calendar-meeting-scheduler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill google-calendar-meeting-scheduler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill google-calendar-meeting-scheduler -a codex
```

### OpenClaw

```bash
clawhub install google-calendar-meeting-scheduler
```

## Source

- Marketplace: https://agentskillexchange.com/skills/google-calendar-meeting-scheduler/
