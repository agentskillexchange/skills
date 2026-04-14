---
title: "AWS S3 & SQS Pipeline Connector"
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

# AWS S3 & SQS Pipeline Connector

The AWS S3 & SQS Pipeline Connector builds event-driven data processing pipelines using AWS SDK v3 modular clients. It combines S3 object storage with SQS message queuing for reliable, scalable data workflows.

S3 operations use @aws-sdk/client-s3 with commands including PutObjectCommand for uploads with server-side encryption (SSE-S3, SSE-KMS), GetObjectCommand for streaming downloads, CopyObjectCommand for cross-bucket transfers, and ListObjectsV2Command for inventory. Multipart uploads via CreateMultipartUploadCommand handle large files with configurable part sizes and parallel upload streams.

SQS integration through @aws-sdk/client-sqs provides reliable message processing. SendMessageCommand and SendMessageBatchCommand handle message publishing with deduplication IDs for FIFO queues. ReceiveMessageCommand with WaitTimeSeconds enables long polling for efficient message consumption, and DeleteMessageCommand provides explicit acknowledgment after successful processing.

The pipeline is connected via S3 Event Notifications configured to send s3:ObjectCreated:* events to SQS queues. The agent manages notification configuration through PutBucketNotificationConfigurationCommand, sets up dead-letter queues for failed processing, and implements visibility timeout management for retry handling. Additional features include S3 Select for server-side filtering with SelectObjectContentCommand, S3 Batch Operations for bulk processing, and CloudWatch metrics monitoring for queue depth alerting.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-s3-sqs-pipeline-connector/)
