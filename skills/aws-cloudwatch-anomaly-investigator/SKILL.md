---
title: "AWS CloudWatch Anomaly Investigator"
description: "The AWS CloudWatch Anomaly Investigator skill automates incident investigation by correlating CloudWatch metric anomalies with log entries and deployment events. It uses the AWS SDK v3 CloudWatch.getMetricData API to pull metric timeseries with anomaly band data from CloudWatch Anomaly Detection.\nWhen a metric breaches its anomaly band, the skill queries CloudWatch Logs using the filterLogEvents API with time-bounded queries centered on the anomaly window. It applies pattern detection using CloudWatch Logs Insights query syntax to identify error rate spikes, latency percentile shifts, and exception frequency changes.\nDeployment correlation checks AWS CodeDeploy via the listDeployments and getDeployment APIs to find deployments that occurred within the anomaly time window. The skill also queries AWS X-Ray using the getTraceSummaries API to identify service map changes and latency contributors. Output includes a timeline view showing metric behavior, correlated log patterns, and deployment events, along with confidence-scored root cause hypotheses and suggested CloudWatch Alarms configurations to catch similar issues proactively."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Anomaly Investigator

The AWS CloudWatch Anomaly Investigator skill automates incident investigation by correlating CloudWatch metric anomalies with log entries and deployment events. It uses the AWS SDK v3 CloudWatch.getMetricData API to pull metric timeseries with anomaly band data from CloudWatch Anomaly Detection.
When a metric breaches its anomaly band, the skill queries CloudWatch Logs using the filterLogEvents API with time-bounded queries centered on the anomaly window. It applies pattern detection using CloudWatch Logs Insights query syntax to identify error rate spikes, latency percentile shifts, and exception frequency changes.
Deployment correlation checks AWS CodeDeploy via the listDeployments and getDeployment APIs to find deployments that occurred within the anomaly time window. The skill also queries AWS X-Ray using the getTraceSummaries API to identify service map changes and latency contributors. Output includes a timeline view showing metric behavior, correlated log patterns, and deployment events, along with confidence-scored root cause hypotheses and suggested CloudWatch Alarms configurations to catch similar issues proactively.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-cloudwatch-anomaly-investigator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/aws-cloudwatch-anomaly-investigator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-investigator/)
