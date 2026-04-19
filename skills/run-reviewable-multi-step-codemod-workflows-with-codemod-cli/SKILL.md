---
title: "Run reviewable multi-step codemod workflows with Codemod CLI"
description: "Best for: codebase migrations that need staged transformations, local testing, and a workflow definition an agent can run in CI or from the terminal. Codemod CLI is the local workflow engine behind Codemod&#8217;s broader ecosystem. It can scaffold codemod projects, run workflow YAMLs, and execute multi-step migration pipelines with explicit checkpoints. That is meaningfully different from a plain AST engine or hosted registry listing. When to invoke it Invoke this skill when a repository change needs a repeatable migration workflow, especially for framework upgrades or coordinated refactors that benefit from staging and review rather than a single raw codemod command. Scope boundary This skill is scoped to the local CLI workflow engine. It is not a listing for the hosted Codemod platform, registry, or company. The publishable job-to-be-done is: scaffold or run a multi-step codemod workflow and inspect the resulting code changes. Install notes Install the CLI with npx codemod or the documented package method. Initialize a codemod project or create a workflow YAML. Run npx codemod workflow run -w workflow.yaml to execute the migration locally or in CI."
source: "https://github.com/codemod/codemod"
verification: "listed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "codemod/codemod"
  github_stars: 979
---

# Run reviewable multi-step codemod workflows with Codemod CLI

Best for: codebase migrations that need staged transformations, local testing, and a workflow definition an agent can run in CI or from the terminal. Codemod CLI is the local workflow engine behind Codemod&#8217;s broader ecosystem. It can scaffold codemod projects, run workflow YAMLs, and execute multi-step migration pipelines with explicit checkpoints. That is meaningfully different from a plain AST engine or hosted registry listing. When to invoke it Invoke this skill when a repository change needs a repeatable migration workflow, especially for framework upgrades or coordinated refactors that benefit from staging and review rather than a single raw codemod command. Scope boundary This skill is scoped to the local CLI workflow engine. It is not a listing for the hosted Codemod platform, registry, or company. The publishable job-to-be-done is: scaffold or run a multi-step codemod workflow and inspect the resulting code changes. Install notes Install the CLI with npx codemod or the documented package method. Initialize a codemod project or create a workflow YAML. Run npx codemod workflow run -w workflow.yaml to execute the migration locally or in CI.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-reviewable-multi-step-codemod-workflows-with-codemod-cli/)
