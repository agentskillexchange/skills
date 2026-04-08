---
title: Microsoft Graph Email Digest Builder
description: The Microsoft Graph Email Digest Builder creates structured summaries
  of unread emails from Microsoft 365 accounts. It queries the Microsoft Graph API
  /me/messages endpoint with OData filters for receivedDateTime ranges and isRead
  status. Emails are grouped into categories using the inferenceClassification property
  (focused vs other) and further organized by conversationId for thread-based grouping.
  The skill extracts key information including subject lines, sender names, preview
  text from body.content, and attachment metadata via the /attachments sub-resource.
  Priority scoring uses a weighted algorithm combining sender importance (based on
  recent reply frequency queried via /me/mailFolders/sentItems/messages), email flags
  (importance and flag.flagStatus properties), and keyword matching against user-defined
  priority terms. The final digest is formatted as a structured document with sections
  for urgent items, thread summaries, and low-priority notifications. Supports delta
  queries via /me/messages/delta for incremental updates since the last digest generation.
  Integrates with Microsoft Teams via the /me/chats endpoint to include Teams message
  notifications in the unified digest.
verification: security_reviewed
source: https://agentskillexchange.com/skills/microsoft-graph-email-digest-builder/
category:
- Calendar, Email &amp; Productivity
framework:
- ChatGPT Agents
---

# Microsoft Graph Email Digest Builder

The Microsoft Graph Email Digest Builder creates structured summaries of unread emails from Microsoft 365 accounts. It queries the Microsoft Graph API /me/messages endpoint with OData filters for receivedDateTime ranges and isRead status. Emails are grouped into categories using the inferenceClassification property (focused vs other) and further organized by conversationId for thread-based grouping. The skill extracts key information including subject lines, sender names, preview text from body.content, and attachment metadata via the /attachments sub-resource. Priority scoring uses a weighted algorithm combining sender importance (based on recent reply frequency queried via /me/mailFolders/sentItems/messages), email flags (importance and flag.flagStatus properties), and keyword matching against user-defined priority terms. The final digest is formatted as a structured document with sections for urgent items, thread summaries, and low-priority notifications. Supports delta queries via /me/messages/delta for incremental updates since the last digest generation. Integrates with Microsoft Teams via the /me/chats endpoint to include Teams message notifications in the unified digest.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-email-digest-builder/)
