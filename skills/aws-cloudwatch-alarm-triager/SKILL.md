---
name: "AWS CloudWatch Alarm Triager"
description: "Triages AWS CloudWatch alarms by correlating alarm state changes with CloudTrail events and EC2 instance health using boto3. Classifies alarms by severity, identifies root cause candidates, and updates OpsGenie alerts."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triager/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "aws"  # from ase_tool_match
  github_stars: 3594  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws/aws-sdk-js-v3"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# AWS CloudWatch Alarm Triager

Triages AWS CloudWatch alarms by correlating alarm state changes with CloudTrail events and EC2 instance health using boto3. Classifies alarms by severity, identifies root cause candidates, and updates OpsGenie alerts.

## Overview

The AWS CloudWatch Alarm Triager skill automates the initial triage of CloudWatch alarms by performing multi-signal correlation. When an alarm transitions to ALARM state, the skill uses boto3 to fetch the alarm configuration, metric data points, and evaluation period details. It then queries CloudTrail for recent API calls that may have triggered the condition — deployment events, configuration changes, scaling actions, or security group modifications. For EC2-related alarms, it checks instance status checks, system status checks, and scheduled events via the EC2 DescribeInstanceStatus API. The skill classifies alarms into severity tiers based on impact scope and blast radius analysis. For each alarm, it generates a triage summary with probable root cause, affected resources, and recommended investigation steps. Updates OpsGenie alerts with enriched context via the OpsGenie REST API. Supports alarm suppression during maintenance windows defined in SSM Parameter Store.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudwatch-alarm-triager -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudwatch-alarm-triager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triager/
