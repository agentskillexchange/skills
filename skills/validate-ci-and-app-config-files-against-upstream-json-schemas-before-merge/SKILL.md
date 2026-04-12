---
title: "Validate CI and app config files against upstream JSON schemas before merge"
slug: "validate-ci-and-app-config-files-against-upstream-json-schemas-before-merge"
description: "Use check-jsonschema when an agent needs to catch broken GitHub Actions, Renovate, Azure Pipelines, and other schema-backed config files before they hit CI. The agent picks the right schema hook, validates the changed files, and reports the exact key or structure that drifted from the contract."
verification: security_reviewed
source: "https://github.com/python-jsonschema/check-jsonschema"
category:
  - "Code Quality &amp; Review"
tool_ecosystem:
  github_repo: "https://github.com/python-jsonschema/check-jsonschema"
  github_stars: 312
---

# Validate CI and app config files against upstream JSON schemas before merge

Use check-jsonschema when an agent needs to catch broken GitHub Actions, Renovate, Azure Pipelines, and other schema-backed config files before they hit CI. The agent picks the right schema hook, validates the changed files, and reports the exact key or structure that drifted from the contract.

## Installation

Choose the setup path that fits your environment:

1. Install from the Agent Skill Exchange UI
2. Clone or download this skill into your skills directory
3. Install with your agent platform's skill manager, if supported
4. Vendor the skill into your workspace or repo
5. Copy the skill files manually for local customization

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-ci-and-app-config-files-against-upstream-json-schemas-before-merge/)
