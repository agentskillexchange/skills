---
title: "Terraform Module Template Engine"
description: "Scaffolds production-ready Terraform modules using HCL templates with automated variable documentation via terraform-docs. Includes Terratest boilerplate and GitHub Actions CI workflow generation."
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
category:
  - "Templates &amp; Workflows"
framework:
  - "Gemini"
---

# Terraform Module Template Engine

Scaffolds production-ready Terraform modules using HCL templates with automated variable documentation via terraform-docs. Includes Terratest boilerplate and GitHub Actions CI workflow generation.

This skill provides automated tooling for terraform module template engine workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-template-engine/)
