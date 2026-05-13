---
title: "Lint Rego Policies Before Promotion with Regal"
slug: "lint-rego-policies-before-promotion-with-regal"
description: "Analyze Rego policy files for style, correctness, and maintainability issues before policy bundles are promoted."
github_stars: 373
verification: "security_reviewed"
source: "https://github.com/StyraInc/regal"
author: "Styra"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "StyraInc/regal"
  github_stars: 373
---

# Lint Rego Policies Before Promotion with Regal

Analyze Rego policy files for style, correctness, and maintainability issues before policy bundles are promoted.

## Prerequisites

Regal, Rego policy files, OPA-compatible policy repository

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Regal using the project instructions, then run it against your policy tree before promotion: regal lint path/to/policies
```

## Documentation

- https://www.openpolicyagent.org/projects/regal/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-rego-policies-before-promotion-with-regal/)
