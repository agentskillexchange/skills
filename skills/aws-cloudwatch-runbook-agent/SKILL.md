---
title: AWS CloudWatch Runbook Agent
description: The AWS CloudWatch Runbook Agent automates operational incident response
  by orchestrating AWS SDK calls across CloudWatch services. It uses CloudWatchClient.GetMetricData
  to pull time-series metrics for CPU utilization, network throughput, error rates,
  and custom application metrics, correlating anomalies across multiple dimensions.
  For log analysis, it constructs CloudWatch Logs Insights queries using the StartQuery
  API, enabling pattern detection across log groups with fields, filter, stats, and
  parse commands. The agent monitors alarm states via DescribeAlarms and traces alarm
  state transitions to identify cascading failures. For distributed applications,
  it integrates with AWS X-Ray by querying GetTraceSummaries and BatchGetTraces to
  map request flows and identify latency bottlenecks or error-producing service segments.
  Runbooks are defined as Step Functions-compatible state machines, enabling automated
  remediation like scaling EC2 Auto Scaling groups via UpdateAutoScalingGroup or flushing
  ElastiCache clusters. Each runbook execution is logged to CloudWatch with correlation
  IDs for audit trailing.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudwatch-runbook-agent/
category:
- Runbooks &amp; Diagnostics
framework:
- ChatGPT Agents
---

# AWS CloudWatch Runbook Agent

The AWS CloudWatch Runbook Agent automates operational incident response by orchestrating AWS SDK calls across CloudWatch services. It uses CloudWatchClient.GetMetricData to pull time-series metrics for CPU utilization, network throughput, error rates, and custom application metrics, correlating anomalies across multiple dimensions. For log analysis, it constructs CloudWatch Logs Insights queries using the StartQuery API, enabling pattern detection across log groups with fields, filter, stats, and parse commands. The agent monitors alarm states via DescribeAlarms and traces alarm state transitions to identify cascading failures. For distributed applications, it integrates with AWS X-Ray by querying GetTraceSummaries and BatchGetTraces to map request flows and identify latency bottlenecks or error-producing service segments. Runbooks are defined as Step Functions-compatible state machines, enabling automated remediation like scaling EC2 Auto Scaling groups via UpdateAutoScalingGroup or flushing ElastiCache clusters. Each runbook execution is logged to CloudWatch with correlation IDs for audit trailing.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-runbook-agent/)
