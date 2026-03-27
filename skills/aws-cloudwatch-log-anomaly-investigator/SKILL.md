---
name: "AWS CloudWatch Log Anomaly Investigator"
description: "Investigates anomalous patterns in AWS CloudWatch Logs using the CloudWatch Logs Insights API and CloudWatch Anomaly Detection. Correlates log spikes with deployment events via AWS CodeDeploy API."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-cloudwatch-log-anomaly-investigator/"
tool_ecosystem:
  tool: aws
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: aws/aws-sdk-js-v3
  license: Apache-2.0
  maintained: true
---

# AWS CloudWatch Log Anomaly Investigator

Investigates anomalous patterns in AWS CloudWatch Logs using the CloudWatch Logs Insights API and CloudWatch Anomaly Detection. Correlates log spikes with deployment events via AWS CodeDeploy API.

## Overview

The AWS CloudWatch Log Anomaly Investigator skill automates root cause analysis for production incidents detected in AWS CloudWatch Logs. It uses the CloudWatch Logs Insights API to run targeted queries across log groups, identifying error rate spikes, latency outliers, and unusual log patterns.

Leveraging CloudWatch Anomaly Detection, the skill establishes baseline metrics and alerts when log volumes or error rates deviate significantly from expected patterns. It automatically correlates anomalies with recent deployment events by querying the AWS CodeDeploy API for deployment timelines.

The investigation workflow includes automatic extraction of stack traces, error codes, and request IDs from structured JSON logs. Using the AWS X-Ray API, the skill traces individual requests across microservices to pinpoint the failing component.

Results are compiled into a structured incident report with timeline, probable root cause, affected services, and recommended remediation steps. The skill supports integration with PagerDuty and Opsgenie via their REST APIs for automated incident escalation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-log-anomaly-investigator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-log-anomaly-investigator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-log-anomaly-investigator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-log-anomaly-investigator -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-log-anomaly-investigator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-cloudwatch-log-anomaly-investigator/
