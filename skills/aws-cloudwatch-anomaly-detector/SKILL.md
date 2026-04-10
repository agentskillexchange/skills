---
name: AWS CloudWatch Anomaly Detector
description: Uses AWS CloudWatch SDK (boto3) to configure anomaly detection bands
  on metrics via PutAnomalyDetector API. Integrates with SNS for notifications and
  CloudWatch Synthetics for canary-based uptime monitoring.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-detector/)
