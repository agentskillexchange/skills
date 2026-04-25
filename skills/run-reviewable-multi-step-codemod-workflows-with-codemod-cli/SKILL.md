---
title: "Run reviewable multi-step codemod workflows with Codemod CLI"
description: "Use Codemod CLI when an agent needs to scaffold, test, and run a reviewable multi-step migration workflow with approval gates, rather than applying a one-off search-and-replace or browsing the hosted Codemod platform."
verification: "security_reviewed"
source: "https://github.com/codemod/codemod"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "codemod/codemod"
  github_stars: 979
---

# Run reviewable multi-step codemod workflows with Codemod CLI

Best for: codebase migrations that need staged transformations, local testing, and a workflow definition an agent can run in CI or from the terminal.

Codemod CLI is the local workflow engine behind Codemod’s broader ecosystem. It can scaffold codemod projects, run workflow YAMLs, and execute multi-step migration pipelines with explicit checkpoints. That is meaningfully different from a plain AST engine or hosted registry listing.

When to invoke it
Invoke this skill when a repository change needs a repeatable migration workflow, especially for framework upgrades or coordinated refactors that benefit from staging and review rather than a single raw codemod command.

Scope boundary
This skill is scoped to the local CLI workflow engine. It is not a listing for the hosted Codemod platform, registry, or company. The publishable job-to-be-done is: scaffold or run a multi-step codemod workflow and inspect the resulting code changes.

Install notes

Install the CLI with npx codemod or the documented package method.
Initialize a codemod project or create a workflow YAML.
Run npx codemod workflow run -w workflow.yaml to execute the migration locally or in CI.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-reviewable-multi-step-codemod-workflows-with-codemod-cli/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-reviewable-multi-step-codemod-workflows-with-codemod-cli
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-reviewable-multi-step-codemod-workflows-with-codemod-cli`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-reviewable-multi-step-codemod-workflows-with-codemod-cli/)
