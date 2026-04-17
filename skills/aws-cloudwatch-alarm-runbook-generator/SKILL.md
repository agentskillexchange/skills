---
name: AWS CloudWatch Alarm Runbook Generator
description: Generates structured incident runbooks from AWS CloudWatch alarm configurations
  using the CloudWatch DescribeAlarms API and AWS Systems Manager documents. Links
  alarms to remediation procedures automatically.
category: Runbooks & Diagnostics
framework: Claude Agents
verification: security_reviewed
source: https://github.com/aws/aws-sdk-js-v3
tool_ecosystem:
  github_repo: aws/aws-sdk-js-v3
  github_stars: 3607
  tool: aws-sdk-js-v3
  license: Apache-2.0
  maintained: true
---
# AWS CloudWatch Alarm Runbook Generator
Generates structured incident runbooks from AWS CloudWatch alarm configurations using the CloudWatch DescribeAlarms API and AWS Systems Manager documents. Links alarms to remediation procedures automatically.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-cloudwatch-alarm-runbook-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/aws-cloudwatch-alarm-runbook-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-alarm-runbook-generator/)
