---
name: Gmail Thread Summarizer and Action Extractor
description: Fetches Gmail threads via the Gmail API (users.threads.get), extracts
  full message content, and produces a structured summary with action items, decisions,
  and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and
  handles forwarded thread chains.
category: Calendar, Email & Productivity
framework: OpenClaw
verification: security_reviewed
source: https://agentskillexchange.com/skills/gmail-thread-summarizer-action-extractor/
---
# Gmail Thread Summarizer and Action Extractor
Fetches Gmail threads via the Gmail API (users.threads.get), extracts full message content, and produces a structured summary with action items, decisions, and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and handles forwarded thread chains.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gmail-thread-summarizer-action-extractor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gmail-thread-summarizer-action-extractor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gmail-thread-summarizer-action-extractor/)
