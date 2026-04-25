---
title: "Microsoft Graph Email Triage Agent"
description: "Automates email triage using Microsoft Graph API v1.0 with delegated permissions. Classifies emails by urgency using NLP, applies Outlook rules, and surfaces action items to Microsoft To Do via Graph Tasks API."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/microsoft-graph-email-triage-agent/"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Claude Code"
---

# Microsoft Graph Email Triage Agent

The Microsoft Graph Email Triage Agent brings intelligent automation to Outlook email management through the Microsoft Graph API v1.0. Using delegated permissions with Mail.ReadWrite and Tasks.ReadWrite scopes, it processes incoming messages to classify urgency, extract action items, and route emails to appropriate folders.

The triage pipeline applies multi-stage classification: sender importance scoring based on interaction history (reply frequency, meeting co-attendance from Calendar API), subject line and body NLP analysis for urgency keywords and deadline mentions, attachment type classification (contracts, invoices, code reviews), and thread activity detection for conversations requiring immediate response. Emails are automatically tagged with Outlook categories and moved to priority-based folders.

Extracted action items are created as tasks in Microsoft To Do via the Graph Tasks API, with due dates parsed from email content, linked back to the source message, and assigned to task lists based on project context. The agent generates daily digest emails summarizing triaged items, pending responses, and follow-up reminders. It supports custom classification rules defined in YAML and can integrate with Power Automate flows for complex routing scenarios.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/microsoft-graph-email-triage-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/microsoft-graph-email-triage-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/microsoft-graph-email-triage-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/microsoft-graph-email-triage-agent/)
