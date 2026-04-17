---
name: AWS CloudFormation Stack Diagnostics
description: Diagnoses failed AWS CloudFormation stack operations using the AWS CLI
  (aws cloudformation describe-stack-events) and cfn-lint validator. Traces resource
  creation failures, rollback causes, and nested stack dependency chains.
category: Runbooks & Diagnostics
framework: ChatGPT Agents
verification: security_reviewed
source: https://agentskillexchange.com/skills/aws-cloudformation-stack-diagnostics/
---
# AWS CloudFormation Stack Diagnostics
Diagnoses failed AWS CloudFormation stack operations using the AWS CLI (aws cloudformation describe-stack-events) and cfn-lint validator. Traces resource creation failures, rollback causes, and nested stack dependency chains.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-cloudformation-stack-diagnostics
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/aws-cloudformation-stack-diagnostics` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudformation-stack-diagnostics/)
