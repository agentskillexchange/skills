---
name: "IMAP Email Classifier"
description: "Classifies and organizes emails from IMAP servers using imaplib and scikit-learn text classification. Supports custom label rules with SpaCy NER for entity extraction."
category: "Calendar, Email & Productivity"
framework: "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/imap-email-classifier-ml/"
---

# IMAP Email Classifier

Classifies and organizes emails from IMAP servers using imaplib and scikit-learn text classification. Supports custom label rules with SpaCy NER for entity extraction.

## Overview

IMAP Email Classifier connects to any IMAP-compatible email server to automatically classify incoming messages into configurable categories. It uses scikit-learn TF-IDF vectorization with LinearSVC classifiers trained on user-labeled examples for high-accuracy categorization. SpaCy NER models extract entities like dates, monetary amounts, and organization names for structured metadata tagging. The tool supports IMAP IDLE for push-based real-time classification, MIME multipart parsing for attachment analysis, and S/MIME header verification. Custom rules engine allows regex-based overrides for known senders or subject patterns. It generates weekly email analytics including response time tracking, sender frequency analysis, and category volume trends. Integration with Microsoft Graph API enables dual Exchange/IMAP support. Training data management includes active learning loops for continuous model improvement.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill imap-email-classifier-ml
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill imap-email-classifier-ml -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill imap-email-classifier-ml -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill imap-email-classifier-ml -a codex
```

### OpenClaw

```bash
clawhub install imap-email-classifier-ml
```

## Source

- Marketplace: https://agentskillexchange.com/skills/imap-email-classifier-ml/
