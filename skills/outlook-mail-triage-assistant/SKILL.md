---
title: Outlook Mail Triage Assistant
description: 'The Outlook Mail Triage Assistant automates email management through
  the Microsoft Graph API, authenticating via @azure/msal-node with delegated permissions.
  It processes incoming messages in real-time using Graph subscriptions and webhooks.
  The agent performs zero-shot classification on email content to categorize messages
  into actionable buckets: urgent, informational, promotional, and follow-up required.
  It leverages the Graph API’s message endpoints to apply labels, move messages between
  folders, and flag items for follow-up with due dates. Advanced triage rules support
  sender reputation scoring, thread importance analysis based on participant lists,
  and attachment scanning metadata. The agent integrates with Outlook’s focused inbox
  API to programmatically adjust message priorities and creates digest summaries of
  low-priority batches. It also manages calendar invites embedded in emails, auto-responding
  to scheduling requests based on configurable availability windows.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/outlook-mail-triage-assistant/
category:
- Calendar, Email &amp; Productivity
framework:
- Claude Code
---

# Outlook Mail Triage Assistant

The Outlook Mail Triage Assistant automates email management through the Microsoft Graph API, authenticating via @azure/msal-node with delegated permissions. It processes incoming messages in real-time using Graph subscriptions and webhooks. The agent performs zero-shot classification on email content to categorize messages into actionable buckets: urgent, informational, promotional, and follow-up required. It leverages the Graph API’s message endpoints to apply labels, move messages between folders, and flag items for follow-up with due dates. Advanced triage rules support sender reputation scoring, thread importance analysis based on participant lists, and attachment scanning metadata. The agent integrates with Outlook’s focused inbox API to programmatically adjust message priorities and creates digest summaries of low-priority batches. It also manages calendar invites embedded in emails, auto-responding to scheduling requests based on configurable availability windows.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/outlook-mail-triage-assistant/)
