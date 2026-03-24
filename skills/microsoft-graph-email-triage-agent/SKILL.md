---
name: "Microsoft Graph Email Triage Agent"
description: "Automates email triage using Microsoft Graph API v1.0 with delegated permissions. Classifies emails by urgency using NLP, applies Outlook rules, and surfaces action items to Microsoft To Do via Graph Tasks API."
category: "Calendar, Email & Productivity"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/microsoft-graph-email-triage-agent/"
---

# Microsoft Graph Email Triage Agent

Automates email triage using Microsoft Graph API v1.0 with delegated permissions. Classifies emails by urgency using NLP, applies Outlook rules, and surfaces action items to Microsoft To Do via Graph Tasks API.

## Overview

The Microsoft Graph Email Triage Agent brings intelligent automation to Outlook email management through the Microsoft Graph API v1.0. Using delegated permissions with Mail.ReadWrite and Tasks.ReadWrite scopes, it processes incoming messages to classify urgency, extract action items, and route emails to appropriate folders.

The triage pipeline applies multi-stage classification: sender importance scoring based on interaction history (reply frequency, meeting co-attendance from Calendar API), subject line and body NLP analysis for urgency keywords and deadline mentions, attachment type classification (contracts, invoices, code reviews), and thread activity detection for conversations requiring immediate response. Emails are automatically tagged with Outlook categories and moved to priority-based folders.

Extracted action items are created as tasks in Microsoft To Do via the Graph Tasks API, with due dates parsed from email content, linked back to the source message, and assigned to task lists based on project context. The agent generates daily digest emails summarizing triaged items, pending responses, and follow-up reminders. It supports custom classification rules defined in YAML and can integrate with Power Automate flows for complex routing scenarios.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-email-triage-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-email-triage-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-email-triage-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill microsoft-graph-email-triage-agent -a codex
```

### OpenClaw

```bash
clawhub install microsoft-graph-email-triage-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/microsoft-graph-email-triage-agent/
