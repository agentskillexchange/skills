---
name: Outlook Rule Automation Manager
description: Creates and manages Outlook email rules programmatically using the Microsoft
  Graph API /me/mailFolders/inbox/messageRules endpoint. Supports complex condition
  chains with action sequences for automated email triage.
verification: security_reviewed
source: https://agentskillexchange.com/skills/outlook-rule-automation-manager/
category:
- Calendar, Email &amp; Productivity
framework:
- Custom Agents
---
# Outlook Rule Automation Manager

The Outlook Rule Automation Manager provides programmatic control over Microsoft Outlook email rules through the Microsoft Graph API. It uses the /me/mailFolders/inbox/messageRules endpoint to create, update, list, and delete inbox rules with full support for the messageRule resource type. Rules are defined with conditions including senderContains, subjectContains, bodyContains, headerContains, fromAddresses, sentToAddresses, hasAttachments, importance, and isAutomaticForward predicates. Each rule maps to one or more actions: moveToFolder (using folder IDs from /me/mailFolders), copyToFolder, forwardTo, forwardAsAttachmentTo, redirectTo, markAsRead, markImportance, and delete. The skill supports exception conditions that override rule matching for specific senders or subjects. Rule priority is managed via the sequence property, with the skill providing a reorder function that batch-updates priorities via PATCH requests. Complex workflows chain multiple rules with folder-specific triggers: rules can monitor subfolders by creating rules via /me/mailFolders/{folderId}/messageRules. The manager includes a test mode that evaluates existing messages against proposed rules via /me/messages with matching OData filters before rule activation. Supports shared mailbox rules via the /users/{userId}/mailFolders endpoint with appropriate delegated permissions.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/outlook-rule-automation-manager/)
