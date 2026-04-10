---
title: "Microsoft Graph Email Digest Builder"
description: "Generates daily email digests from Microsoft 365 mailboxes using the Microsoft Graph API /me/messages endpoint. Groups emails by sender, thread, and priority using the inferenceClassification properties."
slug: "microsoft-graph-email-digest-builder"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/microsoft-graph-email-digest-builder/"
listed: true
---

# Microsoft Graph Email Digest Builder

Generates daily email digests from Microsoft 365 mailboxes using the Microsoft Graph API /me/messages endpoint. Groups emails by sender, thread, and priority using the inferenceClassification properties.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install microsoft-graph-email-digest-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Microsoft Graph Email Digest Builder creates structured summaries of unread emails from Microsoft 365 accounts. It queries the Microsoft Graph API /me/messages endpoint with OData filters for receivedDateTime ranges and isRead status. Emails are grouped into categories using the inferenceClassification property (focused vs other) and further organized by conversationId for thread-based grouping. The skill extracts key information including subject lines, sender names, preview text from body.content, and attachment metadata via the /attachments sub-resource. Priority scoring uses a weighted algorithm combining sender importance (based on recent reply frequency queried via /me/mailFolders/sentItems/messages), email flags (importance and flag.flagStatus properties), and keyword matching against user-defined priority terms. The final digest is formatted as a structured document with sections for urgent items, thread summaries, and low-priority notifications. Supports delta queries via /me/messages/delta for incremental updates since the last digest generation. Integrates with Microsoft Teams via the /me/chats endpoint to include Teams message notifications in the unified digest.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-email-digest-builder/)
