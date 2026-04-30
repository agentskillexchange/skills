---
title: "AWS CloudFormation Stack Diagnostics"
description: "Diagnoses failed AWS CloudFormation stack operations using the AWS CLI (aws cloudformation describe-stack-events) and cfn-lint validator. Traces resource creation failures, rollback causes, and nested stack dependency chains."
verification: "security_reviewed"
source: "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html"
author: "Amazon Web Services"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
---

# AWS CloudFormation Stack Diagnostics

Diagnoses failed AWS CloudFormation stack operations using the AWS CLI (aws cloudformation describe-stack-events) and cfn-lint validator. Traces resource creation failures, rollback causes, and nested stack dependency chains.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Documentation

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudformation-stack-diagnostics/)
