---
title: "Generate Terraform module inputs and outputs docs with terraform-docs before review drift sets in"
description: "Refresh Terraform module documentation from source so variables, outputs, and providers stay aligned with the code before review or release."
verification: "security_reviewed"
source: "https://github.com/terraform-docs/terraform-docs"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "terraform-docs/terraform-docs"
  github_stars: 4753
---

# Generate Terraform module inputs and outputs docs with terraform-docs before review drift sets in

Use terraform-docs when a Terraform module’s README or reference docs need to be regenerated from the module source before review, release, or internal handoff. The upstream project is explicit about the workflow: inspect a module, extract its documented inputs, outputs, providers, and related metadata, then emit updated docs in stable formats.

Invoke this instead of editing module docs by hand when the real need is code-to-doc synchronization, not general Terraform authoring or infrastructure deployment. The scope boundary is narrow and skill-shaped: terraform-docs generates documentation from Terraform modules. It is not a Terraform platform listing, registry, or broad infrastructure-as-code framework card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/generate-terraform-module-inputs-and-outputs-docs-with-terraform-docs-before-review-drift-sets-in/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/generate-terraform-module-inputs-and-outputs-docs-with-terraform-docs-before-review-drift-sets-in
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/generate-terraform-module-inputs-and-outputs-docs-with-terraform-docs-before-review-drift-sets-in`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-terraform-module-inputs-and-outputs-docs-with-terraform-docs-before-review-drift-sets-in/)
