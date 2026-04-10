---
title: "calcurse Text-Based Calendar and Scheduling Application"
description: "calcurse is a text-based calendar and scheduling application for the command line. It helps keep track of events, appointments, and everyday tasks with a curses-based TUI, configurable notifications, and CalDAV synchronization support."
slug: "calcurse-text-calendar-scheduling"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/lfos/calcurse"
tool_ecosystem:
  github_repo: "lfos/calcurse"
  github_stars: 1235
---

# calcurse Text-Based Calendar and Scheduling Application

calcurse is a text-based calendar and scheduling application for the command line. It helps keep track of events, appointments, and everyday tasks with a curses-based TUI, configurable notifications, and CalDAV synchronization support.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install calcurse-text-calendar-scheduling
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

calcurse is a calendar and scheduling application that runs entirely in the terminal. Created in 2004 by Frederic Culot and maintained since 2011 by Lukas Fleischer, it provides a full-featured personal information manager through an ncurses-based text user interface.
How It Works
calcurse presents a split-pane terminal interface showing your calendar, appointments, and to-do list simultaneously. Events and appointments are stored in plain-text iCalendar format files, making them easy to back up, version control, and sync. The built-in CalDAV synchronization script (calcurse-caldav) lets you sync with remote calendars like Google Calendar, Nextcloud, or Radicale.
Key Features
- Interactive ncurses TUI with configurable layouts and color schemes
- Appointment management with support for recurring events and reminders
- To-do list with priority levels
- CalDAV synchronization via the included calcurse-caldav Python script
- Import and export in iCalendar (.ics) and pcal formats
- Powerful command-line filtering options for use in shell scripts and cron jobs
- Configurable notification system for upcoming deadlines
- Internationalization with gettext support
Integration Points
calcurse stores data in ~/.local/share/calcurse/ in plain text. Agents can directly read and write appointment files, query upcoming events using calcurse command-line options with format strings, or trigger CalDAV syncs. The command-line interface supports filtering by date ranges and outputting in machine-parseable formats, making it straightforward to integrate into automation workflows.
Agent Use Cases
Agents can leverage calcurse as a lightweight, local-first calendar backend. An agent can add appointments by piping iCalendar data, query the agenda for a date range to check availability, trigger CalDAV syncs to keep local and remote calendars aligned, and set up reminder commands that notify users through whatever channel they prefer. Because calcurse uses plain text files, agents can also perform bulk operations like importing conference schedules or cleaning up past events.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/calcurse-text-calendar-scheduling/)
