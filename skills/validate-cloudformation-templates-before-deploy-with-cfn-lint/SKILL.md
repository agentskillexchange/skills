---
title: "Validate CloudFormation templates before deploy with cfn-lint"
description: "Catch CloudFormation schema, region, and intrinsic-function mistakes before a stack update fails in review or deployment."
verification: "listed"
source: "https://github.com/aws-cloudformation/cfn-lint"
author: "AWS CloudFormation"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "aws-cloudformation/cfn-lint"
  github_stars: 2608
---

# Validate CloudFormation templates before deploy with cfn-lint

Catch CloudFormation schema, region, and intrinsic-function mistakes before a stack update fails in review or deployment.

## Prerequisites

Python or cfn-lint binary, CloudFormation templates

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install cfn-lint` or use the project binaries, then run `cfn-lint` on the template files before review, CI, or deployment.
```

## Documentation

- https://github.com/aws-cloudformation/cfn-lint

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-cloudformation-templates-before-deploy-with-cfn-lint/)
