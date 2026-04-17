---
name: Strip quoted email history and signatures before summarizing inbound replies
description: Uses mail-parser-reply to isolate the newest human reply from text email
  threads while removing quoted history, signatures, and common disclaimers. This
  is useful when an agent needs the actionable part of an inbound email before routing,
  summarizing, or creating follow-up tasks.
category: Calendar, Email & Productivity
framework: Multi-Framework
verification: security_reviewed
source: https://github.com/alfonsrv/mail-parser-reply
tool_ecosystem:
  github_repo: alfonsrv/mail-parser-reply
  github_stars: 78
  tool: mail-parser-reply
---
# Strip quoted email history and signatures before summarizing inbound replies
Uses mail-parser-reply to isolate the newest human reply from text email threads while removing quoted history, signatures, and common disclaimers. This is useful when an agent needs the actionable part of an inbound email before routing, summarizing, or creating follow-up tasks.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/strip-quoted-email-history-and-signatures-before-summarizing-inbound-replies
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/strip-quoted-email-history-and-signatures-before-summarizing-inbound-replies` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/strip-quoted-email-history-and-signatures-before-summarizing-inbound-replies/)
