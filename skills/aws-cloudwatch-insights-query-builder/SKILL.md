---
title: AWS CloudWatch Insights Query Builder
description: The AWS CloudWatch Insights Query Builder constructs optimized CloudWatch
  Logs Insights queries for log analysis using the @aws-sdk/client-cloudwatch-logs
  SDK for query execution and result pagination. It generates CloudWatch Logs Insights
  query syntax with proper parse, filter, stats, and sort commands for structured
  log analysis across multiple log groups. The skill creates CloudWatch metric alarms
  using @aws-sdk/client-cloudwatch with proper evaluation periods, datapoints-to-alarm
  thresholds, and composite alarm configurations for multi-signal alerting. It supports
  CloudWatch Metrics Insights queries (metrics SQL) for cross-account and cross-region
  metric aggregation using the CloudWatch cross-account observability features. The
  builder generates CloudWatch dashboards with automated widget layouts combining
  metric graphs, log insights widgets, and alarm status widgets. It integrates with
  AWS SNS for alarm notification routing and supports CloudWatch Anomaly Detection
  for dynamic threshold alerting. The tool also configures metric filters for extracting
  custom metrics from log events with proper filter pattern syntax and metric transformation
  specifications.
verification: security_reviewed
source: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html
category:
- Monitoring &amp; Alerts
framework:
- Codex
- Multi-Framework
---

# AWS CloudWatch Insights Query Builder

The AWS CloudWatch Insights Query Builder constructs optimized CloudWatch Logs Insights queries for log analysis using the @aws-sdk/client-cloudwatch-logs SDK for query execution and result pagination. It generates CloudWatch Logs Insights query syntax with proper parse, filter, stats, and sort commands for structured log analysis across multiple log groups. The skill creates CloudWatch metric alarms using @aws-sdk/client-cloudwatch with proper evaluation periods, datapoints-to-alarm thresholds, and composite alarm configurations for multi-signal alerting. It supports CloudWatch Metrics Insights queries (metrics SQL) for cross-account and cross-region metric aggregation using the CloudWatch cross-account observability features. The builder generates CloudWatch dashboards with automated widget layouts combining metric graphs, log insights widgets, and alarm status widgets. It integrates with AWS SNS for alarm notification routing and supports CloudWatch Anomaly Detection for dynamic threshold alerting. The tool also configures metric filters for extracting custom metrics from log events with proper filter pattern syntax and metric transformation specifications.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-insights-query-builder/)
