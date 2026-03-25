---
name: "AWS CloudFormation Drift Detector"
description: "Monitors AWS CloudFormation stacks for configuration drift using the AWS SDK DetectStackDrift and DescribeStackResourceDrifts APIs. Generates remediation templates and integrates with AWS Config rules for continuous compliance."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/aws-cloudformation-drift-detector-4/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "aws"  # from ase_tool_match
  github_stars: 3594  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws/aws-sdk-js-v3"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# AWS CloudFormation Drift Detector

Monitors AWS CloudFormation stacks for configuration drift using the AWS SDK DetectStackDrift and DescribeStackResourceDrifts APIs. Generates remediation templates and integrates with AWS Config rules for continuous compliance.

## Overview

The AWS CloudFormation Drift Detector automates infrastructure compliance monitoring by continuously checking CloudFormation stacks for configuration drift. It uses the AWS SDK CloudFormation client to call DetectStackDrift, polls drift detection status, and retrieves detailed results via DescribeStackResourceDrifts for each stack resource.

The skill categorizes drift by resource type and modification scope, distinguishing between property-level changes and resource deletions. It generates remediation CloudFormation template patches that bring drifted resources back into compliance, with change set previews before execution.

Integration with AWS Config provides continuous compliance evaluation using managed rules like cloudformation-stack-drift-detection-check and custom Lambda-backed rules for organization-specific policies. The detector also interfaces with AWS Systems Manager Parameter Store to track configuration baselines, SNS topics for drift alert notifications, and EventBridge rules for scheduled drift detection across multiple accounts using AWS Organizations StackSets. Reports are generated in both JSON and HTML formats for audit documentation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector-4
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector-4 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector-4 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-cloudformation-drift-detector-4 -a codex
```

### OpenClaw

```bash
clawhub install aws-cloudformation-drift-detector-4
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-cloudformation-drift-detector-4/
