---
title: "Terraform Plan Diff Analyzer"
description: "Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/"
category:
  - "CI/CD Integrations"
---

# Terraform Plan Diff Analyzer

Parses Terraform plan JSON output to summarize resource changes, detect destructive actions, and flag policy violations. Uses the terraform show -json command and the Terraform Cloud API to retrieve plan artifacts. Integrates with OPA (Open Policy Agent) for policy-as-code enforcement on planned changes.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-plan-diff-analyzer/)
