---
name: "gcalcli Google Calendar Command Line Interface"
description: "gcalcli is a Python CLI that provides full access to Google Calendar from the command line. View agendas, search events, quick-add appointments, import ICS files, set reminders, and display ASCII calendar views—all without leaving the terminal."
verification: security_reviewed
source: "https://github.com/insanum/gcalcli"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "insanum/gcalcli"
  github_stars: 3678
---

# gcalcli Google Calendar Command Line Interface

gcalcli is a Python application that provides comprehensive command-line access to Google Calendar. Created in 2012 and actively maintained, it uses the Google Calendar API v3 to let users manage their calendars entirely from the terminal, making it a natural fit for scripting, cron jobs, and AI agent workflows.
How It Works
gcalcli authenticates via OAuth2 with your Google account and provides subcommands for every common calendar operation. You can view your agenda for any date range, search for events, quick-add events using natural language, create detailed events interactively, edit or delete events, and import ICS/vCal files. The tool can also serve as a reminder system, executing arbitrary commands when events are approaching.
Key Features

OAuth2 authentication with Google Calendar API v3
View agenda, weekly calendar (calw), and monthly calendar (calm) in ASCII art
Quick-add events using Google's natural language parsing
Search events across calendars with date range filters
Import ICS/vCal files from email attachments or other sources
Reminder system: execute any command when an event is approaching
Filter by specific calendar names using regex patterns
Colored output with Unicode character support
Shell completion for bash, zsh, and fish
Available via pip, apt (Debian/Ubuntu), brew (macOS), and nix

Integration Points
gcalcli's command-line interface is designed for scripting. Each subcommand outputs structured text that can be parsed by other tools. The remind subcommand integrates with any notification system by executing arbitrary shell commands with event details substituted in. Configuration can be stored in a config.toml file for persistent defaults.
Agent Use Cases
AI agents can use gcalcli as a bridge to Google Calendar. An agent can check a user's agenda before scheduling, quick-add events using natural language, find free time slots by searching for gaps, set up reminders that trigger agent actions, and import calendar invites received via email. The CLI output is easily parseable, making it straightforward for agents to extract structured schedule data. Combined with cron, agents can run periodic calendar checks and proactively notify users about upcoming commitments.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gcalcli-google-calendar-cli/)
