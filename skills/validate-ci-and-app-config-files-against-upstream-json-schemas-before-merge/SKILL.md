---
title: "Validate CI and app config files against upstream JSON schemas before merge"
description: "Use check-jsonschema when an agent needs to catch broken GitHub Actions, Renovate, Azure Pipelines, and other schema-backed config files before they hit CI. The agent picks the right schema hook, validates the changed files, and reports the exact key or structure that drifted from the contract."
slug: validate-ci-and-app-config-files-against-upstream-json-schemas-before-merge
verification: listed
source: "https://github.com/python-jsonschema/check-jsonschema"
category:
- "Code Quality & Review"
framework:
- "Multi-Framework"
tool_ecosystem:
  github_repo: python-jsonschema/check-jsonschema
  github_stars: 312
---
# Validate CI and app config files against upstream JSON schemas before merge

Use check-jsonschema when an agent needs to catch broken GitHub Actions, Renovate, Azure Pipelines, and other schema-backed config files before they hit CI. The agent picks the right schema hook, validates the changed files, and reports the exact key or structure that drifted from the contract.

## Installation

You can install this skill in any of these ways:

1. Browse and install from Agent Skill Exchange.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule in your skills workspace.
4. Install it with your preferred agent skill or package manager if your setup supports that.
5. Copy the `SKILL.md` into an existing skill folder and adapt any referenced assets as needed.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-ci-and-app-config-files-against-upstream-json-schemas-before-merge/)
