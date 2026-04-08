---
title: AWS CloudWatch Anomaly Investigator
description: The AWS CloudWatch Anomaly Investigator skill automates incident investigation
  by correlating CloudWatch metric anomalies with log entries and deployment events.
  It uses the AWS SDK v3 CloudWatch.getMetricData API to pull metric timeseries with
  anomaly band data from CloudWatch Anomaly Detection. When a metric breaches its
  anomaly band, the skill queries CloudWatch Logs using the filterLogEvents API with
  time-bounded queries centered on the anomaly window. It applies pattern detection
  using CloudWatch Logs Insights query syntax to identify error rate spikes, latency
  percentile shifts, and exception frequency changes. Deployment correlation checks
  AWS CodeDeploy via the listDeployments and getDeployment APIs to find deployments
  that occurred within the anomaly time window. The skill also queries AWS X-Ray using
  the getTraceSummaries API to identify service map changes and latency contributors.
  Output includes a timeline view showing metric behavior, correlated log patterns,
  and deployment events, along with confidence-scored root cause hypotheses and suggested
  CloudWatch Alarms configurations to catch similar issues proactively.
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-investigator/
category:
- Runbooks &amp; Diagnostics
framework:
- ChatGPT Agents
---

# AWS CloudWatch Anomaly Investigator

The AWS CloudWatch Anomaly Investigator skill automates incident investigation by correlating CloudWatch metric anomalies with log entries and deployment events. It uses the AWS SDK v3 CloudWatch.getMetricData API to pull metric timeseries with anomaly band data from CloudWatch Anomaly Detection. When a metric breaches its anomaly band, the skill queries CloudWatch Logs using the filterLogEvents API with time-bounded queries centered on the anomaly window. It applies pattern detection using CloudWatch Logs Insights query syntax to identify error rate spikes, latency percentile shifts, and exception frequency changes. Deployment correlation checks AWS CodeDeploy via the listDeployments and getDeployment APIs to find deployments that occurred within the anomaly time window. The skill also queries AWS X-Ray using the getTraceSummaries API to identify service map changes and latency contributors. Output includes a timeline view showing metric behavior, correlated log patterns, and deployment events, along with confidence-scored root cause hypotheses and suggested CloudWatch Alarms configurations to catch similar issues proactively.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-investigator/)
