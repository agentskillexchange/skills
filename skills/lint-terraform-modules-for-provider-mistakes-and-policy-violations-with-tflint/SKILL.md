---
title: "Lint Terraform modules for provider mistakes and policy violations with TFLint"
description: "Check Terraform before plan or apply so invalid attributes, provider-specific mistakes, and custom rule violations are caught early."
verification: listed
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/lint-terraform-modules-for-provider-mistakes-and-policy-violations-with-tflint
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/lint-terraform-modules-for-provider-mistakes-and-policy-violations-with-tflint` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-terraform-modules-for-provider-mistakes-and-policy-violations-with-tflint/)
