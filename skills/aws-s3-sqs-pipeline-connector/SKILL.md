---
name: "AWS S3 & SQS Pipeline Connector"
description: "Orchestrates AWS data pipelines using @aws-sdk/client-s3 and @aws-sdk/client-sqs. Manages S3 object lifecycle with PutObjectCommand/GetObjectCommand, processes SQS message queues via ReceiveMessageCommand with long polling, and configures S3 event notifications to SQS for event-driven processing."
category: "Integrations &amp; Connectors"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-s3-sqs-pipeline-connector/"
---
# AWS S3 & SQS Pipeline Connector

Orchestrates AWS data pipelines using @aws-sdk/client-s3 and @aws-sdk/client-sqs. Manages S3 object lifecycle with PutObjectCommand/GetObjectCommand, processes SQS message queues via ReceiveMessageCommand with long polling, and configures S3 event notifications to SQS for event-driven processing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-s3-sqs-pipeline-connector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-s3-sqs-pipeline-connector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-s3-sqs-pipeline-connector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-s3-sqs-pipeline-connector -a codex
```

### OpenClaw

```bash
clawhub install aws-s3-sqs-pipeline-connector
```

## Details

The AWS S3 & SQS Pipeline Connector builds event-driven data processing pipelines using AWS SDK v3 modular clients. It combines S3 object storage with SQS message queuing for reliable, scalable data workflows.

S3 operations use @aws-sdk/client-s3 with commands including PutObjectCommand for uploads with server-side encryption (SSE-S3, SSE-KMS), GetObjectCommand for streaming downloads, CopyObjectCommand for cross-bucket transfers, and ListObjectsV2Command for inventory. Multipart uploads via CreateMultipartUploadCommand handle large files with configurable part sizes and parallel upload streams.

SQS integration through @aws-sdk/client-sqs provides reliable message processing. SendMessageCommand and SendMessageBatchCommand handle message publishing with deduplication IDs for FIFO queues. ReceiveMessageCommand with WaitTimeSeconds enables long polling for efficient message consumption, and DeleteMessageCommand provides explicit acknowledgment after successful processing.

The pipeline is connected via S3 Event Notifications configured to send s3:ObjectCreated:* events to SQS queues. The agent manages notification configuration through PutBucketNotificationConfigurationCommand, sets up dead-letter queues for failed processing, and implements visibility timeout management for retry handling. Additional features include S3 Select for server-side filtering with SelectObjectContentCommand, S3 Batch Operations for bulk processing, and CloudWatch metrics monitoring for queue depth alerting.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-s3-sqs-pipeline-connector/)
