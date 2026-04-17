---
title: "AWS Systems Manager Runbook"
description: "The AWS Systems Manager Runbook Executor skill automates operational procedures through AWS SSM Automation documents and Run Command. It leverages boto3 SSM client methods (start_automation_execution, send_command, get_command_invocation) to execute both AWS-managed runbooks (AWS-RunPatchBaseline, AWS-RestartEC2Instance, AWSSupport-TroubleshootSSH) and custom Automation documents written in YAML with aws:executeScript, aws:runCommand, aws:invokeLambdaFunction, and aws:approve steps. The skill handles parameter resolution from SSM Parameter Store (get_parameter, get_parameters_by_path) including SecureString decryption, manages execution with rate controls (MaxConcurrency, MaxErrors) for fleet-wide operations, and supports cross-account execution through shared documents and assume role configurations. It monitors automation execution status through describe_automation_executions, captures step-level output, and handles failure scenarios with onFailure/onCancel specifications. The executor also supports maintenance window integration via register_task_with_maintenance_window, compliance reporting through list_compliance_items, and State Manager associations for desired state enforcement across EC2 fleets."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS Systems Manager Runbook

The AWS Systems Manager Runbook Executor skill automates operational procedures through AWS SSM Automation documents and Run Command. It leverages boto3 SSM client methods (start_automation_execution, send_command, get_command_invocation) to execute both AWS-managed runbooks (AWS-RunPatchBaseline, AWS-RestartEC2Instance, AWSSupport-TroubleshootSSH) and custom Automation documents written in YAML with aws:executeScript, aws:runCommand, aws:invokeLambdaFunction, and aws:approve steps. The skill handles parameter resolution from SSM Parameter Store (get_parameter, get_parameters_by_path) including SecureString decryption, manages execution with rate controls (MaxConcurrency, MaxErrors) for fleet-wide operations, and supports cross-account execution through shared documents and assume role configurations. It monitors automation execution status through describe_automation_executions, captures step-level output, and handles failure scenarios with onFailure/onCancel specifications. The executor also supports maintenance window integration via register_task_with_maintenance_window, compliance reporting through list_compliance_items, and State Manager associations for desired state enforcement across EC2 fleets.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-ssm-runbook-executor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/aws-ssm-runbook-executor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-ssm-runbook-executor/)
