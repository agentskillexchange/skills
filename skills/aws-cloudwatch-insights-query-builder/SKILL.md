---
title: "AWS CloudWatch Insights Query Builder"
description: "The AWS CloudWatch Insights Query Builder constructs optimized CloudWatch Logs Insights queries for log analysis using the @aws-sdk/client-cloudwatch-logs SDK for query execution and result pagination. It generates CloudWatch Logs Insights query syntax with proper parse, filter, stats, and sort commands for structured log analysis across multiple log groups. The skill creates CloudWatch metric alarms using @aws-sdk/client-cloudwatch with proper evaluation periods, datapoints-to-alarm thresholds, and composite alarm configurations for multi-signal alerting. It supports CloudWatch Metrics Insights queries (metrics SQL) for cross-account and cross-region metric aggregation using the CloudWatch cross-account observability features. The builder generates CloudWatch dashboards with automated widget layouts combining metric graphs, log insights widgets, and alarm status widgets. It integrates with AWS SNS for alarm notification routing and supports CloudWatch Anomaly Detection for dynamic threshold alerting. The tool also configures metric filters for extracting custom metrics from log events with proper filter pattern syntax and metric transformation specifications."
source: "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Codex"
  - "Multi-Framework"
---

# AWS CloudWatch Insights Query Builder

The AWS CloudWatch Insights Query Builder constructs optimized CloudWatch Logs Insights queries for log analysis using the @aws-sdk/client-cloudwatch-logs SDK for query execution and result pagination. It generates CloudWatch Logs Insights query syntax with proper parse, filter, stats, and sort commands for structured log analysis across multiple log groups. The skill creates CloudWatch metric alarms using @aws-sdk/client-cloudwatch with proper evaluation periods, datapoints-to-alarm thresholds, and composite alarm configurations for multi-signal alerting. It supports CloudWatch Metrics Insights queries (metrics SQL) for cross-account and cross-region metric aggregation using the CloudWatch cross-account observability features. The builder generates CloudWatch dashboards with automated widget layouts combining metric graphs, log insights widgets, and alarm status widgets. It integrates with AWS SNS for alarm notification routing and supports CloudWatch Anomaly Detection for dynamic threshold alerting. The tool also configures metric filters for extracting custom metrics from log events with proper filter pattern syntax and metric transformation specifications.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-insights-query-builder/)
