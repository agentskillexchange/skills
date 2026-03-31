---
name: "Terraform Module Scaffolder"
description: "Scaffolds Terraform modules using the HCL SDK with provider schema introspection and automatic variable extraction. Generates documentation via terraform-docs API, validates with tflint rules, and publishes to Terraform Registry via API."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/hashicorp/terraform"
tool_ecosystem:
  tool: terraform
  github_repo: hashicorp/terraform
  github_stars: 48003
  maintained: true
---
# Terraform Module Scaffolder

Scaffolds Terraform modules using the HCL SDK with provider schema introspection and automatic variable extraction. Generates documentation via terraform-docs API, validates with tflint rules, and publishes to Terraform Registry via API.

## Overview

Scaffolds Terraform modules using the HCL SDK with provider schema introspection and automatic variable extraction. Generates documentation via terraform-docs API, validates with tflint rules, and publishes to Terraform Registry via API.

This skill provides a comprehensive automation layer for developers and teams who need reliable, repeatable workflows. It handles authentication, rate limiting, and error recovery automatically, so you can focus on the logic that matters. The agent monitors for changes in real time and applies incremental updates to minimize API calls and reduce latency. Configuration is handled through a simple YAML manifest that defines inputs, outputs, and trigger conditions. Built-in logging captures every action for audit trails and debugging. Supports both interactive and headless modes, making it suitable for CI/CD pipelines as well as local development. The skill includes pre-built templates for common use cases and can be extended with custom plugins. Error handling follows exponential backoff with jitter for transient failures and provides clear diagnostic messages for permanent errors. Compatible with major operating systems and containerized environments. Tested against production workloads with comprehensive integration test suites.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-module-scaffolder-hcl-sdk
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-module-scaffolder-hcl-sdk -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-module-scaffolder-hcl-sdk -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-module-scaffolder-hcl-sdk -a codex
```

### OpenClaw

```bash
clawhub install terraform-module-scaffolder-hcl-sdk
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-scaffolder-hcl-sdk/)
