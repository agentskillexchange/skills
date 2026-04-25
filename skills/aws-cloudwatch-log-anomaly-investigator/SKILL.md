---
title: "AWS CloudWatch Log Anomaly Investigator"
description: "Investigates anomalous patterns in AWS CloudWatch Logs using the CloudWatch Logs Insights API and CloudWatch Anomaly Detection. Correlates log spikes with deployment events via AWS CodeDeploy API."
verification: "security_reviewed"
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks & Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Log Anomaly Investigator

The AWS CloudWatch Log Anomaly Investigator skill automates root cause analysis for production incidents detected in AWS CloudWatch Logs. It uses the CloudWatch Logs Insights API to run targeted queries across log groups, identifying error rate spikes, latency outliers, and unusual log patterns.

Leveraging CloudWatch Anomaly Detection, the skill establishes baseline metrics and alerts when log volumes or error rates deviate significantly from expected patterns. It automatically correlates anomalies with recent deployment events by querying the AWS CodeDeploy API for deployment timelines.

The investigation workflow includes automatic extraction of stack traces, error codes, and request IDs from structured JSON logs. Using the AWS X-Ray API, the skill traces individual requests across microservices to pinpoint the failing component.

Results are compiled into a structured incident report with timeline, probable root cause, affected services, and recommended remediation steps. The skill supports integration with PagerDuty and Opsgenie via their REST APIs for automated incident escalation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/aws-cloudwatch-log-anomaly-investigator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-cloudwatch-log-anomaly-investigator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/aws-cloudwatch-log-anomaly-investigator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-log-anomaly-investigator/)
