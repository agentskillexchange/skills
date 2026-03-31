---
name: "Outlook Mail Triage Assistant"
description: "Automated email triage using Microsoft Graph API and @azure/msal-node for OAuth. Classifies messages with zero-shot classification, applies Outlook rules, and manages focused inbox priorities."
category: "Calendar, Email &amp; Productivity"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/outlook-mail-triage-assistant/"
---
# Outlook Mail Triage Assistant

Automated email triage using Microsoft Graph API and @azure/msal-node for OAuth. Classifies messages with zero-shot classification, applies Outlook rules, and manages focused inbox priorities.

## Overview

The Outlook Mail Triage Assistant automates email management through the Microsoft Graph API, authenticating via @azure/msal-node with delegated permissions. It processes incoming messages in real-time using Graph subscriptions and webhooks.

The agent performs zero-shot classification on email content to categorize messages into actionable buckets: urgent, informational, promotional, and follow-up required. It leverages the Graph API's message endpoints to apply labels, move messages between folders, and flag items for follow-up with due dates.

Advanced triage rules support sender reputation scoring, thread importance analysis based on participant lists, and attachment scanning metadata. The agent integrates with Outlook's focused inbox API to programmatically adjust message priorities and creates digest summaries of low-priority batches. It also manages calendar invites embedded in emails, auto-responding to scheduling requests based on configurable availability windows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill outlook-mail-triage-assistant
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill outlook-mail-triage-assistant -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill outlook-mail-triage-assistant -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill outlook-mail-triage-assistant -a codex
```

### OpenClaw

```bash
clawhub install outlook-mail-triage-assistant
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/outlook-mail-triage-assistant/)
