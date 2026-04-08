---
title: Gmail Thread Summarizer and Action Extractor
description: 'Fetches Gmail threads via the Gmail API (users.threads.get), extracts
  full message content, and produces a structured summary with action items, decisions,
  and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and
  handles forwarded thread chains. This skill authenticates with the Gmail API using
  OAuth2, fetches a thread by ID or search query (users.messages.list with q parameter),
  decodes base64url-encoded message parts, strips HTML to plain text, and runs summarization
  with action item extraction. Outputs structured JSON with: summary, action_items
  array (owner, deadline, description), decisions array, and key_contacts. Use for
  inbox zero workflows, meeting prep, CRM note generation, and async team communication
  summaries. Not for real-time email triage at high volume — rate limit is 250 quota
  units/second. Not for emails with encrypted attachments. Requires Gmail API OAuth
  credentials with gmail.readonly scope. Handles threads up to 100 messages; very
  long threads may need chunking.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/gmail-thread-summarizer-action-extractor/
category:
- Calendar, Email &amp; Productivity
framework:
- OpenClaw
---

# Gmail Thread Summarizer and Action Extractor

Fetches Gmail threads via the Gmail API (users.threads.get), extracts full message content, and produces a structured summary with action items, decisions, and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and handles forwarded thread chains. This skill authenticates with the Gmail API using OAuth2, fetches a thread by ID or search query (users.messages.list with q parameter), decodes base64url-encoded message parts, strips HTML to plain text, and runs summarization with action item extraction. Outputs structured JSON with: summary, action_items array (owner, deadline, description), decisions array, and key_contacts. Use for inbox zero workflows, meeting prep, CRM note generation, and async team communication summaries. Not for real-time email triage at high volume — rate limit is 250 quota units/second. Not for emails with encrypted attachments. Requires Gmail API OAuth credentials with gmail.readonly scope. Handles threads up to 100 messages; very long threads may need chunking.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gmail-thread-summarizer-action-extractor/)
