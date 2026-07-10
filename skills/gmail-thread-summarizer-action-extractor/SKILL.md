---
title: "Gmail Thread Summarizer and Action Extractor"
description: "Fetches Gmail threads via the Gmail API (users.threads.get), extracts full message content, and produces a structured summary with action items, decisions, and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and handles forwarded thread chains."
verification: "security_reviewed"
source: "https://developers.google.com/gmail/api/reference/rest/v1/users.threads/get"
author: "Google"
category:
  - "Calendar, Email & Productivity"
framework:
  - "OpenClaw"
---

# Gmail Thread Summarizer and Action Extractor

Fetches Gmail threads via the Gmail API (users.threads.get), extracts full message content, and produces a structured summary with action items, decisions, and follow-ups. Uses MIME part decoding for multi-part HTML/plain text emails and handles forwarded thread chains.

## Prerequisites

Google account, Google Cloud project, Gmail API enabled, and OAuth 2.0 credentials

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Create a Google Cloud project, enable the Gmail API, configure OAuth 2.0 credentials, then authorize your app against the Gmail API.
```

## Documentation

- https://developers.google.com/gmail/api/reference/rest/v1/users.threads/get

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gmail-thread-summarizer-action-extractor/)
