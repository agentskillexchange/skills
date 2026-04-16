---
title: "AWS CloudWatch Anomaly Detector"
description: "Uses AWS CloudWatch SDK (boto3) to configure anomaly detection bands on metrics via PutAnomalyDetector API. Integrates with SNS for notifications and CloudWatch Synthetics for canary-based uptime monitoring."
verification: "security_reviewed"
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
  license: "Apache-2.0"
---

# AWS CloudWatch Anomaly Detector

The AWS CloudWatch Anomaly Detector uses the boto3 CloudWatch client to configure intelligent anomaly detection across your AWS infrastructure. It calls the PutAnomalyDetector API to create machine-learning-based anomaly detection bands on any CloudWatch metric, automatically learning seasonal patterns and baseline behavior. The agent configures composite alarms that combine anomaly detection with static thresholds using the PutCompositeAlarm API for nuanced alerting logic. CloudWatch Synthetics canaries are managed through the Synthetics client to create browser-based and API endpoint uptime monitors with configurable check intervals. Alert notifications flow through SNS topics with subscription filters for routing to email, SMS, Slack via AWS Chatbot, or Lambda functions for custom remediation. The detector supports cross-account metric aggregation using CloudWatch cross-account observability features for centralized monitoring dashboards.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-detector/)
