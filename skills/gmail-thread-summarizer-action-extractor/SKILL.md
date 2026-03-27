---
name: "Gmail Thread Summarizer and Action Extractor"
description: "Fetches Gmail threads via the Gmail API (users.threads.get), extracts full message content, and produces a structured summary with action items, decisions, and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and handles forwarded thread chains."
category: "Calendar, Email & Productivity"
framework: "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/gmail-thread-summarizer-action-extractor/"
---

# Gmail Thread Summarizer and Action Extractor

Fetches Gmail threads via the Gmail API (users.threads.get), extracts full message content, and produces a structured summary with action items, decisions, and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and handles forwarded thread chains.

## Overview

Fetches Gmail threads via the Gmail API (users.threads.get), extracts full message content, and produces a structured summary with action items, decisions, and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and handles forwarded thread chains.

This skill authenticates with the Gmail API using OAuth2, fetches a thread by ID or search query (users.messages.list with q parameter), decodes base64url-encoded message parts, strips HTML to plain text, and runs summarization with action item extraction. Outputs structured JSON with: summary, action_items array (owner, deadline, description), decisions array, and key_contacts.

Use for inbox zero workflows, meeting prep, CRM note generation, and async team communication summaries. Not for real-time email triage at high volume — rate limit is 250 quota units/second. Not for emails with encrypted attachments. Requires Gmail API OAuth credentials with gmail.readonly scope. Handles threads up to 100 messages; very long threads may need chunking.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gmail-thread-summarizer-action-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gmail-thread-summarizer-action-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gmail-thread-summarizer-action-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gmail-thread-summarizer-action-extractor -a codex
```

### OpenClaw

```bash
clawhub install gmail-thread-summarizer-action-extractor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gmail-thread-summarizer-action-extractor/
