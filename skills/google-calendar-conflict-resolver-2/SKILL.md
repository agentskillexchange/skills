---
title: Google Calendar Conflict Resolver
description: 'The Google Calendar Conflict Resolver scans multiple calendar accounts
  for overlapping events and proposes resolution strategies. Using the Google Calendar
  API v3 freebusy.query endpoint, it fetches busy intervals across specified calendars
  and time ranges. The skill identifies three conflict types: hard conflicts (same
  attendees, overlapping times), soft conflicts (back-to-back meetings with no buffer),
  and travel conflicts (in-person meetings with insufficient transit time between
  locations). For each conflict, it queries available slots using the same freebusy
  API and proposes up to three rescheduling options ranked by attendee preference
  scores. The preference model considers historical meeting patterns via events.list,
  working hours from calendar settings, and timezone-aware scheduling constraints.
  It integrates with Google Maps Distance Matrix API to calculate realistic travel
  times between physical meeting locations. Automated resolution can be enabled for
  low-priority events, sending calendar update requests via events.patch with configurable
  approval workflows. Supports recurring event conflict detection and series-level
  rescheduling.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/google-calendar-conflict-resolver-2/
category:
- Calendar, Email &amp; Productivity
framework:
- OpenClaw
---

# Google Calendar Conflict Resolver

The Google Calendar Conflict Resolver scans multiple calendar accounts for overlapping events and proposes resolution strategies. Using the Google Calendar API v3 freebusy.query endpoint, it fetches busy intervals across specified calendars and time ranges. The skill identifies three conflict types: hard conflicts (same attendees, overlapping times), soft conflicts (back-to-back meetings with no buffer), and travel conflicts (in-person meetings with insufficient transit time between locations). For each conflict, it queries available slots using the same freebusy API and proposes up to three rescheduling options ranked by attendee preference scores. The preference model considers historical meeting patterns via events.list, working hours from calendar settings, and timezone-aware scheduling constraints. It integrates with Google Maps Distance Matrix API to calculate realistic travel times between physical meeting locations. Automated resolution can be enabled for low-priority events, sending calendar update requests via events.patch with configurable approval workflows. Supports recurring event conflict detection and series-level rescheduling.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-conflict-resolver-2/)
