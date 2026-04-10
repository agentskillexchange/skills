---
name: IMAP Inbox Triage Agent
description: Connects to IMAP email servers to classify, prioritize, and auto-label
  incoming messages using rule-based and ML-driven filtering. Supports Gmail, Outlook,
  and Fastmail.
verification: security_reviewed
source: https://agentskillexchange.com/skills/imap-inbox-triage-agent/
category:
- Calendar, Email &amp; Productivity
framework:
- Codex
---
# IMAP Inbox Triage Agent

The IMAP Inbox Triage Agent skill establishes secure IMAP connections to email providers including Gmail, Outlook 365, and Fastmail to perform intelligent inbox management. It fetches message headers and bodies using IMAP FETCH commands with envelope parsing for efficient bandwidth usage.
Classification operates in two modes: rule-based filtering using sender, subject, and header patterns, and ML-driven categorization using embeddings similarity against user-defined category exemplars. Priority scoring combines sender importance, thread activity, keyword presence, and time sensitivity signals.
Actions include auto-labeling via IMAP STORE with custom flags, folder moves using COPY and EXPUNGE sequences, and digest generation that summarizes unread messages by category. The agent handles IDLE push notifications for real-time processing and batch mode for periodic sweeps. OAuth2 XOAUTH2 authentication is supported for Gmail and Microsoft accounts alongside app-specific passwords for other providers.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imap-inbox-triage-agent/)
