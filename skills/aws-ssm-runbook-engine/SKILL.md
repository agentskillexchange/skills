---
title: "AWS Systems Manager Runbook Engine"
description: "Executes automated diagnostics using the AWS Systems Manager Automation API and SSM Documents. Collects system metrics via the CloudWatch GetMetricData API and correlates with AWS Health events."
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

# AWS Systems Manager Runbook Engine

The AWS Systems Manager Runbook Engine skill automates operational diagnostics and remediation on AWS infrastructure. It creates and executes SSM Automation documents that define multi-step runbooks with conditional branching, approval gates, and error handling. The skill uses the AWS Systems Manager Automation API to trigger runbooks against individual instances or entire fleets using rate-controlled execution. Diagnostic data is collected through the CloudWatch GetMetricData API, pulling CPU utilization, disk I/O, network throughput, and custom application metrics for correlation analysis. AWS Health events are monitored to provide context during incidents, linking infrastructure changes to observed symptoms. The skill supports Run Command for ad-hoc diagnostics across instance fleets, Session Manager for interactive troubleshooting without SSH, Parameter Store integration for runbook configuration, and OpsCenter OpsItem creation for tracking operational issues. It generates comprehensive diagnostic reports combining CloudWatch metrics, SSM inventory data, and Config compliance status.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-ssm-runbook-engine/)
