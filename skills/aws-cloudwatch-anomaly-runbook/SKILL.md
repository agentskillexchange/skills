---
title: AWS CloudWatch Anomaly Runbook
description: 'The AWS CloudWatch Anomaly Runbook skill activates when CloudWatch Anomaly
  Detection identifies metric deviations beyond trained baselines. Using the AWS SDK
  CloudWatch client, it calls GetMetricData to retrieve the anomalous metric series
  alongside its expected band, then DescribeAlarms to gather alarm configuration and
  state transition history. The skill follows structured diagnostic runbooks organized
  by metric namespace: for EC2 it checks CPU, network, and disk metrics correlation;
  for RDS it examines connection counts, replica lag, and freeable memory; for ALB
  it correlates 5xx spikes with target group health. Each runbook step queries additional
  AWS APIs (EC2 DescribeInstances, RDS DescribeDBInstances, ECS DescribeServices)
  to build a complete diagnostic picture. The skill outputs a timeline-ordered investigation
  report with root cause probability scores and specific remediation actions, including
  AWS CLI commands to execute fixes and CloudFormation snippets to prevent recurrence.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---

# AWS CloudWatch Anomaly Runbook

The AWS CloudWatch Anomaly Runbook skill activates when CloudWatch Anomaly Detection identifies metric deviations beyond trained baselines. Using the AWS SDK CloudWatch client, it calls GetMetricData to retrieve the anomalous metric series alongside its expected band, then DescribeAlarms to gather alarm configuration and state transition history. The skill follows structured diagnostic runbooks organized by metric namespace: for EC2 it checks CPU, network, and disk metrics correlation; for RDS it examines connection counts, replica lag, and freeable memory; for ALB it correlates 5xx spikes with target group health. Each runbook step queries additional AWS APIs (EC2 DescribeInstances, RDS DescribeDBInstances, ECS DescribeServices) to build a complete diagnostic picture. The skill outputs a timeline-ordered investigation report with root cause probability scores and specific remediation actions, including AWS CLI commands to execute fixes and CloudFormation snippets to prevent recurrence.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-runbook/)
