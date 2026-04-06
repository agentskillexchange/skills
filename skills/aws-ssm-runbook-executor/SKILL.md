---
name: AWS Systems Manager Runbook
description: Execute AWS Systems Manager Automation runbooks and Run Command documents
  using the SSM API and boto3. Supports cross-account execution, rate controls, and
  parameter store integration.
category: "Runbooks &amp; Diagnostics"
framework: Claude Agents
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-ssm-runbook-executor/"
---
# AWS Systems Manager Runbook

Execute AWS Systems Manager Automation runbooks and Run Command documents using the SSM API and boto3. Supports cross-account execution, rate controls, and parameter store integration.

The AWS Systems Manager Runbook Executor skill automates operational procedures through AWS SSM Automation documents and Run Command. It leverages boto3 SSM client methods (start_automation_execution, send_command, get_command_invocation) to execute both AWS-managed runbooks (AWS-RunPatchBaseline, AWS-RestartEC2Instance, AWSSupport-TroubleshootSSH) and custom Automation documents written in YAML with aws:executeScript, aws:runCommand, aws:invokeLambdaFunction, and aws:approve steps. The skill handles parameter resolution from SSM Parameter Store (get_parameter, get_parameters_by_path) including SecureString decryption, manages execution with rate controls (MaxConcurrency, MaxErrors) for fleet-wide operations, and supports cross-account execution through shared documents and assume role configurations. It monitors automation execution status through describe_automation_executions, captures step-level output, and handles failure scenarios with onFailure/onCancel specifications. The executor also supports maintenance window integration via register_task_with_maintenance_window, compliance reporting through list_compliance_items, and State Manager associations for desired state enforcement across EC2 fleets.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-ssm-runbook-executor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-ssm-runbook-executor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-ssm-runbook-executor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-ssm-runbook-executor -a codex
```

### OpenClaw

```bash
clawhub install aws-ssm-runbook-executor
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-ssm-runbook-executor/)
