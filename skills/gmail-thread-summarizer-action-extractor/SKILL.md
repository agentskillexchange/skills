---
title: "Gmail Thread Summarizer and Action Extractor"
description: "Fetches Gmail threads via the Gmail API (users.threads.get), extracts full message content, and produces a structured summary with action items, decisions, and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and handles forwarded thread chains."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/gmail-thread-summarizer-action-extractor/"
category:
  - "Calendar, Email & Productivity"
framework:
  - "OpenClaw"
---

# Gmail Thread Summarizer and Action Extractor

Fetches Gmail threads via the Gmail API (users.threads.get), extracts full message content, and produces a structured summary with action items, decisions, and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and handles forwarded thread chains.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gmail-thread-summarizer-action-extractor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gmail-thread-summarizer-action-extractor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gmail-thread-summarizer-action-extractor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gmail-thread-summarizer-action-extractor/)
