---
name: "AWS CloudWatch Runbook Agent"
description: "Uses AWS SDK CloudWatchClient GetMetricData and CloudWatch Logs Insights StartQueryExecution to automate incident triage. Correlates alarms via DescribeAlarms with X-Ray trace segments for root cause analysis."
category: "Runbooks &amp; Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-cloudwatch-runbook-agent/"
---
# AWS CloudWatch Runbook Agent

Uses AWS SDK CloudWatchClient GetMetricData and CloudWatch Logs Insights StartQueryExecution to automate incident triage. Correlates alarms via DescribeAlarms with X-Ray trace segments for root cause analysis.

The AWS CloudWatch Runbook Agent automates operational incident response by orchestrating AWS SDK calls across CloudWatch services. It uses CloudWatchClient.GetMetricData to pull time-series metrics for CPU utilization, network throughput, error rates, and custom application metrics, correlating anomalies across multiple dimensions. For log analysis, it constructs CloudWatch Logs Insights queries using the StartQuery API, enabling pattern detection across log groups with fields, filter, stats, and parse commands. The agent monitors alarm states via DescribeAlarms and traces alarm state transitions to identify cascading failures. For distributed applications, it integrates with AWS X-Ray by querying GetTraceSummaries and BatchGetTraces to map request flows and identify latency bottlenecks or error-producing service segments. Runbooks are defined as Step Functions-compatible state machines, enabling automated remediation like scaling EC2 Auto Scaling groups via UpdateAutoScalingGroup or flushing ElastiCache clusters. Each runbook execution is logged to CloudWatch with correlation IDs for audit trailing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-runbook-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-runbook-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-runbook-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-runbook-agent -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-runbook-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-runbook-agent/)
