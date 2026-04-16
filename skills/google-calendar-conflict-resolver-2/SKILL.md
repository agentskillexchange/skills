---
title: "Google Calendar Conflict Resolver"
description: "Detects and resolves scheduling conflicts across multiple Google Calendar accounts using the Google Calendar API v3 freebusy query. Suggests optimal rescheduling slots based on attendee availability windows."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/google-calendar-conflict-resolver-2/"
category:
  - "Calendar, Email & Productivity"
framework:
  - "OpenClaw"
---

# Google Calendar Conflict Resolver

The Google Calendar Conflict Resolver scans multiple calendar accounts for overlapping events and proposes resolution strategies. Using the Google Calendar API v3 freebusy.query endpoint, it fetches busy intervals across specified calendars and time ranges. The skill identifies three conflict types: hard conflicts (same attendees, overlapping times), soft conflicts (back-to-back meetings with no buffer), and travel conflicts (in-person meetings with insufficient transit time between locations). For each conflict, it queries available slots using the same freebusy API and proposes up to three rescheduling options ranked by attendee preference scores. The preference model considers historical meeting patterns via events.list, working hours from calendar settings, and timezone-aware scheduling constraints. It integrates with Google Maps Distance Matrix API to calculate realistic travel times between physical meeting locations. Automated resolution can be enabled for low-priority events, sending calendar update requests via events.patch with configurable approval workflows. Supports recurring event conflict detection and series-level rescheduling.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-conflict-resolver-2/)
