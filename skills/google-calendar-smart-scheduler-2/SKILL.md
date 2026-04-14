---
title: "Google Calendar Smart Scheduler"
description: "Optimizes meeting scheduling using the Google Calendar API v3 and FreeBusy queries. Applies time-zone-aware slot finding, focus time protection, and travel buffer calculations via Google Maps Distance Matrix API."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/google-calendar-smart-scheduler-2/"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "OpenClaw"
---

# Google Calendar Smart Scheduler

The Google Calendar Smart Scheduler automates meeting coordination by leveraging the Google Calendar API v3 for availability analysis and intelligent slot selection. It queries FreeBusy endpoints across multiple calendars and attendees to identify optimal meeting windows that respect everyone’s constraints and preferences.

The scheduler implements sophisticated heuristics: focus time block protection (configurable quiet hours that remain unscheduled), meeting clustering to batch meetings together and preserve contiguous deep work periods, time zone normalization for distributed teams with visual overlap displays, and travel buffer insertion using Google Maps Distance Matrix API to calculate transit time between in-person meetings at different locations.

Additional features include: recurring meeting optimization that finds stable weekly slots across changing schedules, conference room auto-booking via Google Workspace Resource Calendar API, meeting cost estimation based on attendee hourly rates, and smart rescheduling suggestions when conflicts arise. The agent can create calendar events with Google Meet links via the Hangouts API, attach agenda documents from Google Drive, and send customized invitation emails through Gmail API with calendar file attachments.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-smart-scheduler-2/)
