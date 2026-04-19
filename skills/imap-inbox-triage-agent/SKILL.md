---
title: "IMAP Inbox Triage Agent"
description: "The IMAP Inbox Triage Agent skill establishes secure IMAP connections to email providers including Gmail, Outlook 365, and Fastmail to perform intelligent inbox management. It fetches message headers and bodies using IMAP FETCH commands with envelope parsing for efficient bandwidth usage. Classification operates in two modes: rule-based filtering using sender, subject, and header patterns, and ML-driven categorization using embeddings similarity against user-defined category exemplars. Priority scoring combines sender importance, thread activity, keyword presence, and time sensitivity signals. Actions include auto-labeling via IMAP STORE with custom flags, folder moves using COPY and EXPUNGE sequences, and digest generation that summarizes unread messages by category. The agent handles IDLE push notifications for real-time processing and batch mode for periodic sweeps. OAuth2 XOAUTH2 authentication is supported for Gmail and Microsoft accounts alongside app-specific passwords for other providers."
source: "https://agentskillexchange.com/skills/imap-inbox-triage-agent/"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Codex"
---

# IMAP Inbox Triage Agent

The IMAP Inbox Triage Agent skill establishes secure IMAP connections to email providers including Gmail, Outlook 365, and Fastmail to perform intelligent inbox management. It fetches message headers and bodies using IMAP FETCH commands with envelope parsing for efficient bandwidth usage. Classification operates in two modes: rule-based filtering using sender, subject, and header patterns, and ML-driven categorization using embeddings similarity against user-defined category exemplars. Priority scoring combines sender importance, thread activity, keyword presence, and time sensitivity signals. Actions include auto-labeling via IMAP STORE with custom flags, folder moves using COPY and EXPUNGE sequences, and digest generation that summarizes unread messages by category. The agent handles IDLE push notifications for real-time processing and batch mode for periodic sweeps. OAuth2 XOAUTH2 authentication is supported for Gmail and Microsoft accounts alongside app-specific passwords for other providers.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imap-inbox-triage-agent/)
