---
title: "IMAP Inbox Triage Agent"
description: "Connects to IMAP email servers to classify, prioritize, and auto-label incoming messages using rule-based and ML-driven filtering. Supports Gmail, Outlook, and Fastmail."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/imap-inbox-triage-agent/"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Codex"
---

# IMAP Inbox Triage Agent

The IMAP Inbox Triage Agent skill establishes secure IMAP connections to email providers including Gmail, Outlook 365, and Fastmail to perform intelligent inbox management. It fetches message headers and bodies using IMAP FETCH commands with envelope parsing for efficient bandwidth usage. Classification operates in two modes: rule-based filtering using sender, subject, and header patterns, and ML-driven categorization using embeddings similarity against user-defined category exemplars. Priority scoring combines sender importance, thread activity, keyword presence, and time sensitivity signals. Actions include auto-labeling via IMAP STORE with custom flags, folder moves using COPY and EXPUNGE sequences, and digest generation that summarizes unread messages by category. The agent handles IDLE push notifications for real-time processing and batch mode for periodic sweeps. OAuth2 XOAUTH2 authentication is supported for Gmail and Microsoft accounts alongside app-specific passwords for other providers.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/imap-inbox-triage-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/imap-inbox-triage-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/imap-inbox-triage-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imap-inbox-triage-agent/)
