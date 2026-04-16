---
title: "AWS CloudWatch Runbook Agent"
description: "Uses AWS SDK CloudWatchClient GetMetricData and CloudWatch Logs Insights StartQueryExecution to automate incident triage. Correlates alarms via DescribeAlarms with X-Ray trace segments for root cause analysis."
verification: "security_reviewed"
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks & Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
  license: "Apache-2.0"
---

# AWS CloudWatch Runbook Agent

The AWS CloudWatch Runbook Agent automates operational incident response by orchestrating AWS SDK calls across CloudWatch services. It uses CloudWatchClient.GetMetricData to pull time-series metrics for CPU utilization, network throughput, error rates, and custom application metrics, correlating anomalies across multiple dimensions. For log analysis, it constructs CloudWatch Logs Insights queries using the StartQuery API, enabling pattern detection across log groups with fields, filter, stats, and parse commands. The agent monitors alarm states via DescribeAlarms and traces alarm state transitions to identify cascading failures. For distributed applications, it integrates with AWS X-Ray by querying GetTraceSummaries and BatchGetTraces to map request flows and identify latency bottlenecks or error-producing service segments. Runbooks are defined as Step Functions-compatible state machines, enabling automated remediation like scaling EC2 Auto Scaling groups via UpdateAutoScalingGroup or flushing ElastiCache clusters. Each runbook execution is logged to CloudWatch with correlation IDs for audit trailing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-runbook-agent/)
