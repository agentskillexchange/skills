---
name: "Gmail Thread Summarizer and Action Extractor"
description: "Fetches Gmail threads via the Gmail API (users.threads.get), extracts full message content, and produces a structured summary with action items, decisions, and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and handles forwarded thread chains."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gmail-thread-summarizer-action-extractor/"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "OpenClaw"
---

# Gmail Thread Summarizer and Action Extractor

Fetches Gmail threads via the Gmail API (users.threads.get), extracts full message content, and produces a structured summary with action items, decisions, and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and handles forwarded thread chains.
This skill authenticates with the Gmail API using OAuth2, fetches a thread by ID or search query (users.messages.list with q parameter), decodes base64url-encoded message parts, strips HTML to plain text, and runs summarization with action item extraction. Outputs structured JSON with: summary, action_items array (owner, deadline, description), decisions array, and key_contacts.
Use for inbox zero workflows, meeting prep, CRM note generation, and async team communication summaries. Not for real-time email triage at high volume — rate limit is 250 quota units/second. Not for emails with encrypted attachments. Requires Gmail API OAuth credentials with gmail.readonly scope. Handles threads up to 100 messages; very long threads may need chunking.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gmail-thread-summarizer-action-extractor/)
