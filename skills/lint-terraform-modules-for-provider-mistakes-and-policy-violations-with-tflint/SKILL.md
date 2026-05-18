---
name: "Lint Terraform modules for provider mistakes and policy violations with TFLint"
slug: "lint-terraform-modules-for-provider-mistakes-and-policy-violations-with-tflint"
description: "Check Terraform before plan or apply so invalid attributes, provider-specific mistakes, and custom rule violations are caught early."
github_stars: 5677
verification: "security_reviewed"
source: "https://github.com/terraform-linters/tflint"
author: "terraform-linters"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "terraform-linters/tflint"
  github_stars: 5677
---

# Lint Terraform modules for provider mistakes and policy violations with TFLint

Check Terraform before plan or apply so invalid attributes, provider-specific mistakes, and custom rule violations are caught early.

## Prerequisites

TFLint binary, Terraform configuration, optional plugin rules

## Installation

Use the upstream install or setup path that matches your environment:
- brew install terraform-linters/tap/tflint
- docker run --rm -v $(pwd):/data -t ghcr.io/terraform-linters/tflint
- docker run --rm -v $(pwd):/data -t --entrypoint /bin/sh ghcr.io/terraform-linters/tflint -c "tflint --init && tflint"

Requirements and caveats from upstream:
- ### Docker
- Instead of installing directly, you can use the Docker image:
- To download plugins, you can override the entrypoint to a shell (sh) to run --init and the main command in a single docker run command:

Basic usage or getting-started notes:
- Download the appropriate archive from the [latest release](https://github.com/terraform-linters/tflint/releases/latest), verify it, and install the binary:
- console
- curl -sSLO https://github.com/terraform-linters/tflint/releases/latest/download/tflint_linux_amd64.zip

- Source: https://github.com/terraform-linters/tflint
- Extracted from upstream docs: https://raw.githubusercontent.com/terraform-linters/tflint/HEAD/README.md

## Documentation

- https://github.com/terraform-linters/tflint

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-terraform-modules-for-provider-mistakes-and-policy-violations-with-tflint/)
