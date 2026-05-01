---
title: "Strip quoted email history and signatures before summarizing inbound replies"
description: "Uses mail-parser-reply to isolate the newest human reply from text email threads while removing quoted history, signatures, and common disclaimers. This is useful when an agent needs the actionable part of an inbound email before routing, summarizing, or creating follow-up tasks."
verification: "security_reviewed"
source: "https://github.com/alfonsrv/mail-parser-reply"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "alfonsrv/mail-parser-reply"
  github_stars: 78
---

# Strip quoted email history and signatures before summarizing inbound replies

This ASE entry is built around mail-parser-reply, the Python project from alfonsrv/mail-parser-reply that splits text email threads into replies and can strip headers, signatures, and disclaimers across multiple languages. The agent job here is precise: receive a text email body from an inbox, webhook, or helpdesk system, isolate the newest reply, and hand only the useful human-written content to the next step. That dramatically reduces noise when downstream automations are classifying intent, drafting acknowledgements, summarizing conversations, or routing a message to support, sales, or operations queues.

Use this instead of treating the whole thread as the payload. An agent can pair mail-parser-reply with Gmail, IMAP, Microsoft Graph, or a ticketing webhook, then keep only the latest response before passing it into a summarizer, CRM logger, escalation router, or task generator. The multilingual support is a real boundary-clearer here, because agents often receive replies from customers or teammates using different mail clients and different reply header conventions.

The scope boundary keeps this from being just another email tool listing. mail-parser-reply does not send mail, manage inboxes, parse attachments, or replace a full MIME parser. It specializes in text-thread cleanup and latest-reply extraction. In other words, it solves one repeated operator problem inside email-heavy automations, and it integrates cleanly with richer mail ingestion stacks such as MailParser or provider APIs that handle the raw message retrieval first.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/strip-quoted-email-history-and-signatures-before-summarizing-inbound-replies/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/strip-quoted-email-history-and-signatures-before-summarizing-inbound-replies
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/strip-quoted-email-history-and-signatures-before-summarizing-inbound-replies`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/strip-quoted-email-history-and-signatures-before-summarizing-inbound-replies/)
