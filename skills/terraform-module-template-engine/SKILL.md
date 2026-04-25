---
title: "Terraform Module Template Engine"
description: "Scaffolds production-ready Terraform modules using HCL templates with automated variable documentation via terraform-docs. Includes Terratest boilerplate and GitHub Actions CI workflow generation."
verification: "security_reviewed"
source: "https://github.com/hashicorp/terraform"
category:
  - "Templates & Workflows"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "hashicorp/terraform"
  github_stars: 48146
---

# Terraform Module Template Engine

Scaffolds production-ready Terraform modules using HCL templates with automated variable documentation via terraform-docs. Includes Terratest boilerplate and GitHub Actions CI workflow generation. This skill provides automated tooling for terraform module template engine workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/terraform-module-template-engine/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/terraform-module-template-engine
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/terraform-module-template-engine`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-template-engine/)
