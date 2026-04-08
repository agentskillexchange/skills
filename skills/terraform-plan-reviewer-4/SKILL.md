---
title: Terraform Plan Reviewer
description: 'The Terraform Plan Reviewer skill analyzes Terraform plan output to
  provide intelligent infrastructure change reviews before apply. It parses the JSON
  plan format produced by terraform show -json and integrates with the hashicorp/terraform-exec
  Go SDK for programmatic plan execution. The skill classifies resource changes into
  categories: creates, updates, destroys, and replacements, flagging potentially destructive
  operations like database deletions or security group modifications. Integration
  with the Infracost API provides estimated cost impact for AWS, GCP, and Azure resources
  before changes are applied. The reviewer generates structured approval summaries
  with risk scores based on the sensitivity of modified resources, blast radius estimation,
  and dependency chain analysis. It supports Terraform workspace-aware reviews, module-level
  change grouping, and state drift detection by comparing plan output against expected
  configurations. The skill also validates provider version constraints, checks for
  deprecated resource attributes, and ensures backend configuration consistency. Output
  formats include Markdown summaries for PR comments, Slack notifications, and structured
  JSON for integration with custom approval workflows.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/terraform-plan-reviewer-4/
category:
- CI/CD Integrations
framework:
- Claude Code
---

# Terraform Plan Reviewer

The Terraform Plan Reviewer skill analyzes Terraform plan output to provide intelligent infrastructure change reviews before apply. It parses the JSON plan format produced by terraform show -json and integrates with the hashicorp/terraform-exec Go SDK for programmatic plan execution. The skill classifies resource changes into categories: creates, updates, destroys, and replacements, flagging potentially destructive operations like database deletions or security group modifications. Integration with the Infracost API provides estimated cost impact for AWS, GCP, and Azure resources before changes are applied. The reviewer generates structured approval summaries with risk scores based on the sensitivity of modified resources, blast radius estimation, and dependency chain analysis. It supports Terraform workspace-aware reviews, module-level change grouping, and state drift detection by comparing plan output against expected configurations. The skill also validates provider version constraints, checks for deprecated resource attributes, and ensures backend configuration consistency. Output formats include Markdown summaries for PR comments, Slack notifications, and structured JSON for integration with custom approval workflows.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-reviewer-4/)
