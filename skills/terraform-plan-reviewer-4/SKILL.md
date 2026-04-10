---
title: "Terraform Plan Reviewer"
description: "Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec Go SDK. Identifies destructive changes, cost implications via Infracost API, and generates approval summaries."
slug: "terraform-plan-reviewer-4"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/terraform-plan-reviewer-4/"
listed: true
---

# Terraform Plan Reviewer

Parses Terraform plan JSON output from terraform show -json and the hashicorp/terraform-exec Go SDK. Identifies destructive changes, cost implications via Infracost API, and generates approval summaries.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install terraform-plan-reviewer-4
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Terraform Plan Reviewer skill analyzes Terraform plan output to provide intelligent infrastructure change reviews before apply. It parses the JSON plan format produced by terraform show -json and integrates with the hashicorp/terraform-exec Go SDK for programmatic plan execution. The skill classifies resource changes into categories: creates, updates, destroys, and replacements, flagging potentially destructive operations like database deletions or security group modifications. Integration with the Infracost API provides estimated cost impact for AWS, GCP, and Azure resources before changes are applied. The reviewer generates structured approval summaries with risk scores based on the sensitivity of modified resources, blast radius estimation, and dependency chain analysis. It supports Terraform workspace-aware reviews, module-level change grouping, and state drift detection by comparing plan output against expected configurations. The skill also validates provider version constraints, checks for deprecated resource attributes, and ensures backend configuration consistency. Output formats include Markdown summaries for PR comments, Slack notifications, and structured JSON for integration with custom approval workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-reviewer-4/)
