---
title: "Validate CI and app config files against upstream JSON schemas before merge"
description: "Use check-jsonschema when an agent needs to catch broken GitHub Actions, Renovate, Azure Pipelines, and other schema-backed config files before they hit CI. The agent picks the right schema hook, validates the changed files, and reports the exact key or structure that drifted from the contract."
verification: security_reviewed
source: "https://github.com/python-jsonschema/check-jsonschema"
category:
  - "Code Quality &amp; Review"
tool_ecosystem:
  github_repo: "python-jsonschema/check-jsonschema"
  github_stars: 312
---

# Validate CI and app config files against upstream JSON schemas before merge

Use check-jsonschema when an agent needs to catch broken GitHub Actions, Renovate, Azure Pipelines, and other schema-backed config files before they hit CI. The agent picks the right schema hook, validates the changed files, and reports the exact key or structure that drifted from the contract.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-ci-and-app-config-files-against-upstream-json-schemas-before-merge/)
