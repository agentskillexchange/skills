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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imap-email-classifier-ml/)
