---
name: Terraform Module Template Engine
description: Scaffolds production-ready Terraform modules using HCL templates with
  automated variable documentation via terraform-docs. Includes Terratest boilerplate
  and GitHub Actions CI workflow generation.
category: "Templates &amp; Workflows"
framework: Gemini
verification: security_reviewed
source: "https://agentskillexchange.com/skills/terraform-module-template-engine/"
---
# Terraform Module Template Engine

Scaffolds production-ready Terraform modules using HCL templates with automated variable documentation via terraform-docs. Includes Terratest boilerplate and GitHub Actions CI workflow generation.

This skill provides automated tooling for terraform module template engine workflows. It integrates directly with your development pipeline, offering configurable scanning depth, custom rule definitions, and structured output formats compatible with major CI/CD platforms. The agent handles authentication, rate limiting, and retry logic internally, so you can focus on reviewing results rather than managing infrastructure. Supports both interactive and headless operation modes with JSON and SARIF output for downstream processing. Includes built-in caching to minimize redundant API calls across sequential runs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-module-template-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-module-template-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-module-template-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-module-template-engine -a codex
```

### OpenClaw

```bash
clawhub install terraform-module-template-engine
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-template-engine/)
