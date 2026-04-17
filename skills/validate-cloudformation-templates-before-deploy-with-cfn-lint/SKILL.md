---
title: "Validate CloudFormation templates before deploy with cfn-lint"
description: "Use cfn-lint when an agent needs to review or gate AWS CloudFormation changes before deployment. It can validate template structure, catch invalid properties, check region-specific resource rules, and surface intrinsic-function mistakes before they become failed stack operations. The scope is tightly bounded to pre-deploy CloudFormation validation, which keeps this from collapsing into a general AWS product listing."
verification: listed
source: "https://github.com/aws-cloudformation/cfn-lint"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "aws-cloudformation/cfn-lint"
  github_stars: 2608
---

# Validate CloudFormation templates before deploy with cfn-lint

Use cfn-lint when an agent needs to review or gate AWS CloudFormation changes before deployment. It can validate template structure, catch invalid properties, check region-specific resource rules, and surface intrinsic-function mistakes before they become failed stack operations. The scope is tightly bounded to pre-deploy CloudFormation validation, which keeps this from collapsing into a general AWS product listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/validate-cloudformation-templates-before-deploy-with-cfn-lint
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/validate-cloudformation-templates-before-deploy-with-cfn-lint` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-cloudformation-templates-before-deploy-with-cfn-lint/)
