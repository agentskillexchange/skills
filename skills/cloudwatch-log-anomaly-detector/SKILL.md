---
title: "CloudWatch Log Anomaly Detector"
description: "Detects anomalous patterns in AWS CloudWatch Logs using CloudWatch Logs Insights queries and Anomaly Detection APIs. Surfaces error rate spikes and latency regressions with contextual log samples."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cloudwatch-log-anomaly-detector/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
---

# CloudWatch Log Anomaly Detector

The CloudWatch Log Anomaly Detector skill leverages AWS CloudWatch Logs Insights to run scheduled queries across log groups, identifying anomalous patterns in error rates, response latencies, and request volumes. It uses the CloudWatch Anomaly Detection API to create and manage anomaly detection models on custom metrics extracted from log data via metric filters. The skill automatically surfaces significant deviations with contextual log samples, presenting correlated events from multiple log streams. Supports integration with AWS SNS for alert delivery, AWS Lambda for automated remediation triggers, and S3 for long-term anomaly report archival. Features configurable sensitivity bands, training period management for detection models, and cross-account log aggregation via CloudWatch cross-account observability.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudwatch-log-anomaly-detector/)
