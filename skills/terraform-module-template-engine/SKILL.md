---
title: "Terraform Module Template Engine"
description: "Scaffolds production-ready Terraform modules using HCL templates with automated variable documentation via terraform-docs. Includes Terratest boilerplate and GitHub Actions CI workflow generation."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category:
  - "Templates &amp; Workflows"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Module Template Engine

Scaffolds production-ready Terraform modules using HCL templates with automated variable documentation via terraform-docs. Includes Terratest boilerplate and GitHub Actions CI workflow generation.

This skill provides automated tooling for terraform module template engine workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-template-engine/)
