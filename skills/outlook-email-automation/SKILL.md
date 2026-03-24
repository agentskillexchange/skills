---
name: "Outlook Email Automation"
description: "Authenticates to Microsoft Graph API using MSAL with Mail.ReadWrite and Calendars.ReadWrite permissions. Reads, classifies, and responds to emails via GET /me/messages and POST /me/sendMail. Moves processed messages into folders and tracks reply SLAs in a local SQLite store."
category: "Calendar, Email & Productivity"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/outlook-email-automation/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sqlite"  # from ase_tool_match
  npm_weekly_downloads: 4960915  # from ase_npm_downloads
---

# Outlook Email Automation

Authenticates to Microsoft Graph API using MSAL with Mail.ReadWrite and Calendars.ReadWrite permissions. Reads, classifies, and responds to emails via GET /me/messages and POST /me/sendMail. Moves processed messages into folders and tracks reply SLAs in a local SQLite store.

## Overview

Authenticates to Microsoft Graph API using MSAL with Mail.ReadWrite and Calendars.ReadWrite permissions. Reads, classifies, and responds to emails via GET /me/messages and POST /me/sendMail. Moves processed messages into folders and tracks reply SLAs in a local SQLite store.

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

- Marketplace: https://agentskillexchange.com/skills/outlook-email-automation/
