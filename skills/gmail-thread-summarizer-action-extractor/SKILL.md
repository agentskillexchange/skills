---
title: "Gmail Thread Summarizer and Action Extractor"
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
