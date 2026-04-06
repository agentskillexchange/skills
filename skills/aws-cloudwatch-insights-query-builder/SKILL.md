---
name: "AWS CloudWatch Insights Query Builder"
description: "Builds CloudWatch Logs Insights queries and metric alarms using AWS SDK v3 (@aws-sdk/client-cloudwatch-logs, @aws-sdk/client-cloudwatch). Generates cross-account observability dashboards with CloudWatch Metrics Insights."
category: "Monitoring &amp; Alerts"
framework: "Codex, Multi-Framework"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-cloudwatch-insights-query-builder/"
---
# AWS CloudWatch Insights Query Builder

Builds CloudWatch Logs Insights queries and metric alarms using AWS SDK v3 (@aws-sdk/client-cloudwatch-logs, @aws-sdk/client-cloudwatch). Generates cross-account observability dashboards with CloudWatch Metrics Insights.

The AWS CloudWatch Insights Query Builder constructs optimized CloudWatch Logs Insights queries for log analysis using the @aws-sdk/client-cloudwatch-logs SDK for query execution and result pagination. It generates CloudWatch Logs Insights query syntax with proper parse, filter, stats, and sort commands for structured log analysis across multiple log groups. The skill creates CloudWatch metric alarms using @aws-sdk/client-cloudwatch with proper evaluation periods, datapoints-to-alarm thresholds, and composite alarm configurations for multi-signal alerting. It supports CloudWatch Metrics Insights queries (metrics SQL) for cross-account and cross-region metric aggregation using the CloudWatch cross-account observability features. The builder generates CloudWatch dashboards with automated widget layouts combining metric graphs, log insights widgets, and alarm status widgets. It integrates with AWS SNS for alarm notification routing and supports CloudWatch Anomaly Detection for dynamic threshold alerting. The tool also configures metric filters for extracting custom metrics from log events with proper filter pattern syntax and metric transformation specifications.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-insights-query-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-insights-query-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-insights-query-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-insights-query-builder -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-insights-query-builder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-insights-query-builder/)
