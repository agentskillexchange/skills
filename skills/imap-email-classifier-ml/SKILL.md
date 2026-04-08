---
title: IMAP Email Classifier
description: IMAP Email Classifier connects to any IMAP-compatible email server to
  automatically classify incoming messages into configurable categories. It uses scikit-learn
  TF-IDF vectorization with LinearSVC classifiers trained on user-labeled examples
  for high-accuracy categorization. SpaCy NER models extract entities like dates,
  monetary amounts, and organization names for structured metadata tagging. The tool
  supports IMAP IDLE for push-based real-time classification, MIME multipart parsing
  for attachment analysis, and S/MIME header verification. Custom rules engine allows
  regex-based overrides for known senders or subject patterns. It generates weekly
  email analytics including response time tracking, sender frequency analysis, and
  category volume trends. Integration with Microsoft Graph API enables dual Exchange/IMAP
  support. Training data management includes active learning loops for continuous
  model improvement.
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imap-email-classifier-ml/)
