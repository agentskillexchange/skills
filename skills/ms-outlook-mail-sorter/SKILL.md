---
name: "Microsoft Outlook Mail Sorter"
description: "Automatically triages Microsoft Outlook emails using the Microsoft Graph API /me/messages endpoint. Applies intelligent categorization with customizable rules and moves messages to appropriate folders."
category: "Calendar, Email & Productivity"
framework: "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ms-outlook-mail-sorter/"
---

# Microsoft Outlook Mail Sorter

Automatically triages Microsoft Outlook emails using the Microsoft Graph API /me/messages endpoint. Applies intelligent categorization with customizable rules and moves messages to appropriate folders.

## Overview

The Microsoft Outlook Mail Sorter skill connects to Microsoft 365 mailboxes via the Microsoft Graph API v1.0 /me/messages endpoint with $filter and $orderby OData query parameters. It processes incoming emails by analyzing sender reputation, subject line patterns, and body content to assign categories using the /me/messages/{id} PATCH endpoint. The skill creates and manages mail folders via /me/mailFolders POST operations and moves messages using the /me/messages/{id}/move action. Custom rules are defined in a YAML configuration supporting regex patterns, sender domain matching, and keyword extraction. The skill handles pagination with @odata.nextLink for large mailboxes and supports batch requests via the $batch endpoint for processing up to 20 operations simultaneously. Delta queries using /me/mailFolders/{id}/messages/delta enable efficient incremental sync without re-scanning the entire mailbox. Priority scoring weights recent sender interaction history from the People API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ms-outlook-mail-sorter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ms-outlook-mail-sorter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ms-outlook-mail-sorter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ms-outlook-mail-sorter -a codex
```

### OpenClaw

```bash
clawhub install ms-outlook-mail-sorter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ms-outlook-mail-sorter/
