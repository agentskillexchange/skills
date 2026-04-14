---
title: "Gmail Thread Summarizer and Action Extractor"
description: "Fetches Gmail threads via the Gmail API (users.threads.get), extracts full message content, and produces a structured summary with action items, decisions, and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and handles forwarded thread chains."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gmail-thread-summarizer-action-extractor/"
category:
  - "Calendar, Email &amp; Productivity"
---

# Gmail Thread Summarizer and Action Extractor

Fetches Gmail threads via the Gmail API (users.threads.get), extracts full message content, and produces a structured summary with action items, decisions, and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and handles forwarded thread chains.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gmail-thread-summarizer-action-extractor/)
