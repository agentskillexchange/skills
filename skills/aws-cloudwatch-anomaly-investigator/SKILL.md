---
name: "AWS CloudWatch Anomaly Investigator"
description: "Investigates CloudWatch metric anomalies using the AWS SDK CloudWatch.getMetricData and Logs.filterLogEvents APIs. Correlates metric spikes with log patterns and deployment events from CodeDeploy."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-investigator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "aws"  # from ase_tool_match
  github_stars: 3594  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws/aws-sdk-js-v3"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# AWS CloudWatch Anomaly Investigator

Investigates CloudWatch metric anomalies using the AWS SDK CloudWatch.getMetricData and Logs.filterLogEvents APIs. Correlates metric spikes with log patterns and deployment events from CodeDeploy.

## Overview

The AWS CloudWatch Anomaly Investigator skill automates incident investigation by correlating CloudWatch metric anomalies with log entries and deployment events. It uses the AWS SDK v3 CloudWatch.getMetricData API to pull metric timeseries with anomaly band data from CloudWatch Anomaly Detection.

When a metric breaches its anomaly band, the skill queries CloudWatch Logs using the filterLogEvents API with time-bounded queries centered on the anomaly window. It applies pattern detection using CloudWatch Logs Insights query syntax to identify error rate spikes, latency percentile shifts, and exception frequency changes.

Deployment correlation checks AWS CodeDeploy via the listDeployments and getDeployment APIs to find deployments that occurred within the anomaly time window. The skill also queries AWS X-Ray using the getTraceSummaries API to identify service map changes and latency contributors. Output includes a timeline view showing metric behavior, correlated log patterns, and deployment events, along with confidence-scored root cause hypotheses and suggested CloudWatch Alarms configurations to catch similar issues proactively.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-investigator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-investigator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-investigator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-anomaly-investigator -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-anomaly-investigator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-cloudwatch-anomaly-investigator/
