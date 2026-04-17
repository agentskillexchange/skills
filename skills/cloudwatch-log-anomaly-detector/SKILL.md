---
title: "CloudWatch Log Anomaly Detector"
description: "The CloudWatch Log Anomaly Detector skill leverages AWS CloudWatch Logs Insights to run scheduled queries across log groups, identifying anomalous patterns in error rates, response latencies, and request volumes. It uses the CloudWatch Anomaly Detection API to create and manage anomaly detection models on custom metrics extracted from log data via metric filters. The skill automatically surfaces significant deviations with contextual log samples, presenting correlated events from multiple log streams. Supports integration with AWS SNS for alert delivery, AWS Lambda for automated remediation triggers, and S3 for long-term anomaly report archival. Features configurable sensitivity bands, training period management for detection models, and cross-account log aggregation via CloudWatch cross-account observability."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cloudwatch-log-anomaly-detector/"
framework:
  - "Gemini"
---

# CloudWatch Log Anomaly Detector

The CloudWatch Log Anomaly Detector skill leverages AWS CloudWatch Logs Insights to run scheduled queries across log groups, identifying anomalous patterns in error rates, response latencies, and request volumes. It uses the CloudWatch Anomaly Detection API to create and manage anomaly detection models on custom metrics extracted from log data via metric filters. The skill automatically surfaces significant deviations with contextual log samples, presenting correlated events from multiple log streams. Supports integration with AWS SNS for alert delivery, AWS Lambda for automated remediation triggers, and S3 for long-term anomaly report archival. Features configurable sensitivity bands, training period management for detection models, and cross-account log aggregation via CloudWatch cross-account observability.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cloudwatch-log-anomaly-detector
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/cloudwatch-log-anomaly-detector` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudwatch-log-anomaly-detector/)
