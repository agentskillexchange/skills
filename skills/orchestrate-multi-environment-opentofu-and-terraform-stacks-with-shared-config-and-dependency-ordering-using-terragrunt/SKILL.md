---
title: "Orchestrate multi-environment OpenTofu and Terraform stacks with shared config and dependency ordering using Terragrunt"
description: "Coordinate layered Terraform or OpenTofu stacks across environments so plan and apply runs happen in the right order with shared inputs and less drift."
verification: "listed"
source: "https://github.com/gruntwork-io/terragrunt"
author: "Gruntwork"
publisher_type: "organization"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "gruntwork-io/terragrunt"
  github_stars: 9503
---

# Orchestrate multi-environment OpenTofu and Terraform stacks with shared config and dependency ordering using Terragrunt

Coordinate layered Terraform or OpenTofu stacks across environments so plan and apply runs happen in the right order with shared inputs and less drift.

## Prerequisites

Terragrunt CLI, Terraform or OpenTofu, access to the target infrastructure codebase, environment credentials, and remote state or backend access as required by the stack

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Terragrunt from the upstream release or package instructions, ensure Terraform or OpenTofu is available, configure credentials and backends for the target environments, then run the documented terragrunt plan or apply workflow against the stack hierarchy.
```

## Documentation

- https://terragrunt.com

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/orchestrate-multi-environment-opentofu-and-terraform-stacks-with-shared-config-and-dependency-ordering-using-terragrunt/)
