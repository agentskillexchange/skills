---
title: "gcalcli Google Calendar Command Line Interface"
description: "gcalcli is a Python application that provides comprehensive command-line access to Google Calendar. Created in 2012 and actively maintained, it uses the Google Calendar API v3 to let users manage their calendars entirely from the terminal, making it a natural fit for scripting, cron jobs, and AI agent workflows. How It Works gcalcli authenticates via OAuth2 with your Google account and provides subcommands for every common calendar operation. You can view your agenda for any date range, search for events, quick-add events using natural language, create detailed events interactively, edit or delete events, and import ICS/vCal files. The tool can also serve as a reminder system, executing arbitrary commands when events are approaching. Key Features OAuth2 authentication with Google Calendar API v3 View agenda, weekly calendar (calw), and monthly calendar (calm) in ASCII art Quick-add events using Google&#8217;s natural language parsing Search events across calendars with date range filters Import ICS/vCal files from email attachments or other sources Reminder system: execute any command when an event is approaching Filter by specific calendar names using regex patterns Colored output with Unicode character support Shell completion for bash, zsh, and fish Available via pip, apt (Debian/Ubuntu), brew (macOS), and nix Integration Points gcalcli&#8217;s command-line interface is designed for scripting. Each subcommand outputs structured text that can be parsed by other tools. The remind subcommand integrates with any notification system by executing arbitrary shell commands with event details substituted in. Configuration can be stored in a config.toml file for persistent defaults. Agent Use Cases AI agents can use gcalcli as a bridge to Google Calendar. An agent can check a user&#8217;s agenda before scheduling, quick-add events using natural language, find free time slots by searching for gaps, set up reminders that trigger agent actions, and import calendar invites received via email. The CLI output is easily parseable, making it straightforward for agents to extract structured schedule data. Combined with cron, agents can run periodic calendar checks and proactively notify users about upcoming commitments."
source: "https://github.com/insanum/gcalcli"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "insanum/gcalcli"
  github_stars: 3678
---

# gcalcli Google Calendar Command Line Interface

gcalcli is a Python application that provides comprehensive command-line access to Google Calendar. Created in 2012 and actively maintained, it uses the Google Calendar API v3 to let users manage their calendars entirely from the terminal, making it a natural fit for scripting, cron jobs, and AI agent workflows. How It Works gcalcli authenticates via OAuth2 with your Google account and provides subcommands for every common calendar operation. You can view your agenda for any date range, search for events, quick-add events using natural language, create detailed events interactively, edit or delete events, and import ICS/vCal files. The tool can also serve as a reminder system, executing arbitrary commands when events are approaching. Key Features OAuth2 authentication with Google Calendar API v3 View agenda, weekly calendar (calw), and monthly calendar (calm) in ASCII art Quick-add events using Google&#8217;s natural language parsing Search events across calendars with date range filters Import ICS/vCal files from email attachments or other sources Reminder system: execute any command when an event is approaching Filter by specific calendar names using regex patterns Colored output with Unicode character support Shell completion for bash, zsh, and fish Available via pip, apt (Debian/Ubuntu), brew (macOS), and nix Integration Points gcalcli&#8217;s command-line interface is designed for scripting. Each subcommand outputs structured text that can be parsed by other tools. The remind subcommand integrates with any notification system by executing arbitrary shell commands with event details substituted in. Configuration can be stored in a config.toml file for persistent defaults. Agent Use Cases AI agents can use gcalcli as a bridge to Google Calendar. An agent can check a user&#8217;s agenda before scheduling, quick-add events using natural language, find free time slots by searching for gaps, set up reminders that trigger agent actions, and import calendar invites received via email. The CLI output is easily parseable, making it straightforward for agents to extract structured schedule data. Combined with cron, agents can run periodic calendar checks and proactively notify users about upcoming commitments.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gcalcli-google-calendar-cli/)
