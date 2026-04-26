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

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-plan-reviewer-4/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-plan-reviewer-4
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-plan-reviewer-4`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-reviewer-4/)
