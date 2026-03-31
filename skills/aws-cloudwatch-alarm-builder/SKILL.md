---
name: "AWS CloudWatch Alarm Builder"
description: "Creates and manages CloudWatch alarms using the AWS SDK for JavaScript v3 (@aws-sdk/client-cloudwatch). Configures metric math expressions, composite alarms, and SNS notification routing via @aws-sdk/client-sns."
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-builder/"
---
# AWS CloudWatch Alarm Builder

Creates and manages CloudWatch alarms using the AWS SDK for JavaScript v3 (@aws-sdk/client-cloudwatch). Configures metric math expressions, composite alarms, and SNS notification routing via @aws-sdk/client-sns.

## Overview

The AWS CloudWatch Alarm Builder skill automates the creation of comprehensive monitoring alarm sets for AWS infrastructure. It uses the AWS SDK for JavaScript v3, specifically the @aws-sdk/client-cloudwatch PutMetricAlarm and PutCompositeAlarm commands, to define alarms with proper threshold configurations, evaluation periods, and missing data treatment.

This skill generates metric math expressions for complex monitoring scenarios like calculating error rates as a percentage of total requests, or combining p99 latency with request count for anomaly detection. It supports both static threshold and anomaly detection band configurations using the CloudWatch anomaly detection model.

Notification routing is handled through @aws-sdk/client-sns integration, creating topic subscriptions for email, SMS, Lambda, and PagerDuty endpoints. The skill generates composite alarms that aggregate multiple metric alarms with AND/OR logic to reduce alert fatigue while maintaining coverage.

Pre-built alarm templates cover common AWS services including EC2 (CPU, status checks, disk), RDS (connections, replica lag, storage), ALB (5xx rates, target response time), Lambda (errors, throttles, duration), and ECS (service CPU/memory utilization).

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-builder -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-alarm-builder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-builder/)
