---
title: "Outlook Mail Triage Assistant"
description: "Automated email triage using Microsoft Graph API and @azure/msal-node for OAuth. Classifies messages with zero-shot classification, applies Outlook rules, and manages focused inbox priorities."
slug: "outlook-mail-triage-assistant"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/outlook-mail-triage-assistant/"
listed: true
---

# Outlook Mail Triage Assistant

Automated email triage using Microsoft Graph API and @azure/msal-node for OAuth. Classifies messages with zero-shot classification, applies Outlook rules, and manages focused inbox priorities.

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
clawhub install outlook-mail-triage-assistant
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Outlook Mail Triage Assistant automates email management through the Microsoft Graph API, authenticating via @azure/msal-node with delegated permissions. It processes incoming messages in real-time using Graph subscriptions and webhooks.
The agent performs zero-shot classification on email content to categorize messages into actionable buckets: urgent, informational, promotional, and follow-up required. It leverages the Graph API’s message endpoints to apply labels, move messages between folders, and flag items for follow-up with due dates.
Advanced triage rules support sender reputation scoring, thread importance analysis based on participant lists, and attachment scanning metadata. The agent integrates with Outlook’s focused inbox API to programmatically adjust message priorities and creates digest summaries of low-priority batches. It also manages calendar invites embedded in emails, auto-responding to scheduling requests based on configurable availability windows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/outlook-mail-triage-assistant/)
