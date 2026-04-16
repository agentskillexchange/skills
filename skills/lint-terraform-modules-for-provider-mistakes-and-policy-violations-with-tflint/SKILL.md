---
title: "Lint Terraform modules for provider mistakes and policy violations with TFLint"
description: "Check Terraform before plan or apply so invalid attributes, provider-specific mistakes, and custom rule violations are caught early."
verification: "listed"
source: "https://github.com/terraform-linters/tflint"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "terraform-linters/tflint"
  github_stars: 5677
---

# Lint Terraform modules for provider mistakes and policy violations with TFLint

Use TFLint when an agent is validating Terraform code before plan, apply, or review. It can catch provider-specific mistakes, unsupported arguments, deprecated patterns, and custom rule violations across modules before the infrastructure run reaches a more expensive failure point. The boundary is Terraform linting and rule enforcement, not a generic infrastructure platform card.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-terraform-modules-for-provider-mistakes-and-policy-violations-with-tflint/)
