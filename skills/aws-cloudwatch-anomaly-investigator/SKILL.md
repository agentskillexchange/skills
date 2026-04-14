---
title: "AWS CloudWatch Anomaly Investigator"
description: "Investigates CloudWatch metric anomalies using the AWS SDK CloudWatch.getMetricData and Logs.filterLogEvents APIs. Correlates metric spikes with log patterns and deployment events from CodeDeploy."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks &amp; Diagnostics"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-investigator/)
