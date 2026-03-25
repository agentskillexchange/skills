---
name: "AWS CloudFormation Stack Diagnostics"
description: "Diagnoses failed AWS CloudFormation stack operations using the AWS CLI (aws cloudformation describe-stack-events) and cfn-lint validator. Traces resource creation failures, rollback causes, and nested stack dependency chains."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudformation-stack-diagnostics/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "cloudformation"  # from ase_tool_match
  github_stars: 2611  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws-cloudformation/cfn-lint"  # from ase_github_repo
  license: "MIT-0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# AWS CloudFormation Stack Diagnostics

Diagnoses failed AWS CloudFormation stack operations using the AWS CLI (aws cloudformation describe-stack-events) and cfn-lint validator. Traces resource creation failures, rollback causes, and nested stack dependency chains.

## Overview

The AWS CloudFormation Stack Diagnostics skill automates troubleshooting of failed CloudFormation stack deployments. It uses the AWS CLI commands aws cloudformation describe-stack-events to trace resource-level failure chains, aws cloudformation detect-stack-drift for drift detection, and aws cloudformation get-template to retrieve deployed templates for comparison.

The skill integrates with cfn-lint (cloudformation-linter) for template validation against AWS CloudFormation Resource Specification, catching errors before deployment. It validates both JSON and YAML templates, checks resource property types against provider schemas, and verifies IAM policy document syntax.

Diagnostic workflows include stack event timeline analysis to identify the root cause resource in creation/update failures, rollback trigger identification through ROLLBACK_IN_PROGRESS event tracing, nested stack failure propagation tracking via parent-child stack relationships, and change set analysis using aws cloudformation describe-change-set for safe update previewing.

Advanced capabilities include custom resource (AWS::CloudFormation::CustomResource) Lambda log correlation via CloudWatch Logs Insights queries, stack policy analysis for update protection verification, resource import feasibility checking for brownfield adoption, and integration with AWS CloudFormation Guard (cfn-guard) for policy-as-code compliance validation against organizational rules.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-stack-diagnostics
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-stack-diagnostics -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-stack-diagnostics -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-stack-diagnostics -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudformation-stack-diagnostics
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-cloudformation-stack-diagnostics/
