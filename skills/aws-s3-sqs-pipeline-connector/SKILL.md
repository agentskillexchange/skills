---
title: "AWS S3 &#038; SQS Pipeline Connector"
description: "Orchestrates AWS data pipelines using @aws-sdk/client-s3 and @aws-sdk/client-sqs. Manages S3 object lifecycle with PutObjectCommand/GetObjectCommand, processes SQS message queues via ReceiveMessageCommand with long polling, and configures S3 event notifications to SQS for event-driven processing."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS S3 &#038; SQS Pipeline Connector

Orchestrates AWS data pipelines using @aws-sdk/client-s3 and @aws-sdk/client-sqs. Manages S3 object lifecycle with PutObjectCommand/GetObjectCommand, processes SQS message queues via ReceiveMessageCommand with long polling, and configures S3 event notifications to SQS for event-driven processing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/aws-s3-sqs-pipeline-connector/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-s3-sqs-pipeline-connector
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/aws-s3-sqs-pipeline-connector`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-s3-sqs-pipeline-connector/)
