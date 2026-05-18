---
name: "Validate CloudFormation templates before deploy with cfn-lint"
slug: "validate-cloudformation-templates-before-deploy-with-cfn-lint"
description: "Catch CloudFormation schema, region, and intrinsic-function mistakes before a stack update fails in review or deployment."
github_stars: 2608
verification: "listed"
source: "https://github.com/aws-cloudformation/cfn-lint"
author: "AWS CloudFormation"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "aws-cloudformation/cfn-lint"
  github_stars: 2608
---

# Validate CloudFormation templates before deploy with cfn-lint

Catch CloudFormation schema, region, and intrinsic-function mistakes before a stack update fails in review or deployment.

## Prerequisites

Python or cfn-lint binary, CloudFormation templates

## Installation

Use the upstream install or setup path that matches your environment:
- pip install cfn-lint. If pip is not available, run
- brew install cfn-lint
- docker build --tag cfn-lint:latest .
- docker run --rm -v pwd:/data cfn-lint:latest /data/template.yaml

Requirements and caveats from upstream:
- <img alt="[cfn-lint logo]" src="https://github.com/aws-cloudformation/cfn-python-lint/blob/main/logo.png?raw=true" width="150" align="right">
- [![codecov](https://codecov.io/gh/aws-cloudformation/cfn-lint/branch/main/graph/badge.svg)](https://codecov.io/gh/aws-cloudformation/cfn-python-lint)
- Python 3.10 to 3.14 are supported.

Basic usage or getting-started notes:
- _To get information about the [SAM Transformation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html), run the linter with --info_
- ### Pip
- #### Optional dependencies

- Source: https://github.com/aws-cloudformation/cfn-lint
- Extracted from upstream docs: https://raw.githubusercontent.com/aws-cloudformation/cfn-lint/HEAD/README.md

## Documentation

- https://github.com/aws-cloudformation/cfn-lint

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-cloudformation-templates-before-deploy-with-cfn-lint/)
