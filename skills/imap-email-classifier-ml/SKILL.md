---
name: IMAP Email Classifier
description: Classifies and organizes emails from IMAP servers using imaplib and scikit-learn
  text classification. Supports custom label rules with SpaCy NER for entity extraction.
verification: security_reviewed
source: https://agentskillexchange.com/skills/imap-email-classifier-ml/
category:
- Calendar, Email &amp; Productivity
framework:
- ChatGPT Agents
---
# IMAP Email Classifier

IMAP Email Classifier connects to any IMAP-compatible email server to automatically classify incoming messages into configurable categories. It uses scikit-learn TF-IDF vectorization with LinearSVC classifiers trained on user-labeled examples for high-accuracy categorization. SpaCy NER models extract entities like dates, monetary amounts, and organization names for structured metadata tagging. The tool supports IMAP IDLE for push-based real-time classification, MIME multipart parsing for attachment analysis, and S/MIME header verification. Custom rules engine allows regex-based overrides for known senders or subject patterns. It generates weekly email analytics including response time tracking, sender frequency analysis, and category volume trends. Integration with Microsoft Graph API enables dual Exchange/IMAP support. Training data management includes active learning loops for continuous model improvement.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imap-email-classifier-ml/)
