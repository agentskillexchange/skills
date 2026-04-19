---
title: "Outlook Mail Triage Assistant"
description: "The Outlook Mail Triage Assistant automates email management through the Microsoft Graph API, authenticating via @azure/msal-node with delegated permissions. It processes incoming messages in real-time using Graph subscriptions and webhooks. The agent performs zero-shot classification on email content to categorize messages into actionable buckets: urgent, informational, promotional, and follow-up required. It leverages the Graph API&#8217;s message endpoints to apply labels, move messages between folders, and flag items for follow-up with due dates. Advanced triage rules support sender reputation scoring, thread importance analysis based on participant lists, and attachment scanning metadata. The agent integrates with Outlook&#8217;s focused inbox API to programmatically adjust message priorities and creates digest summaries of low-priority batches. It also manages calendar invites embedded in emails, auto-responding to scheduling requests based on configurable availability windows."
source: "https://agentskillexchange.com/skills/outlook-mail-triage-assistant/"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Claude Code"
---

# Outlook Mail Triage Assistant

The Outlook Mail Triage Assistant automates email management through the Microsoft Graph API, authenticating via @azure/msal-node with delegated permissions. It processes incoming messages in real-time using Graph subscriptions and webhooks. The agent performs zero-shot classification on email content to categorize messages into actionable buckets: urgent, informational, promotional, and follow-up required. It leverages the Graph API&#8217;s message endpoints to apply labels, move messages between folders, and flag items for follow-up with due dates. Advanced triage rules support sender reputation scoring, thread importance analysis based on participant lists, and attachment scanning metadata. The agent integrates with Outlook&#8217;s focused inbox API to programmatically adjust message priorities and creates digest summaries of low-priority batches. It also manages calendar invites embedded in emails, auto-responding to scheduling requests based on configurable availability windows.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/outlook-mail-triage-assistant/)
