---
title: "Validate CloudFormation templates before deploy with cfn-lint"
description: "Catch CloudFormation schema, region, and intrinsic-function mistakes before a stack update fails in review or deployment."
verification: "listed"
source: "https://github.com/aws-cloudformation/cfn-lint"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "aws-cloudformation/cfn-lint"
  github_stars: 2608
---

# Validate CloudFormation templates before deploy with cfn-lint

Use cfn-lint when an agent needs to review or gate AWS CloudFormation changes before deployment. It can validate template structure, catch invalid properties, check region-specific resource rules, and surface intrinsic-function mistakes before they become failed stack operations. The scope is tightly bounded to pre-deploy CloudFormation validation, which keeps this from collapsing into a general AWS product listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/validate-cloudformation-templates-before-deploy-with-cfn-lint/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/validate-cloudformation-templates-before-deploy-with-cfn-lint
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/validate-cloudformation-templates-before-deploy-with-cfn-lint`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-cloudformation-templates-before-deploy-with-cfn-lint/)
