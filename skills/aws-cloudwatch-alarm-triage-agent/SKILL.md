---
name: "AWS CloudWatch Alarm Triage Agent"
description: "Triages AWS CloudWatch alarms using the CloudWatch DescribeAlarms API, GetMetricData for historical analysis, and CloudTrail LookupEvents for root cause correlation. Prioritizes alerts by blast radius and provides remediation playbooks."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
tool_ecosystem:
  tool: aws
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: aws/aws-sdk-js-v3
  license: Apache-2.0
  maintained: true
---

# AWS CloudWatch Alarm Triage Agent

Triages AWS CloudWatch alarms using the CloudWatch DescribeAlarms API, GetMetricData for historical analysis, and CloudTrail LookupEvents for root cause correlation. Prioritizes alerts by blast radius and provides remediation playbooks.

## Overview

The AWS CloudWatch Alarm Triage Agent automates incident response for CloudWatch alarm notifications. It uses the DescribeAlarms API to retrieve alarm configuration details including metric name, namespace, threshold, comparison operator, and evaluation periods, then queries GetMetricData to pull historical metric values for trend analysis.

The agent correlates alarm triggers with infrastructure changes by querying AWS CloudTrail via the LookupEvents API, identifying recent API calls that may have caused the alert (deployments, configuration changes, scaling events). It integrates with AWS Health API to check for ongoing AWS service issues that could explain metric anomalies.

For EC2-related alarms, it queries the DescribeInstances API for instance status checks and DescribeInstanceStatus for system/instance reachability. For RDS alarms, it uses DescribeDBInstances and DescribeEvents to check for maintenance windows, failovers, and storage issues. The agent calculates blast radius by mapping affected resources through AWS Resource Groups Tagging API and service dependency graphs defined in AWS Systems Manager OpsCenter. Remediation playbooks include AWS CLI commands for common fixes like scaling adjustments, security group corrections, and RDS parameter group modifications.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triage-agent -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-alarm-triage-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triage-agent/
