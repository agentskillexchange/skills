---
name: "Outlook Email Automation"
description: "Authenticates to Microsoft Graph API using MSAL with Mail.ReadWrite and Calendars.ReadWrite permissions. Reads, classifies, and responds to emails via GET /me/messages and POST /me/sendMail. Moves processed messages into folders and tracks reply SLAs in a local SQLite store."
category: "Calendar, Email &amp; Productivity"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/outlook-email-automation/"
---
# Outlook Email Automation

Authenticates to Microsoft Graph API using MSAL with Mail.ReadWrite and Calendars.ReadWrite permissions. Reads, classifies, and responds to emails via GET /me/messages and POST /me/sendMail. Moves processed messages into folders and tracks reply SLAs in a local SQLite store.

Outlook Email Automation is built around SQLite embedded database. The underlying ecosystem is represented by WiseLibs/better-sqlite3 (7,041+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like local .db files, SQL queries, schema inspection, FTS, WAL, query plans and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to sqlite so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Authenticates to Microsoft Graph API using MSAL with Mail.ReadWrite and Calendars.ReadWrite permissions. Reads, classifies, and responds to emails via GET /me/messages and POST /me/sendMail. Moves processed messages into folders and tracks reply SLAs in a local SQLite store. The implementation typically relies on local .db files, SQL queries, schema inspection, FTS, WAL, query plans, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses local .db files, SQL queries, schema inspection, FTS, WAL, query plans instead of scraping a UI, which makes runs easier to audit and retry. Supports structured inputs and outputs so another tool, agent, or CI step can consume the result. Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format. Fits into broader integration points such as lightweight analytics, app data inspection, and local tooling.

Key integration points include lightweight analytics, app data inspection, and local tooling. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill outlook-email-automation
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill outlook-email-automation -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill outlook-email-automation -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill outlook-email-automation -a codex
```

### OpenClaw

```bash
clawhub install outlook-email-automation
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/outlook-email-automation/)
