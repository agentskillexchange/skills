---
title: AWS S3 & SQS Pipeline Connector
description: The AWS S3 & SQS Pipeline Connector builds event-driven data processing
  pipelines using AWS SDK v3 modular clients. It combines S3 object storage with SQS
  message queuing for reliable, scalable data workflows. S3 operations use @aws-sdk/client-s3
  with commands including PutObjectCommand for uploads with server-side encryption
  (SSE-S3, SSE-KMS), GetObjectCommand for streaming downloads, CopyObjectCommand for
  cross-bucket transfers, and ListObjectsV2Command for inventory. Multipart uploads
  via CreateMultipartUploadCommand handle large files with configurable part sizes
  and parallel upload streams. SQS integration through @aws-sdk/client-sqs provides
  reliable message processing. SendMessageCommand and SendMessageBatchCommand handle
  message publishing with deduplication IDs for FIFO queues. ReceiveMessageCommand
  with WaitTimeSeconds enables long polling for efficient message consumption, and
  DeleteMessageCommand provides explicit acknowledgment after successful processing.
  The pipeline is connected via S3 Event Notifications configured to send s3:ObjectCreated:*
  events to SQS queues. The agent manages notification configuration through PutBucketNotificationConfigurationCommand,
  sets up dead-letter queues for failed processing, and implements visibility timeout
  management for retry handling. Additional features include S3 Select for server-side
  filtering with SelectObjectContentCommand, S3 Batch Operations for bulk processing,
  and CloudWatch metrics monitoring for queue depth alerting.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-s3-sqs-pipeline-connector/
category:
- Integrations &amp; Connectors
framework:
- MCP
---

# AWS S3 & SQS Pipeline Connector

The AWS S3 & SQS Pipeline Connector builds event-driven data processing pipelines using AWS SDK v3 modular clients. It combines S3 object storage with SQS message queuing for reliable, scalable data workflows. S3 operations use @aws-sdk/client-s3 with commands including PutObjectCommand for uploads with server-side encryption (SSE-S3, SSE-KMS), GetObjectCommand for streaming downloads, CopyObjectCommand for cross-bucket transfers, and ListObjectsV2Command for inventory. Multipart uploads via CreateMultipartUploadCommand handle large files with configurable part sizes and parallel upload streams. SQS integration through @aws-sdk/client-sqs provides reliable message processing. SendMessageCommand and SendMessageBatchCommand handle message publishing with deduplication IDs for FIFO queues. ReceiveMessageCommand with WaitTimeSeconds enables long polling for efficient message consumption, and DeleteMessageCommand provides explicit acknowledgment after successful processing. The pipeline is connected via S3 Event Notifications configured to send s3:ObjectCreated:* events to SQS queues. The agent manages notification configuration through PutBucketNotificationConfigurationCommand, sets up dead-letter queues for failed processing, and implements visibility timeout management for retry handling. Additional features include S3 Select for server-side filtering with SelectObjectContentCommand, S3 Batch Operations for bulk processing, and CloudWatch metrics monitoring for queue depth alerting.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-s3-sqs-pipeline-connector/)
