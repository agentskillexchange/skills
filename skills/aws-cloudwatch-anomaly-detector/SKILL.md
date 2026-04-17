---
title: "AWS CloudWatch Anomaly Detector"
description: "The AWS CloudWatch Anomaly Detector uses the boto3 CloudWatch client to configure intelligent anomaly detection across your AWS infrastructure. It calls the PutAnomalyDetector API to create machine-learning-based anomaly detection bands on any CloudWatch metric, automatically learning seasonal patterns and baseline behavior. The agent configures composite alarms that combine anomaly detection with static thresholds using the PutCompositeAlarm API for nuanced alerting logic. CloudWatch Synthetics canaries are managed through the Synthetics client to create browser-based and API endpoint uptime monitors with configurable check intervals. Alert notifications flow through SNS topics with subscription filters for routing to email, SMS, Slack via AWS Chatbot, or Lambda functions for custom remediation. The detector supports cross-account metric aggregation using CloudWatch cross-account observability features for centralized monitoring dashboards."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Anomaly Detector

The AWS CloudWatch Anomaly Detector uses the boto3 CloudWatch client to configure intelligent anomaly detection across your AWS infrastructure. It calls the PutAnomalyDetector API to create machine-learning-based anomaly detection bands on any CloudWatch metric, automatically learning seasonal patterns and baseline behavior. The agent configures composite alarms that combine anomaly detection with static thresholds using the PutCompositeAlarm API for nuanced alerting logic. CloudWatch Synthetics canaries are managed through the Synthetics client to create browser-based and API endpoint uptime monitors with configurable check intervals. Alert notifications flow through SNS topics with subscription filters for routing to email, SMS, Slack via AWS Chatbot, or Lambda functions for custom remediation. The detector supports cross-account metric aggregation using CloudWatch cross-account observability features for centralized monitoring dashboards.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-cloudwatch-anomaly-detector
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/aws-cloudwatch-anomaly-detector` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-detector/)
