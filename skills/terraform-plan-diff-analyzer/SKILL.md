---
title: "Terraform Plan Diff Analyzer"
description: "Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes."
slug: terraform-plan-diff-analyzer
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/"
category:
- "CI/CD Integrations"
framework:
- "Cursor"
---
# Terraform Plan Diff Analyzer

Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes.

## Installation

You can install this skill in any of these ways:

1. Browse and install from Agent Skill Exchange.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule in your skills workspace.
4. Install it with your preferred agent skill or package manager if your setup supports that.
5. Copy the `SKILL.md` into an existing skill folder and adapt any referenced assets as needed.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/)
