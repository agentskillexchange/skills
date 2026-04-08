---
title: AWS CloudWatch Anomaly Detector
description: The AWS CloudWatch Anomaly Detector uses the boto3 CloudWatch client
  to configure intelligent anomaly detection across your AWS infrastructure. It calls
  the PutAnomalyDetector API to create machine-learning-based anomaly detection bands
  on any CloudWatch metric, automatically learning seasonal patterns and baseline
  behavior. The agent configures composite alarms that combine anomaly detection with
  static thresholds using the PutCompositeAlarm API for nuanced alerting logic. CloudWatch
  Synthetics canaries are managed through the Synthetics client to create browser-based
  and API endpoint uptime monitors with configurable check intervals. Alert notifications
  flow through SNS topics with subscription filters for routing to email, SMS, Slack
  via AWS Chatbot, or Lambda functions for custom remediation. The detector supports
  cross-account metric aggregation using CloudWatch cross-account observability features
  for centralized monitoring dashboards.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-detector/
category:
- Monitoring &amp; Alerts
framework:
- MCP
---

# AWS CloudWatch Anomaly Detector

The AWS CloudWatch Anomaly Detector uses the boto3 CloudWatch client to configure intelligent anomaly detection across your AWS infrastructure. It calls the PutAnomalyDetector API to create machine-learning-based anomaly detection bands on any CloudWatch metric, automatically learning seasonal patterns and baseline behavior. The agent configures composite alarms that combine anomaly detection with static thresholds using the PutCompositeAlarm API for nuanced alerting logic. CloudWatch Synthetics canaries are managed through the Synthetics client to create browser-based and API endpoint uptime monitors with configurable check intervals. Alert notifications flow through SNS topics with subscription filters for routing to email, SMS, Slack via AWS Chatbot, or Lambda functions for custom remediation. The detector supports cross-account metric aggregation using CloudWatch cross-account observability features for centralized monitoring dashboards.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-detector/)
