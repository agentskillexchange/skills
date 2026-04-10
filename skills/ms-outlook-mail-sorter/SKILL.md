---
title: "Microsoft Outlook Mail Sorter"
description: "Automatically triages Microsoft Outlook emails using the Microsoft Graph API /me/messages endpoint. Applies intelligent categorization with customizable rules and moves messages to appropriate folders."
slug: "ms-outlook-mail-sorter"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ms-outlook-mail-sorter/"
---

# Microsoft Outlook Mail Sorter

Automatically triages Microsoft Outlook emails using the Microsoft Graph API /me/messages endpoint. Applies intelligent categorization with customizable rules and moves messages to appropriate folders.

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
clawhub install ms-outlook-mail-sorter
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Microsoft Outlook Mail Sorter skill connects to Microsoft 365 mailboxes via the Microsoft Graph API v1.0 /me/messages endpoint with $filter and $orderby OData query parameters. It processes incoming emails by analyzing sender reputation, subject line patterns, and body content to assign categories using the /me/messages/{id} PATCH endpoint. The skill creates and manages mail folders via /me/mailFolders POST operations and moves messages using the /me/messages/{id}/move action. Custom rules are defined in a YAML configuration supporting regex patterns, sender domain matching, and keyword extraction. The skill handles pagination with @odata.nextLink for large mailboxes and supports batch requests via the $batch endpoint for processing up to 20 operations simultaneously. Delta queries using /me/mailFolders/{id}/messages/delta enable efficient incremental sync without re-scanning the entire mailbox. Priority scoring weights recent sender interaction history from the People API.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ms-outlook-mail-sorter/)
