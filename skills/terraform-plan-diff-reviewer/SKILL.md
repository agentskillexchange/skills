---
title: "Terraform Plan Diff Reviewer"
slug: "terraform-plan-diff-reviewer"
description: "Parses terraform plan JSON output to identify destructive changes, security group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace state comparison."
github_stars: 48146
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Plan Diff Reviewer

Parses terraform plan JSON output to identify destructive changes, security group modifications, and IAM policy drift. Uses the Terraform Cloud API for workspace state comparison.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-reviewer/)
