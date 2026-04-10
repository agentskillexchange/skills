---
title: "IMAP Inbox Triage Agent"
description: "Connects to IMAP email servers to classify, prioritize, and auto-label incoming messages using rule-based and ML-driven filtering. Supports Gmail, Outlook, and Fastmail."
slug: "imap-inbox-triage-agent"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/imap-inbox-triage-agent/"
listed: true
---

# IMAP Inbox Triage Agent

Connects to IMAP email servers to classify, prioritize, and auto-label incoming messages using rule-based and ML-driven filtering. Supports Gmail, Outlook, and Fastmail.

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
clawhub install imap-inbox-triage-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The IMAP Inbox Triage Agent skill establishes secure IMAP connections to email providers including Gmail, Outlook 365, and Fastmail to perform intelligent inbox management. It fetches message headers and bodies using IMAP FETCH commands with envelope parsing for efficient bandwidth usage.
Classification operates in two modes: rule-based filtering using sender, subject, and header patterns, and ML-driven categorization using embeddings similarity against user-defined category exemplars. Priority scoring combines sender importance, thread activity, keyword presence, and time sensitivity signals.
Actions include auto-labeling via IMAP STORE with custom flags, folder moves using COPY and EXPUNGE sequences, and digest generation that summarizes unread messages by category. The agent handles IDLE push notifications for real-time processing and batch mode for periodic sweeps. OAuth2 XOAUTH2 authentication is supported for Gmail and Microsoft accounts alongside app-specific passwords for other providers.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imap-inbox-triage-agent/)
