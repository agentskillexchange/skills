---
name: "IMAP Inbox Triage Agent"
description: "Connects to IMAP email servers to classify, prioritize, and auto-label incoming messages using rule-based and ML-driven filtering. Supports Gmail, Outlook, and Fastmail."
category: "Calendar, Email & Productivity"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/imap-inbox-triage-agent/"
---

# IMAP Inbox Triage Agent

Connects to IMAP email servers to classify, prioritize, and auto-label incoming messages using rule-based and ML-driven filtering. Supports Gmail, Outlook, and Fastmail.

## Overview

The IMAP Inbox Triage Agent skill establishes secure IMAP connections to email providers including Gmail, Outlook 365, and Fastmail to perform intelligent inbox management. It fetches message headers and bodies using IMAP FETCH commands with envelope parsing for efficient bandwidth usage.

Classification operates in two modes: rule-based filtering using sender, subject, and header patterns, and ML-driven categorization using embeddings similarity against user-defined category exemplars. Priority scoring combines sender importance, thread activity, keyword presence, and time sensitivity signals.

Actions include auto-labeling via IMAP STORE with custom flags, folder moves using COPY and EXPUNGE sequences, and digest generation that summarizes unread messages by category. The agent handles IDLE push notifications for real-time processing and batch mode for periodic sweeps. OAuth2 XOAUTH2 authentication is supported for Gmail and Microsoft accounts alongside app-specific passwords for other providers.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill imap-inbox-triage-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill imap-inbox-triage-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill imap-inbox-triage-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill imap-inbox-triage-agent -a codex
```

### OpenClaw

```bash
clawhub install imap-inbox-triage-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/imap-inbox-triage-agent/
