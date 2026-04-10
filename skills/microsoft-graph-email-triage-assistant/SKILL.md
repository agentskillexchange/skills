---
name: "Microsoft Graph Email Triage Assistant"
description: "Triages Outlook inboxes via Microsoft Graph API with delta query for incremental sync. Applies classification rules, auto-folders messages, and drafts priority-ranked response summaries."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/microsoft-graph-email-triage-assistant/"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "OpenClaw"
---

# Microsoft Graph Email Triage Assistant

The Microsoft Graph Email Triage Assistant connects to Microsoft 365 mailboxes using the Microsoft Graph REST API with OAuth 2.0 MSAL authentication. It uses delta queries on the /messages endpoint for efficient incremental synchronization, processing only new and modified messages since the last sync token. The skill applies multi-label classification to each message based on configurable rules: sender domain reputation, subject line keyword matching, attachment analysis, and thread urgency indicators like read receipts and high-importance flags. Messages are automatically organized into Outlook folders using the /mailFolders endpoint—creating project-specific folders, moving newsletters to digest folders, and flagging messages requiring immediate attention. For priority messages, it generates concise response drafts using extracted context from the email thread, previous reply patterns, and linked calendar events. The skill supports Microsoft Graph batch requests ($batch endpoint) for processing up to 20 operations per request, dramatically improving throughput for high-volume inboxes. It maintains a local SQLite index for full-text search across triaged messages and integrates with Microsoft To Do API to create follow-up tasks from flagged emails.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-email-triage-assistant/)
