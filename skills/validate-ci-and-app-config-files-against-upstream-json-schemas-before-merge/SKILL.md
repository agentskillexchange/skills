---
title: "Validate CI and app config files against upstream JSON schemas before merge"
slug: "validate-ci-and-app-config-files-against-upstream-json-schemas-before-merge"
verification: security_reviewed
source: "https://github.com/python-jsonschema/check-jsonschema"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "python-jsonschema/check-jsonschema"
  github_stars: 312
---
# Validate CI and app config files against upstream JSON schemas before merge

Use check-jsonschema when an agent needs to catch broken GitHub Actions, Renovate, Azure Pipelines, and other schema-backed config files before they hit CI. The agent picks the right schema hook, validates the changed files, and reports the exact key or structure that drifted from the contract.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-ci-and-app-config-files-against-upstream-json-schemas-before-merge/)
