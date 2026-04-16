---
title: "Microsoft Outlook Mail Sorter"
description: "Automatically triages Microsoft Outlook emails using the Microsoft Graph API /me/messages endpoint. Applies intelligent categorization with customizable rules and moves messages to appropriate folders."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ms-outlook-mail-sorter/"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Claude Code"
---

# Microsoft Outlook Mail Sorter

The Microsoft Outlook Mail Sorter skill connects to Microsoft 365 mailboxes via the Microsoft Graph API v1.0 /me/messages endpoint with $filter and $orderby OData query parameters. It processes incoming emails by analyzing sender reputation, subject line patterns, and body content to assign categories using the /me/messages/{id} PATCH endpoint. The skill creates and manages mail folders via /me/mailFolders POST operations and moves messages using the /me/messages/{id}/move action. Custom rules are defined in a YAML configuration supporting regex patterns, sender domain matching, and keyword extraction. The skill handles pagination with @odata.nextLink for large mailboxes and supports batch requests via the $batch endpoint for processing up to 20 operations simultaneously. Delta queries using /me/mailFolders/{id}/messages/delta enable efficient incremental sync without re-scanning the entire mailbox. Priority scoring weights recent sender interaction history from the People API.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ms-outlook-mail-sorter/)
