---
title: "AWS CloudFormation Stack Diagnostics"
description: "Diagnoses failed AWS CloudFormation stack operations using the AWS CLI (aws cloudformation describe-stack-events) and cfn-lint validator. Traces resource creation failures, rollback causes, and nested stack dependency chains."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-cloudformation-stack-diagnostics/"
category:
  - "Runbooks & Diagnostics"
framework:
  - "ChatGPT Agents"
---

# AWS CloudFormation Stack Diagnostics

The AWS CloudFormation Stack Diagnostics skill automates troubleshooting of failed CloudFormation stack deployments. It uses the AWS CLI commands aws cloudformation describe-stack-events to trace resource-level failure chains, aws cloudformation detect-stack-drift for drift detection, and aws cloudformation get-template to retrieve deployed templates for comparison.


The skill integrates with cfn-lint (cloudformation-linter) for template validation against AWS CloudFormation Resource Specification, catching errors before deployment. It validates both JSON and YAML templates, checks resource property types against provider schemas, and verifies IAM policy document syntax.


Diagnostic workflows include stack event timeline analysis to identify the root cause resource in creation/update failures, rollback trigger identification through ROLLBACK_IN_PROGRESS event tracing, nested stack failure propagation tracking via parent-child stack relationships, and change set analysis using aws cloudformation describe-change-set for safe update previewing.


Advanced capabilities include custom resource (AWS::CloudFormation::CustomResource) Lambda log correlation via CloudWatch Logs Insights queries, stack policy analysis for update protection verification, resource import feasibility checking for brownfield adoption, and integration with AWS CloudFormation Guard (cfn-guard) for policy-as-code compliance validation against organizational rules.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudformation-stack-diagnostics/)
