---
name: Google Calendar Smart Scheduler
description: Optimizes meeting scheduling using the Google Calendar API v3 and FreeBusy
  queries. Applies time-zone-aware slot finding, focus time protection, and travel
  buffer calculations via Google Maps Distance Matrix API.
verification: security_reviewed
source: https://agentskillexchange.com/skills/google-calendar-smart-scheduler-2/
category:
- Calendar, Email &amp; Productivity
framework:
- OpenClaw
---
# Google Calendar Smart Scheduler

The Google Calendar Smart Scheduler automates meeting coordination by leveraging the Google Calendar API v3 for availability analysis and intelligent slot selection. It queries FreeBusy endpoints across multiple calendars and attendees to identify optimal meeting windows that respect everyone's constraints and preferences.
The scheduler implements sophisticated heuristics: focus time block protection (configurable quiet hours that remain unscheduled), meeting clustering to batch meetings together and preserve contiguous deep work periods, time zone normalization for distributed teams with visual overlap displays, and travel buffer insertion using Google Maps Distance Matrix API to calculate transit time between in-person meetings at different locations.
Additional features include: recurring meeting optimization that finds stable weekly slots across changing schedules, conference room auto-booking via Google Workspace Resource Calendar API, meeting cost estimation based on attendee hourly rates, and smart rescheduling suggestions when conflicts arise. The agent can create calendar events with Google Meet links via the Hangouts API, attach agenda documents from Google Drive, and send customized invitation emails through Gmail API with calendar file attachments.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-smart-scheduler-2/)
