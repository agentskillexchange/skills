---
title: "AWS Systems Manager Runbook Engine"
description: "Executes automated diagnostics using the AWS Systems Manager Automation API and SSM Documents. Collects system metrics via the CloudWatch GetMetricData API and correlates with AWS Health events."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks & Diagnostics"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
  license: "Apache-2.0"
---

# AWS Systems Manager Runbook Engine

The AWS Systems Manager Runbook Engine skill automates operational diagnostics and remediation on AWS infrastructure. It creates and executes SSM Automation documents that define multi-step runbooks with conditional branching, approval gates, and error handling. The skill uses the AWS Systems Manager Automation API to trigger runbooks against individual instances or entire fleets using rate-controlled execution. Diagnostic data is collected through the CloudWatch GetMetricData API, pulling CPU utilization, disk I/O, network throughput, and custom application metrics for correlation analysis. AWS Health events are monitored to provide context during incidents, linking infrastructure changes to observed symptoms. The skill supports Run Command for ad-hoc diagnostics across instance fleets, Session Manager for interactive troubleshooting without SSH, Parameter Store integration for runbook configuration, and OpsCenter OpsItem creation for tracking operational issues. It generates comprehensive diagnostic reports combining CloudWatch metrics, SSM inventory data, and Config compliance status.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-ssm-runbook-engine
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/aws-ssm-runbook-engine` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-ssm-runbook-engine/)
