---
title: "Lint YAML configs for syntax, duplicate keys, and style drift before CI or deploy"
slug: "lint-yaml-configs-for-syntax-duplicate-keys-and-style-drift-before-ci-or-deploy"
description: "Uses yamllint to inspect hand-written or generated YAML before it reaches CI or deploy. The agent returns line-level syntax, duplicate-key, indentation, and formatting findings so config changes can be fixed before they break pipelines or runtime environments."
verification: security_reviewed
source: "https://github.com/adrienverge/yamllint"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "adrienverge/yamllint"
  github_stars: 3360
---

# Lint YAML configs for syntax, duplicate keys, and style drift before CI or deploy

Uses yamllint to inspect hand-written or generated YAML before it reaches CI or deploy. The agent returns line-level syntax, duplicate-key, indentation, and formatting findings so config changes can be fixed before they break pipelines or runtime environments.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-yaml-configs-for-syntax-duplicate-keys-and-style-drift-before-ci-or-deploy/)
