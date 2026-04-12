---
title: "Terraform Plan Diff Analyzer"
description: "Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/"
---

# Terraform Plan Diff Analyzer

Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/)
