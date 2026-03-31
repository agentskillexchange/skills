---
name: "AWS CloudWatch Anomaly Detector"
description: "Uses AWS CloudWatch SDK (boto3) to configure anomaly detection bands on metrics via PutAnomalyDetector API. Integrates with SNS for notifications and CloudWatch Synthetics for canary-based uptime monitoring."
category: "Monitoring & Alerts"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-detector/"
---
# AWS CloudWatch Anomaly Detector

Uses AWS CloudWatch SDK (boto3) to configure anomaly detection bands on metrics via PutAnomalyDetector API. Integrates with SNS for notifications and CloudWatch Synthetics for canary-based uptime monitoring.

## Overview

The AWS CloudWatch Anomaly Detector uses the boto3 CloudWatch client to configure intelligent anomaly detection across your AWS infrastructure. It calls the PutAnomalyDetector API to create machine-learning-based anomaly detection bands on any CloudWatch metric, automatically learning seasonal patterns and baseline behavior. The agent configures composite alarms that combine anomaly detection with static thresholds using the PutCompositeAlarm API for nuanced alerting logic. CloudWatch Synthetics canaries are managed through the Synthetics client to create browser-based and API endpoint uptime monitors with configurable check intervals. Alert notifications flow through SNS topics with subscription filters for routing to email, SMS, Slack via AWS Chatbot, or Lambda functions for custom remediation. The detector supports cross-account metric aggregation using CloudWatch cross-account observability features for centralized monitoring dashboards.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-detector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-detector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-detector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-detector -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-anomaly-detector
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-detector/)
