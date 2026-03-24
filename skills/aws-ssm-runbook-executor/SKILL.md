---
name: "AWS Systems Manager Runbook"
description: "Execute AWS Systems Manager Automation runbooks and Run Command documents using the SSM API and boto3. Supports cross-account execution, rate controls, and parameter store integration."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-ssm-runbook-executor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "aws"  # from ase_tool_match
  github_stars: 3594  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws/aws-sdk-js-v3"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# AWS Systems Manager Runbook

Execute AWS Systems Manager Automation runbooks and Run Command documents using the SSM API and boto3. Supports cross-account execution, rate controls, and parameter store integration.

## Overview

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

- Marketplace: https://agentskillexchange.com/skills/aws-ssm-runbook-executor/
