---
title: "Terraform Plan Reviewer"
description: "Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec Go SDK. Identifies destructive changes, cost implications via Infracost API, and generates approval summaries."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Plan Reviewer

The Terraform Plan Reviewer skill analyzes Terraform plan output to provide intelligent infrastructure change reviews before apply. It parses the JSON plan format produced by terraform show -json and integrates with the hashicorp/terraform-exec Go SDK for programmatic plan execution. The skill classifies resource changes into categories: creates, updates, destroys, and replacements, flagging potentially destructive operations like database deletions or security group modifications. Integration with the Infracost API provides estimated cost impact for AWS, GCP, and Azure resources before changes are applied. The reviewer generates structured approval summaries with risk scores based on the sensitivity of modified resources, blast radius estimation, and dependency chain analysis. It supports Terraform workspace-aware reviews, module-level change grouping, and state drift detection by comparing plan output against expected configurations. The skill also validates provider version constraints, checks for deprecated resource attributes, and ensures backend configuration consistency. Output formats include Markdown summaries for PR comments, Slack notifications, and structured JSON for integration with custom approval workflows.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-reviewer-4/)
