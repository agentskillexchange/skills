---
title: "Orchestrate multi-environment OpenTofu and Terraform stacks with shared config and dependency ordering using Terragrunt"
description: "Coordinate layered Terraform or OpenTofu stacks across environments so plan and apply runs happen in the right order with shared inputs and less drift."
verification: listed
source: "https://github.com/gruntwork-io/terragrunt"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "gruntwork-io/terragrunt"
  github_stars: 9503
---

# Orchestrate multi-environment OpenTofu and Terraform stacks with shared config and dependency ordering using Terragrunt

Use Terragrunt when an agent needs to run a multi-stack OpenTofu or Terraform workflow with shared configuration, dependency ordering, and environment-aware orchestration, not when a user is simply managing infrastructure in Terraform by hand. The job is specific: assemble stack inputs, resolve dependencies between units, and run plan or apply in a predictable sequence across environments. That scope boundary, orchestrating multi-stack IaC execution rather than listing Terraform or Terragrunt as products, makes this skill-shaped.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/orchestrate-multi-environment-opentofu-and-terraform-stacks-with-shared-config-and-dependency-ordering-using-terragrunt
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/orchestrate-multi-environment-opentofu-and-terraform-stacks-with-shared-config-and-dependency-ordering-using-terragrunt` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/orchestrate-multi-environment-opentofu-and-terraform-stacks-with-shared-config-and-dependency-ordering-using-terragrunt/)
