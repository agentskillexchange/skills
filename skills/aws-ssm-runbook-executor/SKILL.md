---
title: "AWS Systems Manager Runbook"
description: "Execute AWS Systems Manager Automation runbooks and Run Command documents using the SSM API and boto3. Supports cross-account execution, rate controls, and parameter store integration."
verification: "security_reviewed"
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
  license: "Apache-2.0"
---

# AWS Systems Manager Runbook

The AWS Systems Manager Runbook Executor skill automates operational procedures through AWS SSM Automation documents and Run Command. It leverages boto3 SSM client methods (start_automation_execution, send_command, get_command_invocation) to execute both AWS-managed runbooks (AWS-RunPatchBaseline, AWS-RestartEC2Instance, AWSSupport-TroubleshootSSH) and custom Automation documents written in YAML with aws:executeScript, aws:runCommand, aws:invokeLambdaFunction, and aws:approve steps. The skill handles parameter resolution from SSM Parameter Store (get_parameter, get_parameters_by_path) including SecureString decryption, manages execution with rate controls (MaxConcurrency, MaxErrors) for fleet-wide operations, and supports cross-account execution through shared documents and assume role configurations. It monitors automation execution status through describe_automation_executions, captures step-level output, and handles failure scenarios with onFailure/onCancel specifications. The executor also supports maintenance window integration via register_task_with_maintenance_window, compliance reporting through list_compliance_items, and State Manager associations for desired state enforcement across EC2 fleets.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-ssm-runbook-executor/)
