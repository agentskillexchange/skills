---
name: "Google Calendar Smart Scheduler"
description: "Optimizes meeting scheduling using the Google Calendar API v3 and FreeBusy queries. Applies time-zone-aware slot finding, focus time protection, and travel buffer calculations via Google Maps Distance Matrix API."
category: "Calendar, Email & Productivity"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/google-calendar-smart-scheduler-2/"
---
# Google Calendar Smart Scheduler

Optimizes meeting scheduling using the Google Calendar API v3 and FreeBusy queries. Applies time-zone-aware slot finding, focus time protection, and travel buffer calculations via Google Maps Distance Matrix API.

## Overview

The Google Calendar Smart Scheduler automates meeting coordination by leveraging the Google Calendar API v3 for availability analysis and intelligent slot selection. It queries FreeBusy endpoints across multiple calendars and attendees to identify optimal meeting windows that respect everyone’s constraints and preferences.

The scheduler implements sophisticated heuristics: focus time block protection (configurable quiet hours that remain unscheduled), meeting clustering to batch meetings together and preserve contiguous deep work periods, time zone normalization for distributed teams with visual overlap displays, and travel buffer insertion using Google Maps Distance Matrix API to calculate transit time between in-person meetings at different locations.

Additional features include: recurring meeting optimization that finds stable weekly slots across changing schedules, conference room auto-booking via Google Workspace Resource Calendar API, meeting cost estimation based on attendee hourly rates, and smart rescheduling suggestions when conflicts arise. The agent can create calendar events with Google Meet links via the Hangouts API, attach agenda documents from Google Drive, and send customized invitation emails through Gmail API with calendar file attachments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill google-calendar-smart-scheduler-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill google-calendar-smart-scheduler-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill google-calendar-smart-scheduler-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill google-calendar-smart-scheduler-2 -a codex
```

### OpenClaw

```bash
clawhub install google-calendar-smart-scheduler-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-smart-scheduler-2/)
