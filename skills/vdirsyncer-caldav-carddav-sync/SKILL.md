---
name: "vdirsyncer CalDAV and CardDAV Calendar and Contact Synchronizer"
description: "vdirsyncer is a command-line tool for synchronizing calendars and addressbooks between servers and the local filesystem via CalDAV and CardDAV protocols. It bridges remote calendar and contact servers with local tools like khal and khard."
category: "Calendar, Email &amp; Productivity"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/pimutils/vdirsyncer"
tool_ecosystem:
  github_repo: "https://github.com/pimutils/vdirsyncer"
  github_stars: 1804
---
# vdirsyncer CalDAV and CardDAV Calendar and Contact Synchronizer

vdirsyncer is a command-line tool for synchronizing calendars and addressbooks between servers and the local filesystem via CalDAV and CardDAV protocols. It bridges remote calendar and contact servers with local tools like khal and khard.

vdirsyncer is a Python command-line tool that synchronizes calendars and addressbooks between a variety of CalDAV/CardDAV servers and the local filesystem. Developed as part of the pimutils ecosystem, it serves as the synchronization backbone that connects remote servers (Google Calendar, Nextcloud, Radicale, iCloud, etc.) with local CLI tools like khal (calendar) and khard (contacts).

How It Works

vdirsyncer operates on a pair-based model: you define a source (typically a CalDAV or CardDAV server) and a destination (typically a local vdir directory), and vdirsyncer handles bidirectional synchronization between them. It can also synchronize between two remote servers directly. Calendar events are stored as individual .ics files and contacts as .vcf files in the local vdir format.

Key Features

- Bidirectional sync between CalDAV/CardDAV servers and local vdir directories

- Server-to-server synchronization without local intermediary

- Support for Google Calendar, Google Contacts, Nextcloud, Radicale, iCloud, Fastmail, and other standards-compliant servers

- OAuth2 authentication support for Google services

- Conflict resolution strategies: choose which side wins on conflicts

- Selective sync with filtering by calendar name or collection

- Available on PyPI and major Linux distributions

- Docker image available for containerized deployments

Integration Points

vdirsyncer is designed to be the glue between remote calendar systems and local tools. After syncing, the local vdir files can be read and modified by any tool that understands iCalendar and vCard formats. The CLI supports discover, sync, and metasync subcommands that can be automated via cron or systemd timers.

Agent Use Cases

An AI agent can use vdirsyncer to maintain a local copy of a user’s calendars and contacts. The agent runs vdirsyncer sync periodically to pull down the latest events, reads the .ics files to check availability or find contact information, makes changes locally (adding events, updating contacts), and then runs sync again to push changes back to the server. This gives agents a fast, local-first interface to calendar and contact data without needing to make API calls for every read operation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill vdirsyncer-caldav-carddav-sync
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill vdirsyncer-caldav-carddav-sync -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill vdirsyncer-caldav-carddav-sync -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill vdirsyncer-caldav-carddav-sync -a codex
```

### OpenClaw

```bash
clawhub install vdirsyncer-caldav-carddav-sync
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vdirsyncer-caldav-carddav-sync/)
