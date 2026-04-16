---
title: "AWS CloudWatch Insights Query Builder"
description: "Builds CloudWatch Logs Insights queries and metric alarms using AWS SDK v3 (@aws-sdk/client-cloudwatch-logs, @aws-sdk/client-cloudwatch). Generates cross-account observability dashboards with CloudWatch Metrics Insights."
verification: "security_reviewed"
source: "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Codex"
  - "Multi-Framework"
---

# AWS CloudWatch Insights Query Builder

The AWS CloudWatch Insights Query Builder constructs optimized CloudWatch Logs Insights queries for log analysis using the @aws-sdk/client-cloudwatch-logs SDK for query execution and result pagination. It generates CloudWatch Logs Insights query syntax with proper parse, filter, stats, and sort commands for structured log analysis across multiple log groups. The skill creates CloudWatch metric alarms using @aws-sdk/client-cloudwatch with proper evaluation periods, datapoints-to-alarm thresholds, and composite alarm configurations for multi-signal alerting. It supports CloudWatch Metrics Insights queries (metrics SQL) for cross-account and cross-region metric aggregation using the CloudWatch cross-account observability features. The builder generates CloudWatch dashboards with automated widget layouts combining metric graphs, log insights widgets, and alarm status widgets. It integrates with AWS SNS for alarm notification routing and supports CloudWatch Anomaly Detection for dynamic threshold alerting. The tool also configures metric filters for extracting custom metrics from log events with proper filter pattern syntax and metric transformation specifications.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-insights-query-builder/)
