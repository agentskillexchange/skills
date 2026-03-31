---
name: "Microsoft Graph Email Digest Builder"
description: "Generates daily email digests from Microsoft 365 mailboxes using the Microsoft Graph API /me/messages endpoint. Groups emails by sender, thread, and priority using the inferenceClassification properties."
category: "Calendar, Email &amp; Productivity"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/microsoft-graph-email-digest-builder/"
---
# Microsoft Graph Email Digest Builder

Generates daily email digests from Microsoft 365 mailboxes using the Microsoft Graph API /me/messages endpoint. Groups emails by sender, thread, and priority using the inferenceClassification properties.

## Overview

The Microsoft Graph Email Digest Builder creates structured summaries of unread emails from Microsoft 365 accounts. It queries the Microsoft Graph API /me/messages endpoint with OData filters for receivedDateTime ranges and isRead status. Emails are grouped into categories using the inferenceClassification property (focused vs other) and further organized by conversationId for thread-based grouping. The skill extracts key information including subject lines, sender names, preview text from body.content, and attachment metadata via the /attachments sub-resource. Priority scoring uses a weighted algorithm combining sender importance (based on recent reply frequency queried via /me/mailFolders/sentItems/messages), email flags (importance and flag.flagStatus properties), and keyword matching against user-defined priority terms. The final digest is formatted as a structured document with sections for urgent items, thread summaries, and low-priority notifications. Supports delta queries via /me/messages/delta for incremental updates since the last digest generation. Integrates with Microsoft Teams via the /me/chats endpoint to include Teams message notifications in the unified digest.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-email-digest-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-email-digest-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-email-digest-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-email-digest-builder -a codex
```

### OpenClaw

```bash
clawhub install microsoft-graph-email-digest-builder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-email-digest-builder/)
