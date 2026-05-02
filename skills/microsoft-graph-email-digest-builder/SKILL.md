---
title: "Microsoft Graph Email Digest Builder"
description: "Generates daily email digests from Microsoft 365 mailboxes using the Microsoft Graph API /me/messages endpoint. Groups emails by sender, thread, and priority using the inferenceClassification properties."
verification: "security_reviewed"
source: "https://learn.microsoft.com/graph/overview"
category:
  - "Calendar, Email & Productivity"
framework:
  - "ChatGPT Agents"
---

# Microsoft Graph Email Digest Builder

The Microsoft Graph Email Digest Builder creates structured summaries of unread emails from Microsoft 365 accounts. It queries the Microsoft Graph API /me/messages endpoint with OData filters for receivedDateTime ranges and isRead status. Emails are grouped into categories using the inferenceClassification property (focused vs other) and further organized by conversationId for thread-based grouping. The skill extracts key information including subject lines, sender names, preview text from body.content, and attachment metadata via the /attachments sub-resource. Priority scoring uses a weighted algorithm combining sender importance (based on recent reply frequency queried via /me/mailFolders/sentItems/messages), email flags (importance and flag.flagStatus properties), and keyword matching against user-defined priority terms. The final digest is formatted as a structured document with sections for urgent items, thread summaries, and low-priority notifications. Supports delta queries via /me/messages/delta for incremental updates since the last digest generation. Integrates with Microsoft Teams via the /me/chats endpoint to include Teams message notifications in the unified digest.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/microsoft-graph-email-digest-builder/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/microsoft-graph-email-digest-builder
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/microsoft-graph-email-digest-builder`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-email-digest-builder/)
