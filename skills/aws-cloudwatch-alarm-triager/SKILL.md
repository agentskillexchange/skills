---
title: "AWS CloudWatch Alarm Triager"
description: "Triages AWS CloudWatch alarms by correlating alarm state changes with CloudTrail events and EC2 instance health using boto3. Classifies alarms by severity, identifies root cause candidates, and updates OpsGenie alerts."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Alarm Triager

Triages AWS CloudWatch alarms by correlating alarm state changes with CloudTrail events and EC2 instance health using boto3. Classifies alarms by severity, identifies root cause candidates, and updates OpsGenie alerts.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triager/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-cloudwatch-alarm-triager
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/aws-cloudwatch-alarm-triager`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triager/)
