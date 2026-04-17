---
title: "Microsoft Graph Email Triage Assistant"
description: "The Microsoft Graph Email Triage Assistant connects to Microsoft 365 mailboxes using the Microsoft Graph REST API with OAuth 2.0 MSAL authentication. It uses delta queries on the /messages endpoint for efficient incremental synchronization, processing only new and modified messages since the last sync token. The skill applies multi-label classification to each message based on configurable rules: sender domain reputation, subject line keyword matching, attachment analysis, and thread urgency indicators like read receipts and high-importance flags. Messages are automatically organized into Outlook folders using the /mailFolders endpoint—creating project-specific folders, moving newsletters to digest folders, and flagging messages requiring immediate attention. For priority messages, it generates concise response drafts using extracted context from the email thread, previous reply patterns, and linked calendar events. The skill supports Microsoft Graph batch requests ($batch endpoint) for processing up to 20 operations per request, dramatically improving throughput for high-volume inboxes. It maintains a local SQLite index for full-text search across triaged messages and integrates with Microsoft To Do API to create follow-up tasks from flagged emails."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/microsoft-graph-email-triage-assistant/"
framework:
  - "OpenClaw"
---

# Microsoft Graph Email Triage Assistant

The Microsoft Graph Email Triage Assistant connects to Microsoft 365 mailboxes using the Microsoft Graph REST API with OAuth 2.0 MSAL authentication. It uses delta queries on the /messages endpoint for efficient incremental synchronization, processing only new and modified messages since the last sync token. The skill applies multi-label classification to each message based on configurable rules: sender domain reputation, subject line keyword matching, attachment analysis, and thread urgency indicators like read receipts and high-importance flags. Messages are automatically organized into Outlook folders using the /mailFolders endpoint—creating project-specific folders, moving newsletters to digest folders, and flagging messages requiring immediate attention. For priority messages, it generates concise response drafts using extracted context from the email thread, previous reply patterns, and linked calendar events. The skill supports Microsoft Graph batch requests ($batch endpoint) for processing up to 20 operations per request, dramatically improving throughput for high-volume inboxes. It maintains a local SQLite index for full-text search across triaged messages and integrates with Microsoft To Do API to create follow-up tasks from flagged emails.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/microsoft-graph-email-triage-assistant
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/microsoft-graph-email-triage-assistant` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-email-triage-assistant/)
