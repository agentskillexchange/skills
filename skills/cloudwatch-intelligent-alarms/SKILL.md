---
name: "CloudWatch Intelligent Alarms"
description: "Uses AWS CloudWatch SDK (boto3) to create composite alarms with ML-powered anomaly detection bands. Integrates with AWS SNS for notifications and EventBridge for automated remediation triggers."
category: "Monitoring & Alerts"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cloudwatch-intelligent-alarms/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "aws"  # from ase_tool_match
  github_stars: 3594  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws/aws-sdk-js-v3"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CloudWatch Intelligent Alarms

Uses AWS CloudWatch SDK (boto3) to create composite alarms with ML-powered anomaly detection bands. Integrates with AWS SNS for notifications and EventBridge for automated remediation triggers.

## Overview

The CloudWatch Intelligent Alarms skill enables AI agents to deploy sophisticated monitoring strategies on AWS infrastructure using the boto3 CloudWatch client. It creates and manages metric alarms, composite alarms, and anomaly detection bands through the put_metric_alarm and put_composite_alarm API calls.

The skill leverages CloudWatch Anomaly Detection models via the put_anomaly_detector API, training on two weeks of historical metric data to establish dynamic baselines that account for daily and weekly seasonality. Composite alarms combine multiple signals (CPU, memory, network, application metrics) into service-level health indicators using Boolean algebra expressions.

Alert routing is configured through AWS SNS (Simple Notification Service) topics with subscription filters targeting specific engineering teams based on AWS resource tags. For automated remediation, the skill creates EventBridge rules that trigger Step Functions state machines or Lambda functions. Integration with AWS Systems Manager Incident Manager creates structured incidents with runbook associations. The skill also configures CloudWatch Dashboards via the put_dashboard API, generating CloudFormation-compatible widget JSON for infrastructure-as-code workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cloudwatch-intelligent-alarms
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cloudwatch-intelligent-alarms -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cloudwatch-intelligent-alarms -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cloudwatch-intelligent-alarms -a codex
```

### OpenClaw

```bash
clawhub install cloudwatch-intelligent-alarms
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cloudwatch-intelligent-alarms/
