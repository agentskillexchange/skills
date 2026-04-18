---
title: "AWS CloudWatch Insights Agent"
description: "Runs CloudWatch Logs Insights queries via AWS SDK for JavaScript v3. Analyzes Lambda cold starts, API Gateway latency, and ECS container logs. Generates anomaly detection alarms with math expressions."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Monitoring & Alerts"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Insights Agent

The AWS CloudWatch Insights Agent skill connects Claude to Amazon CloudWatch using the AWS SDK for JavaScript v3 (@aws-sdk/client-cloudwatch-logs). It executes CloudWatch Logs Insights queries to analyze log data across AWS services with SQL-like syntax.

The skill constructs Insights queries for common debugging scenarios: Lambda function cold start analysis (filtering by INIT_START and REPORT lines), API Gateway latency percentile calculations, ECS container log correlation across task IDs, and Step Functions execution tracing. It handles query pagination and asynchronous result polling for long-running queries.

Metric analysis uses the CloudWatch GetMetricData API to retrieve timeseries for custom and AWS-managed metrics. The skill supports math expressions for derived metrics (computing error rates from request counts and error counts) and anomaly detection band configuration for intelligent alerting.

Alarm management includes creating, describing, and modifying CloudWatch alarms with composite alarm support for multi-condition alerting. The skill handles cross-account and cross-region queries for organizations with distributed AWS infrastructure. IAM credential resolution follows the standard AWS credential chain (environment variables, shared credentials file, instance profile). Essential for teams running serverless and containerized workloads on AWS.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-cloudwatch-insights-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/aws-cloudwatch-insights-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-insights-agent/)
