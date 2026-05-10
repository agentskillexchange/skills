---
title: "Lint YAML configs for syntax, duplicate keys, and style drift before CI or deploy"
slug: "lint-yaml-configs-for-syntax-duplicate-keys-and-style-drift-before-ci-or-deploy"
description: "Uses yamllint to inspect hand-written or generated YAML before it reaches CI or deploy. The agent returns line-level syntax, duplicate-key, indentation, and formatting findings so config changes can be fixed before they break pipelines or runtime environments."
github_stars: 3360
verification: "security_reviewed"
source: "https://github.com/adrienverge/yamllint"
author: "adrienverge"
publisher_type: "Open Source Project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "adrienverge/yamllint"
  github_stars: 3360
---

# Lint YAML configs for syntax, duplicate keys, and style drift before CI or deploy

Uses yamllint to inspect hand-written or generated YAML before it reaches CI or deploy. The agent returns line-level syntax, duplicate-key, indentation, and formatting findings so config changes can be fixed before they break pipelines or runtime environments.

## Prerequisites

Python and the yamllint CLI

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install --user yamllint
```

## Documentation

- https://yamllint.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-yaml-configs-for-syntax-duplicate-keys-and-style-drift-before-ci-or-deploy/)
