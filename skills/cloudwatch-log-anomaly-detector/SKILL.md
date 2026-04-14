---
title: "CloudWatch Log Anomaly Detector"
description: "Detects anomalous patterns in AWS CloudWatch Logs using CloudWatch Logs Insights queries and Anomaly Detection APIs. Surfaces error rate spikes and latency regressions with contextual log samples."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cloudwatch-log-anomaly-detector/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
---

# CloudWatch Log Anomaly Detector

The CloudWatch Log Anomaly Detector skill leverages AWS CloudWatch Logs Insights to run scheduled queries across log groups, identifying anomalous patterns in error rates, response latencies, and request volumes. It uses the CloudWatch Anomaly Detection API to create and manage anomaly detection models on custom metrics extracted from log data via metric filters. The skill automatically surfaces significant deviations with contextual log samples, presenting correlated events from multiple log streams. Supports integration with AWS SNS for alert delivery, AWS Lambda for automated remediation triggers, and S3 for long-term anomaly report archival. Features configurable sensitivity bands, training period management for detection models, and cross-account log aggregation via CloudWatch cross-account observability.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudwatch-log-anomaly-detector/)
