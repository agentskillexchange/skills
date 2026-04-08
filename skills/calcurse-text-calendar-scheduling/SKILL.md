---
title: calcurse Text-Based Calendar and Scheduling Application
description: calcurse is a calendar and scheduling application that runs entirely
  in the terminal. Created in 2004 by Frederic Culot and maintained since 2011 by
  Lukas Fleischer, it provides a full-featured personal information manager through
  an ncurses-based text user interface. How It Works calcurse presents a split-pane
  terminal interface showing your calendar, appointments, and to-do list simultaneously.
  Events and appointments are stored in plain-text iCalendar format files, making
  them easy to back up, version control, and sync. The built-in CalDAV synchronization
  script (calcurse-caldav) lets you sync with remote calendars like Google Calendar,
  Nextcloud, or Radicale. Key Features Interactive ncurses TUI with configurable layouts
  and color schemes Appointment management with support for recurring events and reminders
  To-do list with priority levels CalDAV synchronization via the included calcurse-caldav
  Python script Import and export in iCalendar (.ics) and pcal formats Powerful command-line
  filtering options for use in shell scripts and cron jobs Configurable notification
  system for upcoming deadlines Internationalization with gettext support Integration
  Points calcurse stores data in ~/.local/share/calcurse/ in plain text. Agents can
  directly read and write appointment files, query upcoming events using calcurse
  command-line options with format strings, or trigger CalDAV syncs. The command-line
  interface supports filtering by date ranges and outputting in machine-parseable
  formats, making it straightforward to integrate into automation workflows. Agent
  Use Cases Agents can leverage calcurse as a lightweight, local-first calendar backend.
  An agent can add appointments by piping iCalendar data, query the agenda for a date
  range to check availability, trigger CalDAV syncs to keep local and remote calendars
  aligned, and set up reminder commands that notify users through whatever channel
  they prefer. Because calcurse uses plain text files, agents can also perform bulk
  operations like importing conference schedules or cleaning up past events.
verification: security_reviewed
source: https://github.com/lfos/calcurse
category:
- Calendar, Email &amp; Productivity
framework:
- Custom Agents
tool_ecosystem:
  github_repo: lfos/calcurse
  github_stars: 1235
---

# calcurse Text-Based Calendar and Scheduling Application

calcurse is a calendar and scheduling application that runs entirely in the terminal. Created in 2004 by Frederic Culot and maintained since 2011 by Lukas Fleischer, it provides a full-featured personal information manager through an ncurses-based text user interface. How It Works calcurse presents a split-pane terminal interface showing your calendar, appointments, and to-do list simultaneously. Events and appointments are stored in plain-text iCalendar format files, making them easy to back up, version control, and sync. The built-in CalDAV synchronization script (calcurse-caldav) lets you sync with remote calendars like Google Calendar, Nextcloud, or Radicale. Key Features Interactive ncurses TUI with configurable layouts and color schemes Appointment management with support for recurring events and reminders To-do list with priority levels CalDAV synchronization via the included calcurse-caldav Python script Import and export in iCalendar (.ics) and pcal formats Powerful command-line filtering options for use in shell scripts and cron jobs Configurable notification system for upcoming deadlines Internationalization with gettext support Integration Points calcurse stores data in ~/.local/share/calcurse/ in plain text. Agents can directly read and write appointment files, query upcoming events using calcurse command-line options with format strings, or trigger CalDAV syncs. The command-line interface supports filtering by date ranges and outputting in machine-parseable formats, making it straightforward to integrate into automation workflows. Agent Use Cases Agents can leverage calcurse as a lightweight, local-first calendar backend. An agent can add appointments by piping iCalendar data, query the agenda for a date range to check availability, trigger CalDAV syncs to keep local and remote calendars aligned, and set up reminder commands that notify users through whatever channel they prefer. Because calcurse uses plain text files, agents can also perform bulk operations like importing conference schedules or cleaning up past events.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/calcurse-text-calendar-scheduling/)
