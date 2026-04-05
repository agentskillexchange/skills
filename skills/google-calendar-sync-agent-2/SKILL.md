---
name: "Google Calendar Sync Agent"
description: "Synchronizes events across multiple Google Calendar accounts using the Calendar API v3 and OAuth 2.0. Handles recurring events, timezone conversions, and conflict resolution."
category: "Calendar, Email &amp; Productivity"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/google-calendar-sync-agent-2/"
---
# Google Calendar Sync Agent

Synchronizes events across multiple Google Calendar accounts using the Calendar API v3 and OAuth 2.0. Handles recurring events, timezone conversions, and conflict resolution.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill google-calendar-sync-agent-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill google-calendar-sync-agent-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill google-calendar-sync-agent-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill google-calendar-sync-agent-2 -a codex
```

### OpenClaw

```bash
clawhub install google-calendar-sync-agent-2
```

## Details

Google Calendar Sync Agent manages bidirectional synchronization across multiple Google Calendar accounts through the Calendar API v3. It uses incremental sync tokens to minimize API quota consumption, processing only changed events since the last sync. The agent handles complex recurring event patterns including RRULE with EXDATE exceptions, properly converting between timezones using the IANA tz database. Conflict resolution supports configurable strategies: last-write-wins, source-priority, or interactive prompting. It manages OAuth 2.0 refresh token rotation across multiple accounts and supports Google Workspace domain-wide delegation for organizational calendars. The tool generates daily agenda summaries, detects double-bookings across synced calendars, and supports color-coding rules based on event source. Push notifications via Google Cloud Pub/Sub enable near-real-time sync.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/google-calendar-sync-agent-2/)
