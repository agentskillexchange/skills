---
title: "Validate CI and app config files against upstream JSON schemas before merge"
slug: "validate-ci-and-app-config-files-against-upstream-json-schemas-before-merge"
description: "Use check-jsonschema when an agent needs to catch broken GitHub Actions, Renovate, Azure Pipelines, and other schema-backed config files before they hit CI. The agent picks the right schema hook, validates the changed files, and reports the exact key or structure that drifted from the contract."
verification: "security_reviewed"
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

Choose the install method that fits your setup:

1. Install from Agent Skill Exchange
2. Install with OpenClaw skill tools
3. Clone or copy the upstream project files
4. Add the skill to your local skills directory manually
5. Use the upstream package or repo install flow directly

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-ci-and-app-config-files-against-upstream-json-schemas-before-merge/)
