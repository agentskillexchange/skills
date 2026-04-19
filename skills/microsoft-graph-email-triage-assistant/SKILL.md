---
title: "Microsoft Graph Email Triage Assistant"
description: "The Microsoft Graph Email Triage Assistant connects to Microsoft 365 mailboxes using the Microsoft Graph REST API with OAuth 2.0 MSAL authentication. It uses delta queries on the /messages endpoint for efficient incremental synchronization, processing only new and modified messages since the last sync token. The skill applies multi-label classification to each message based on configurable rules: sender domain reputation, subject line keyword matching, attachment analysis, and thread urgency indicators like read receipts and high-importance flags. Messages are automatically organized into Outlook folders using the /mailFolders endpoint—creating project-specific folders, moving newsletters to digest folders, and flagging messages requiring immediate attention. For priority messages, it generates concise response drafts using extracted context from the email thread, previous reply patterns, and linked calendar events. The skill supports Microsoft Graph batch requests ($batch endpoint) for processing up to 20 operations per request, dramatically improving throughput for high-volume inboxes. It maintains a local SQLite index for full-text search across triaged messages and integrates with Microsoft To Do API to create follow-up tasks from flagged emails."
source: "https://agentskillexchange.com/skills/microsoft-graph-email-triage-assistant/"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "OpenClaw"
---

# Microsoft Graph Email Triage Assistant

The Microsoft Graph Email Triage Assistant connects to Microsoft 365 mailboxes using the Microsoft Graph REST API with OAuth 2.0 MSAL authentication. It uses delta queries on the /messages endpoint for efficient incremental synchronization, processing only new and modified messages since the last sync token. The skill applies multi-label classification to each message based on configurable rules: sender domain reputation, subject line keyword matching, attachment analysis, and thread urgency indicators like read receipts and high-importance flags. Messages are automatically organized into Outlook folders using the /mailFolders endpoint—creating project-specific folders, moving newsletters to digest folders, and flagging messages requiring immediate attention. For priority messages, it generates concise response drafts using extracted context from the email thread, previous reply patterns, and linked calendar events. The skill supports Microsoft Graph batch requests ($batch endpoint) for processing up to 20 operations per request, dramatically improving throughput for high-volume inboxes. It maintains a local SQLite index for full-text search across triaged messages and integrates with Microsoft To Do API to create follow-up tasks from flagged emails.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-email-triage-assistant/)
