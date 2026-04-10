---
title: "IMAP Email Classifier"
description: "Classifies and organizes emails from IMAP servers using imaplib and scikit-learn text classification. Supports custom label rules with SpaCy NER for entity extraction."
slug: "imap-email-classifier-ml"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/imap-email-classifier-ml/"
listed: true
---

# IMAP Email Classifier

Classifies and organizes emails from IMAP servers using imaplib and scikit-learn text classification. Supports custom label rules with SpaCy NER for entity extraction.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install imap-email-classifier-ml
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

IMAP Email Classifier connects to any IMAP-compatible email server to automatically classify incoming messages into configurable categories. It uses scikit-learn TF-IDF vectorization with LinearSVC classifiers trained on user-labeled examples for high-accuracy categorization. SpaCy NER models extract entities like dates, monetary amounts, and organization names for structured metadata tagging. The tool supports IMAP IDLE for push-based real-time classification, MIME multipart parsing for attachment analysis, and S/MIME header verification. Custom rules engine allows regex-based overrides for known senders or subject patterns. It generates weekly email analytics including response time tracking, sender frequency analysis, and category volume trends. Integration with Microsoft Graph API enables dual Exchange/IMAP support. Training data management includes active learning loops for continuous model improvement.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imap-email-classifier-ml/)
