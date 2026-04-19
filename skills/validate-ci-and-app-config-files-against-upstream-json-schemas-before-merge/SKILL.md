---
title: "Validate CI and app config files against upstream JSON schemas before merge"
description: "This skill uses check-jsonschema , the JSON Schema CLI and pre-commit hook maintained at python-jsonschema/check-jsonschema , to verify configuration files against official schemas before a branch is merged. It is a good fit when an agent is working in a repository full of operational config, not when the job is ordinary code linting. The useful trick here is that the tool already knows about common config families such as GitHub Actions workflows, Renovate, Azure Pipelines, Read the Docs, Dependabot, and other schema-backed files, so the agent can validate the real contract instead of just checking that the YAML parses. Invoke this skill when the agent is editing CI or automation files, reviewing a pull request that touches infrastructure config, or building a pre-merge guardrail for repositories that depend on schema-driven config. In those moments, using the product normally by hand is too brittle: an agent should discover which files changed, run the matching hook or schema target, and turn the failures into a concrete fix list. That makes it meaningfully different from listing a generic validator. The job is not “use a CLI.” The job is “stop schema drift before it breaks automation.” The scope boundary matters. This is not a general YAML linter, not a JSON Schema authoring toolkit, and not an SDK entry. It is a narrow validation skill for config that already has an upstream schema. Typical integrations include pipx install check-jsonschema , brew install check-jsonschema , pre-commit hooks, and CI steps that run on changed files only. Documentation lives at check-jsonschema.readthedocs.io , and the upstream repo publishes releases and packaged builds that agents can pin in repeatable workflows."
source: "https://github.com/python-jsonschema/check-jsonschema"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "python-jsonschema/check-jsonschema"
  github_stars: 312
---

# Validate CI and app config files against upstream JSON schemas before merge

This skill uses check-jsonschema , the JSON Schema CLI and pre-commit hook maintained at python-jsonschema/check-jsonschema , to verify configuration files against official schemas before a branch is merged. It is a good fit when an agent is working in a repository full of operational config, not when the job is ordinary code linting. The useful trick here is that the tool already knows about common config families such as GitHub Actions workflows, Renovate, Azure Pipelines, Read the Docs, Dependabot, and other schema-backed files, so the agent can validate the real contract instead of just checking that the YAML parses. Invoke this skill when the agent is editing CI or automation files, reviewing a pull request that touches infrastructure config, or building a pre-merge guardrail for repositories that depend on schema-driven config. In those moments, using the product normally by hand is too brittle: an agent should discover which files changed, run the matching hook or schema target, and turn the failures into a concrete fix list. That makes it meaningfully different from listing a generic validator. The job is not “use a CLI.” The job is “stop schema drift before it breaks automation.” The scope boundary matters. This is not a general YAML linter, not a JSON Schema authoring toolkit, and not an SDK entry. It is a narrow validation skill for config that already has an upstream schema. Typical integrations include pipx install check-jsonschema , brew install check-jsonschema , pre-commit hooks, and CI steps that run on changed files only. Documentation lives at check-jsonschema.readthedocs.io , and the upstream repo publishes releases and packaged builds that agents can pin in repeatable workflows.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-ci-and-app-config-files-against-upstream-json-schemas-before-merge/)
