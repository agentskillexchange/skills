---
title: "Lint Terraform modules for provider mistakes and policy violations with TFLint"
description: "Check Terraform before plan or apply so invalid attributes, provider-specific mistakes, and custom rule violations are caught early."
verification: "security_reviewed"
source: "https://github.com/terraform-linters/tflint"
author: "terraform-linters"
publisher_type: "organization"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "terraform-linters/tflint"
  github_stars: 5677
---

# Lint Terraform modules for provider mistakes and policy violations with TFLint

Check Terraform before plan or apply so invalid attributes, provider-specific mistakes, and custom rule violations are caught early.

## Prerequisites

TFLint binary, Terraform configuration, optional plugin rules

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install TFLint for your platform, initialize any required plugins with `tflint --init`, then run `tflint` in the Terraform repository before plan or CI approval.
```

## Documentation

- https://github.com/terraform-linters/tflint

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-terraform-modules-for-provider-mistakes-and-policy-violations-with-tflint/)
