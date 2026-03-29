---
name: "AWS CloudWatch Insights Agent"
description: "Runs CloudWatch Logs Insights queries via AWS SDK for JavaScript v3. Analyzes Lambda cold starts, API Gateway latency, and ECS container logs. Generates anomaly detection alarms with math expressions."
category: "Monitoring & Alerts"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
tool_ecosystem:
  tool: aws
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: aws/aws-sdk-js-v3
  license: Apache-2.0
  maintained: true
---
# AWS CloudWatch Insights Agent

Runs CloudWatch Logs Insights queries via AWS SDK for JavaScript v3. Analyzes Lambda cold starts, API Gateway latency, and ECS container logs. Generates anomaly detection alarms with math expressions.

## Overview

The AWS CloudWatch Insights Agent skill connects Claude to Amazon CloudWatch using the AWS SDK for JavaScript v3 (@aws-sdk/client-cloudwatch-logs). It executes CloudWatch Logs Insights queries to analyze log data across AWS services with SQL-like syntax.

The skill constructs Insights queries for common debugging scenarios: Lambda function cold start analysis (filtering by INIT_START and REPORT lines), API Gateway latency percentile calculations, ECS container log correlation across task IDs, and Step Functions execution tracing. It handles query pagination and asynchronous result polling for long-running queries.

Metric analysis uses the CloudWatch GetMetricData API to retrieve timeseries for custom and AWS-managed metrics. The skill supports math expressions for derived metrics (computing error rates from request counts and error counts) and anomaly detection band configuration for intelligent alerting.

Alarm management includes creating, describing, and modifying CloudWatch alarms with composite alarm support for multi-condition alerting. The skill handles cross-account and cross-region queries for organizations with distributed AWS infrastructure. IAM credential resolution follows the standard AWS credential chain (environment variables, shared credentials file, instance profile). Essential for teams running serverless and containerized workloads on AWS.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-insights-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-insights-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-insights-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-insights-agent -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-insights-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-insights-agent/)
