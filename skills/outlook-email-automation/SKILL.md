---
title: "Outlook Email Automation"
description: "Authenticates to Microsoft Graph API using MSAL with Mail.ReadWrite and Calendars.ReadWrite permissions. Reads, classifies, and responds to emails via GET /me/messages and POST /me/sendMail. Moves processed messages into folders and tracks reply SLAs in a local SQLite store."
verification: security_reviewed
source: "https://learn.microsoft.com/en-us/graph/outlook-mail-concept-overview"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Claude Code"
---

# Outlook Email Automation

Authenticates to Microsoft Graph API using MSAL with Mail.ReadWrite and Calendars.ReadWrite permissions. Reads, classifies, and responds to emails via GET /me/messages and POST /me/sendMail. Moves processed messages into folders and tracks reply SLAs in a local SQLite store.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/outlook-email-automation/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/outlook-email-automation
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/outlook-email-automation`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/outlook-email-automation/)
