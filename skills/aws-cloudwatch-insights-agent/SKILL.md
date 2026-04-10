---
title: "AWS CloudWatch Insights Agent"
description: "Runs CloudWatch Logs Insights queries via AWS SDK for JavaScript v3. Analyzes Lambda cold starts, API Gateway latency, and ECS container logs. Generates anomaly detection alarms with math expressions."
slug: "aws-cloudwatch-insights-agent"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-cloudwatch-insights-agent/"
---

# AWS CloudWatch Insights Agent

Runs CloudWatch Logs Insights queries via AWS SDK for JavaScript v3. Analyzes Lambda cold starts, API Gateway latency, and ECS container logs. Generates anomaly detection alarms with math expressions.

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
clawhub install aws-cloudwatch-insights-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The AWS CloudWatch Insights Agent skill connects Claude to Amazon CloudWatch using the AWS SDK for JavaScript v3 (@aws-sdk/client-cloudwatch-logs). It executes CloudWatch Logs Insights queries to analyze log data across AWS services with SQL-like syntax.
The skill constructs Insights queries for common debugging scenarios: Lambda function cold start analysis (filtering by INIT_START and REPORT lines), API Gateway latency percentile calculations, ECS container log correlation across task IDs, and Step Functions execution tracing. It handles query pagination and asynchronous result polling for long-running queries.
Metric analysis uses the CloudWatch GetMetricData API to retrieve timeseries for custom and AWS-managed metrics. The skill supports math expressions for derived metrics (computing error rates from request counts and error counts) and anomaly detection band configuration for intelligent alerting.
Alarm management includes creating, describing, and modifying CloudWatch alarms with composite alarm support for multi-condition alerting. The skill handles cross-account and cross-region queries for organizations with distributed AWS infrastructure. IAM credential resolution follows the standard AWS credential chain (environment variables, shared credentials file, instance profile). Essential for teams running serverless and containerized workloads on AWS.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-insights-agent/)
