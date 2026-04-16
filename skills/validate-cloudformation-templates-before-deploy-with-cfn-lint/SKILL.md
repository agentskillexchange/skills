---
title: "Validate CloudFormation templates before deploy with cfn-lint"
description: "Catch CloudFormation schema, region, and intrinsic-function mistakes before a stack update fails in review or deployment."
verification: "listed"
source: "https://github.com/aws-cloudformation/cfn-lint"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "aws-cloudformation/cfn-lint"
  github_stars: 2608
---

# Validate CloudFormation templates before deploy with cfn-lint

Use cfn-lint when an agent needs to review or gate AWS CloudFormation changes before deployment. It can validate template structure, catch invalid properties, check region-specific resource rules, and surface intrinsic-function mistakes before they become failed stack operations. The scope is tightly bounded to pre-deploy CloudFormation validation, which keeps this from collapsing into a general AWS product listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-cloudformation-templates-before-deploy-with-cfn-lint/)
