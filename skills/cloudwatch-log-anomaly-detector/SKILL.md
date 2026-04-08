---
title: CloudWatch Log Anomaly Detector
description: The CloudWatch Log Anomaly Detector skill leverages AWS CloudWatch Logs
  Insights to run scheduled queries across log groups, identifying anomalous patterns
  in error rates, response latencies, and request volumes. It uses the CloudWatch
  Anomaly Detection API to create and manage anomaly detection models on custom metrics
  extracted from log data via metric filters. The skill automatically surfaces significant
  deviations with contextual log samples, presenting correlated events from multiple
  log streams. Supports integration with AWS SNS for alert delivery, AWS Lambda for
  automated remediation triggers, and S3 for long-term anomaly report archival. Features
  configurable sensitivity bands, training period management for detection models,
  and cross-account log aggregation via CloudWatch cross-account observability.
verification: security_reviewed
source: https://agentskillexchange.com/skills/cloudwatch-log-anomaly-detector/
category:
- Monitoring &amp; Alerts
framework:
- Gemini
---

# CloudWatch Log Anomaly Detector

The CloudWatch Log Anomaly Detector skill leverages AWS CloudWatch Logs Insights to run scheduled queries across log groups, identifying anomalous patterns in error rates, response latencies, and request volumes. It uses the CloudWatch Anomaly Detection API to create and manage anomaly detection models on custom metrics extracted from log data via metric filters. The skill automatically surfaces significant deviations with contextual log samples, presenting correlated events from multiple log streams. Supports integration with AWS SNS for alert delivery, AWS Lambda for automated remediation triggers, and S3 for long-term anomaly report archival. Features configurable sensitivity bands, training period management for detection models, and cross-account log aggregation via CloudWatch cross-account observability.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudwatch-log-anomaly-detector/)
