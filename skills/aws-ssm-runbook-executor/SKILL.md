---
title: "AWS Systems Manager Runbook"
description: "Execute AWS Systems Manager Automation runbooks and Run Command documents using the SSM API and boto3. Supports cross-account execution, rate controls, and parameter store integration."
slug: "aws-ssm-runbook-executor"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-ssm-runbook-executor/"
---

# AWS Systems Manager Runbook

Execute AWS Systems Manager Automation runbooks and Run Command documents using the SSM API and boto3. Supports cross-account execution, rate controls, and parameter store integration.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install aws-ssm-runbook-executor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The AWS Systems Manager Runbook Executor skill automates operational procedures through AWS SSM Automation documents and Run Command. It leverages boto3 SSM client methods (start_automation_execution, send_command, get_command_invocation) to execute both AWS-managed runbooks (AWS-RunPatchBaseline, AWS-RestartEC2Instance, AWSSupport-TroubleshootSSH) and custom Automation documents written in YAML with aws:executeScript, aws:runCommand, aws:invokeLambdaFunction, and aws:approve steps. The skill handles parameter resolution from SSM Parameter Store (get_parameter, get_parameters_by_path) including SecureString decryption, manages execution with rate controls (MaxConcurrency, MaxErrors) for fleet-wide operations, and supports cross-account execution through shared documents and assume role configurations. It monitors automation execution status through describe_automation_executions, captures step-level output, and handles failure scenarios with onFailure/onCancel specifications. The executor also supports maintenance window integration via register_task_with_maintenance_window, compliance reporting through list_compliance_items, and State Manager associations for desired state enforcement across EC2 fleets.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-ssm-runbook-executor/)
