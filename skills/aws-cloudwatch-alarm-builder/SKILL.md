---
title: "AWS CloudWatch Alarm Builder"
description: "Creates and manages CloudWatch alarms using the AWS SDK for JavaScript v3 (@aws-sdk/client-cloudwatch). Configures metric math expressions, composite alarms, and SNS notification routing via @aws-sdk/client-sns."
slug: "aws-cloudwatch-alarm-builder"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-builder/"
---

# AWS CloudWatch Alarm Builder

Creates and manages CloudWatch alarms using the AWS SDK for JavaScript v3 (@aws-sdk/client-cloudwatch). Configures metric math expressions, composite alarms, and SNS notification routing via @aws-sdk/client-sns.

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
clawhub install aws-cloudwatch-alarm-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The AWS CloudWatch Alarm Builder skill automates the creation of comprehensive monitoring alarm sets for AWS infrastructure. It uses the AWS SDK for JavaScript v3, specifically the @aws-sdk/client-cloudwatch PutMetricAlarm and PutCompositeAlarm commands, to define alarms with proper threshold configurations, evaluation periods, and missing data treatment.
This skill generates metric math expressions for complex monitoring scenarios like calculating error rates as a percentage of total requests, or combining p99 latency with request count for anomaly detection. It supports both static threshold and anomaly detection band configurations using the CloudWatch anomaly detection model.
Notification routing is handled through @aws-sdk/client-sns integration, creating topic subscriptions for email, SMS, Lambda, and PagerDuty endpoints. The skill generates composite alarms that aggregate multiple metric alarms with AND/OR logic to reduce alert fatigue while maintaining coverage.
Pre-built alarm templates cover common AWS services including EC2 (CPU, status checks, disk), RDS (connections, replica lag, storage), ALB (5xx rates, target response time), Lambda (errors, throttles, duration), and ECS (service CPU/memory utilization).

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-builder/)
