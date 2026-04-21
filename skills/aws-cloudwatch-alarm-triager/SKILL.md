---
title: "AWS CloudWatch Alarm Triager"
description: "Triages AWS CloudWatch alarms by correlating alarm state changes with CloudTrail events and EC2 instance health using boto3. Classifies alarms by severity, identifies root cause candidates, and updates OpsGenie alerts."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
  license: "Apache-2.0"
---

# AWS CloudWatch Alarm Triager

Triages AWS CloudWatch alarms by correlating alarm state changes with CloudTrail events and EC2 instance health using boto3. Classifies alarms by severity, identifies root cause candidates, and updates OpsGenie alerts.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-cloudwatch-alarm-triager
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/aws-cloudwatch-alarm-triager` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-triager/)
