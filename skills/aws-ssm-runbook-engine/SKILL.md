---
name: "AWS Systems Manager Runbook Engine"
description: "Executes automated diagnostics using the AWS Systems Manager Automation API and SSM Documents. Collects system metrics via the CloudWatch GetMetricData API and correlates with AWS Health events."
category: "Runbooks &amp; Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-ssm-runbook-engine/"
---
# AWS Systems Manager Runbook Engine

Executes automated diagnostics using the AWS Systems Manager Automation API and SSM Documents. Collects system metrics via the CloudWatch GetMetricData API and correlates with AWS Health events.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-ssm-runbook-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-ssm-runbook-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-ssm-runbook-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-ssm-runbook-engine -a codex
```

### OpenClaw

```bash
clawhub install aws-ssm-runbook-engine
```

## Details

The AWS Systems Manager Runbook Engine skill automates operational diagnostics and remediation on AWS infrastructure. It creates and executes SSM Automation documents that define multi-step runbooks with conditional branching, approval gates, and error handling. The skill uses the AWS Systems Manager Automation API to trigger runbooks against individual instances or entire fleets using rate-controlled execution. Diagnostic data is collected through the CloudWatch GetMetricData API, pulling CPU utilization, disk I/O, network throughput, and custom application metrics for correlation analysis. AWS Health events are monitored to provide context during incidents, linking infrastructure changes to observed symptoms. The skill supports Run Command for ad-hoc diagnostics across instance fleets, Session Manager for interactive troubleshooting without SSH, Parameter Store integration for runbook configuration, and OpsCenter OpsItem creation for tracking operational issues. It generates comprehensive diagnostic reports combining CloudWatch metrics, SSM inventory data, and Config compliance status.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-ssm-runbook-engine/)
