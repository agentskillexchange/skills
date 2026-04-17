---
title: "Outlook Mail Triage Assistant"
description: "The Outlook Mail Triage Assistant automates email management through the Microsoft Graph API, authenticating via @azure/msal-node with delegated permissions. It processes incoming messages in real-time using Graph subscriptions and webhooks.\nThe agent performs zero-shot classification on email content to categorize messages into actionable buckets: urgent, informational, promotional, and follow-up required. It leverages the Graph API’s message endpoints to apply labels, move messages between folders, and flag items for follow-up with due dates.\nAdvanced triage rules support sender reputation scoring, thread importance analysis based on participant lists, and attachment scanning metadata. The agent integrates with Outlook’s focused inbox API to programmatically adjust message priorities and creates digest summaries of low-priority batches. It also manages calendar invites embedded in emails, auto-responding to scheduling requests based on configurable availability windows."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/outlook-mail-triage-assistant/"
framework:
  - "Claude Code"
---

# Outlook Mail Triage Assistant

The Outlook Mail Triage Assistant automates email management through the Microsoft Graph API, authenticating via @azure/msal-node with delegated permissions. It processes incoming messages in real-time using Graph subscriptions and webhooks.
The agent performs zero-shot classification on email content to categorize messages into actionable buckets: urgent, informational, promotional, and follow-up required. It leverages the Graph API’s message endpoints to apply labels, move messages between folders, and flag items for follow-up with due dates.
Advanced triage rules support sender reputation scoring, thread importance analysis based on participant lists, and attachment scanning metadata. The agent integrates with Outlook’s focused inbox API to programmatically adjust message priorities and creates digest summaries of low-priority batches. It also manages calendar invites embedded in emails, auto-responding to scheduling requests based on configurable availability windows.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/outlook-mail-triage-assistant
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/outlook-mail-triage-assistant` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/outlook-mail-triage-assistant/)
