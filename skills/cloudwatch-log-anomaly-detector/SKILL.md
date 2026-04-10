---
title: "CloudWatch Log Anomaly Detector"
description: "Detects anomalous patterns in AWS CloudWatch Logs using CloudWatch Logs Insights queries and Anomaly Detection APIs. Surfaces error rate spikes and latency regressions with contextual log samples."
slug: "cloudwatch-log-anomaly-detector"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cloudwatch-log-anomaly-detector/"
---

# CloudWatch Log Anomaly Detector

Detects anomalous patterns in AWS CloudWatch Logs using CloudWatch Logs Insights queries and Anomaly Detection APIs. Surfaces error rate spikes and latency regressions with contextual log samples.

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
clawhub install cloudwatch-log-anomaly-detector
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CloudWatch Log Anomaly Detector skill leverages AWS CloudWatch Logs Insights to run scheduled queries across log groups, identifying anomalous patterns in error rates, response latencies, and request volumes. It uses the CloudWatch Anomaly Detection API to create and manage anomaly detection models on custom metrics extracted from log data via metric filters. The skill automatically surfaces significant deviations with contextual log samples, presenting correlated events from multiple log streams. Supports integration with AWS SNS for alert delivery, AWS Lambda for automated remediation triggers, and S3 for long-term anomaly report archival. Features configurable sensitivity bands, training period management for detection models, and cross-account log aggregation via CloudWatch cross-account observability.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudwatch-log-anomaly-detector/)
