---
title: "IMAP Email Classifier"
description: "Classifies and organizes emails from IMAP servers using imaplib and scikit-learn text classification. Supports custom label rules with SpaCy NER for entity extraction."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/imap-email-classifier-ml/"
category:
  - "Calendar, Email & Productivity"
framework:
  - "ChatGPT Agents"
---

# IMAP Email Classifier

IMAP Email Classifier connects to any IMAP-compatible email server to automatically classify incoming messages into configurable categories. It uses scikit-learn TF-IDF vectorization with LinearSVC classifiers trained on user-labeled examples for high-accuracy categorization. SpaCy NER models extract entities like dates, monetary amounts, and organization names for structured metadata tagging. The tool supports IMAP IDLE for push-based real-time classification, MIME multipart parsing for attachment analysis, and S/MIME header verification. Custom rules engine allows regex-based overrides for known senders or subject patterns. It generates weekly email analytics including response time tracking, sender frequency analysis, and category volume trends. Integration with Microsoft Graph API enables dual Exchange/IMAP support. Training data management includes active learning loops for continuous model improvement.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/imap-email-classifier-ml/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/imap-email-classifier-ml
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/imap-email-classifier-ml`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imap-email-classifier-ml/)
