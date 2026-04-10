---
title: "AWS S3 & SQS Pipeline Connector"
description: "Orchestrates AWS data pipelines using @aws-sdk/client-s3 and @aws-sdk/client-sqs. Manages S3 object lifecycle with PutObjectCommand/GetObjectCommand, processes SQS message queues via ReceiveMessageCommand with long polling, and configures S3 event notifications to SQS for event-driven processing."
slug: "aws-s3-sqs-pipeline-connector"
category:
  - "Integrations &amp; Connectors"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-s3-sqs-pipeline-connector/"
---

# AWS S3 & SQS Pipeline Connector

Orchestrates AWS data pipelines using @aws-sdk/client-s3 and @aws-sdk/client-sqs. Manages S3 object lifecycle with PutObjectCommand/GetObjectCommand, processes SQS message queues via ReceiveMessageCommand with long polling, and configures S3 event notifications to SQS for event-driven processing.

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
clawhub install aws-s3-sqs-pipeline-connector
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The AWS S3 & SQS Pipeline Connector builds event-driven data processing pipelines using AWS SDK v3 modular clients. It combines S3 object storage with SQS message queuing for reliable, scalable data workflows.
S3 operations use @aws-sdk/client-s3 with commands including PutObjectCommand for uploads with server-side encryption (SSE-S3, SSE-KMS), GetObjectCommand for streaming downloads, CopyObjectCommand for cross-bucket transfers, and ListObjectsV2Command for inventory. Multipart uploads via CreateMultipartUploadCommand handle large files with configurable part sizes and parallel upload streams.
SQS integration through @aws-sdk/client-sqs provides reliable message processing. SendMessageCommand and SendMessageBatchCommand handle message publishing with deduplication IDs for FIFO queues. ReceiveMessageCommand with WaitTimeSeconds enables long polling for efficient message consumption, and DeleteMessageCommand provides explicit acknowledgment after successful processing.
The pipeline is connected via S3 Event Notifications configured to send s3:ObjectCreated:* events to SQS queues. The agent manages notification configuration through PutBucketNotificationConfigurationCommand, sets up dead-letter queues for failed processing, and implements visibility timeout management for retry handling. Additional features include S3 Select for server-side filtering with SelectObjectContentCommand, S3 Batch Operations for bulk processing, and CloudWatch metrics monitoring for queue depth alerting.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-s3-sqs-pipeline-connector/)
