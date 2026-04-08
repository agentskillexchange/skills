---
title: AWS CloudWatch Alarm Builder
description: The AWS CloudWatch Alarm Builder skill automates the creation of comprehensive
  monitoring alarm sets for AWS infrastructure. It uses the AWS SDK for JavaScript
  v3, specifically the @aws-sdk/client-cloudwatch PutMetricAlarm and PutCompositeAlarm
  commands, to define alarms with proper threshold configurations, evaluation periods,
  and missing data treatment. This skill generates metric math expressions for complex
  monitoring scenarios like calculating error rates as a percentage of total requests,
  or combining p99 latency with request count for anomaly detection. It supports both
  static threshold and anomaly detection band configurations using the CloudWatch
  anomaly detection model. Notification routing is handled through @aws-sdk/client-sns
  integration, creating topic subscriptions for email, SMS, Lambda, and PagerDuty
  endpoints. The skill generates composite alarms that aggregate multiple metric alarms
  with AND/OR logic to reduce alert fatigue while maintaining coverage. Pre-built
  alarm templates cover common AWS services including EC2 (CPU, status checks, disk),
  RDS (connections, replica lag, storage), ALB (5xx rates, target response time),
  Lambda (errors, throttles, duration), and ECS (service CPU/memory utilization).
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudwatch-alarm-builder/
category:
- CI/CD Integrations
framework:
- ChatGPT Agents
---

# AWS CloudWatch Alarm Builder

The AWS CloudWatch Alarm Builder skill automates the creation of comprehensive monitoring alarm sets for AWS infrastructure. It uses the AWS SDK for JavaScript v3, specifically the @aws-sdk/client-cloudwatch PutMetricAlarm and PutCompositeAlarm commands, to define alarms with proper threshold configurations, evaluation periods, and missing data treatment. This skill generates metric math expressions for complex monitoring scenarios like calculating error rates as a percentage of total requests, or combining p99 latency with request count for anomaly detection. It supports both static threshold and anomaly detection band configurations using the CloudWatch anomaly detection model. Notification routing is handled through @aws-sdk/client-sns integration, creating topic subscriptions for email, SMS, Lambda, and PagerDuty endpoints. The skill generates composite alarms that aggregate multiple metric alarms with AND/OR logic to reduce alert fatigue while maintaining coverage. Pre-built alarm templates cover common AWS services including EC2 (CPU, status checks, disk), RDS (connections, replica lag, storage), ALB (5xx rates, target response time), Lambda (errors, throttles, duration), and ECS (service CPU/memory utilization).

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-builder/)
