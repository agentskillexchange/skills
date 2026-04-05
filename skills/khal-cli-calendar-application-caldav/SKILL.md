---
name: "khal Standards-Based CLI Calendar Application"
description: "khal is a standards-based CLI and terminal calendar program written in Python. It reads and writes iCalendar data to vdir format, synchronizes with CalDAV servers via vdirsyncer, and provides both a command-line interface for scripting and an interactive terminal UI (ikhal) for browsing and editing events."
category: "Calendar, Email &amp; Productivity"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/pimutils/khal"
tool_ecosystem:
  github_repo: "pimutils/khal"
  github_stars: 2971
---
# khal Standards-Based CLI Calendar Application

khal is a standards-based CLI and terminal calendar program written in Python. It reads and writes iCalendar data to vdir format, synchronizes with CalDAV servers via vdirsyncer, and provides both a command-line interface for scripting and an interactive terminal UI (ikhal) for browsing and editing events.

khal is a CLI calendar application that adheres to iCalendar standards for event storage and exchange. Written in Python, it provides both a non-interactive command-line interface for quick operations and an interactive terminal UI called ikhal for browsing calendars and editing events visually.

Calendar Data Storage khal reads and writes events in the vdir format, a simple directory-based storage for iCalendar files. Each calendar is a directory containing .ics files, one per event. This plain-file approach means calendar data is easily backed up, version controlled, and inspected without specialized tools. The vdir format is shared with vdirsyncer, enabling seamless synchronization.

CalDAV Synchronization Through vdirsyncer, khal synchronizes with CalDAV servers including Google Calendar, Nextcloud, Radicale, Baikal, and any other CalDAV-compatible server. vdirsyncer handles the network protocol and conflict resolution, while khal operates on the local vdir copy. This separation of concerns means khal works fully offline and syncs when connectivity is available.

Interactive Terminal UI The ikhal interactive mode provides a terminal-based calendar view with keyboard navigation. Users can browse dates, view event details, create new events, edit existing ones, and switch between calendars. The interface shows a monthly calendar grid alongside a daily event list, providing at-a-glance schedule visibility without leaving the terminal.

Command-Line Interface The non-interactive CLI supports operations like listing events for a date range, creating new events with natural-language-like syntax, importing .ics files, and searching events. Commands output plain text by default, making them suitable for scripting and piping. The khal new command accepts date, time, and event title as arguments for fast event creation.

Configuration and Compatibility khal is configured via a simple INI-style configuration file specifying calendar directories, date and time formats, default calendar, and display preferences. It requires Python 3.10+ and runs on Linux, macOS, and BSD operating systems. It is packaged for major distributions including Debian/Ubuntu (apt), Arch Linux (pacman), Homebrew, Fedora (dnf), FreeBSD (pkg), and Nix. The project has nearly 3,000 GitHub stars and is licensed under MIT.

Agent Skill Application An agent can use khal CLI commands to query upcoming events, check schedule conflicts, create new calendar entries, and provide scheduling context. Combined with vdirsyncer for CalDAV sync, it gives agents read-write access to calendar data stored on standard calendar servers, making it a practical foundation for calendar-aware agent skills.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill khal-cli-calendar-application-caldav
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill khal-cli-calendar-application-caldav -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill khal-cli-calendar-application-caldav -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill khal-cli-calendar-application-caldav -a codex
```

### OpenClaw

```bash
clawhub install khal-cli-calendar-application-caldav
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/khal-cli-calendar-application-caldav/)
