---
title: "CloudWatch Log Anomaly Detector"
description: "Detects anomalous patterns in AWS CloudWatch Logs using CloudWatch Logs Insights queries and Anomaly Detection APIs. Surfaces error rate spikes and latency regressions with contextual log samples."
verification: "security_reviewed"
source: "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection.html"
category:
  - "Monitoring & Alerts"
framework:
  - "Gemini"
---

# CloudWatch Log Anomaly Detector

The CloudWatch Log Anomaly Detector skill leverages AWS CloudWatch Logs Insights to run scheduled queries across log groups, identifying anomalous patterns in error rates, response latencies, and request volumes. It uses the CloudWatch Anomaly Detection API to create and manage anomaly detection models on custom metrics extracted from log data via metric filters. The skill automatically surfaces significant deviations with contextual log samples, presenting correlated events from multiple log streams. Supports integration with AWS SNS for alert delivery, AWS Lambda for automated remediation triggers, and S3 for long-term anomaly report archival. Features configurable sensitivity bands, training period management for detection models, and cross-account log aggregation via CloudWatch cross-account observability.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/cloudwatch-log-anomaly-detector/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cloudwatch-log-anomaly-detector
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/cloudwatch-log-anomaly-detector`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudwatch-log-anomaly-detector/)
