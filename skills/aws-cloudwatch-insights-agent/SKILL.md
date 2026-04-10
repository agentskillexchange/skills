---
name: AWS CloudWatch Insights Agent
description: Runs CloudWatch Logs Insights queries via AWS SDK for JavaScript v3.
  Analyzes Lambda cold starts, API Gateway latency, and ECS container logs. Generates
  anomaly detection alarms with math expressions.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudwatch-insights-agent/
category:
- Monitoring &amp; Alerts
framework:
- ChatGPT Agents
---
# AWS CloudWatch Insights Agent

The AWS CloudWatch Insights Agent skill connects Claude to Amazon CloudWatch using the AWS SDK for JavaScript v3 (@aws-sdk/client-cloudwatch-logs). It executes CloudWatch Logs Insights queries to analyze log data across AWS services with SQL-like syntax.
The skill constructs Insights queries for common debugging scenarios: Lambda function cold start analysis (filtering by INIT_START and REPORT lines), API Gateway latency percentile calculations, ECS container log correlation across task IDs, and Step Functions execution tracing. It handles query pagination and asynchronous result polling for long-running queries.
Metric analysis uses the CloudWatch GetMetricData API to retrieve timeseries for custom and AWS-managed metrics. The skill supports math expressions for derived metrics (computing error rates from request counts and error counts) and anomaly detection band configuration for intelligent alerting.
Alarm management includes creating, describing, and modifying CloudWatch alarms with composite alarm support for multi-condition alerting. The skill handles cross-account and cross-region queries for organizations with distributed AWS infrastructure. IAM credential resolution follows the standard AWS credential chain (environment variables, shared credentials file, instance profile). Essential for teams running serverless and containerized workloads on AWS.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-insights-agent/)
