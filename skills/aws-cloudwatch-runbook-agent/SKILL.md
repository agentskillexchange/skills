---
title: "AWS CloudWatch Runbook Agent"
description: "The AWS CloudWatch Runbook Agent automates operational incident response by orchestrating AWS SDK calls across CloudWatch services. It uses CloudWatchClient.GetMetricData to pull time-series metrics for CPU utilization, network throughput, error rates, and custom application metrics, correlating anomalies across multiple dimensions. For log analysis, it constructs CloudWatch Logs Insights queries using the StartQuery API, enabling pattern detection across log groups with fields, filter, stats, and parse commands. The agent monitors alarm states via DescribeAlarms and traces alarm state transitions to identify cascading failures. For distributed applications, it integrates with AWS X-Ray by querying GetTraceSummaries and BatchGetTraces to map request flows and identify latency bottlenecks or error-producing service segments. Runbooks are defined as Step Functions-compatible state machines, enabling automated remediation like scaling EC2 Auto Scaling groups via UpdateAutoScalingGroup or flushing ElastiCache clusters. Each runbook execution is logged to CloudWatch with correlation IDs for audit trailing."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Runbook Agent

The AWS CloudWatch Runbook Agent automates operational incident response by orchestrating AWS SDK calls across CloudWatch services. It uses CloudWatchClient.GetMetricData to pull time-series metrics for CPU utilization, network throughput, error rates, and custom application metrics, correlating anomalies across multiple dimensions. For log analysis, it constructs CloudWatch Logs Insights queries using the StartQuery API, enabling pattern detection across log groups with fields, filter, stats, and parse commands. The agent monitors alarm states via DescribeAlarms and traces alarm state transitions to identify cascading failures. For distributed applications, it integrates with AWS X-Ray by querying GetTraceSummaries and BatchGetTraces to map request flows and identify latency bottlenecks or error-producing service segments. Runbooks are defined as Step Functions-compatible state machines, enabling automated remediation like scaling EC2 Auto Scaling groups via UpdateAutoScalingGroup or flushing ElastiCache clusters. Each runbook execution is logged to CloudWatch with correlation IDs for audit trailing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-cloudwatch-runbook-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/aws-cloudwatch-runbook-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-runbook-agent/)
