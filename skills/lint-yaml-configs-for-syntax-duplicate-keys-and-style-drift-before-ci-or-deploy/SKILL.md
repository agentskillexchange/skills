---
name: "Lint YAML configs for syntax, duplicate keys, and style drift before CI or deploy"
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

Use the upstream install or setup path that matches your environment:
- pip install --user yamllint

Requirements and caveats from upstream:
- Written in Python.
- Using pip, the Python package manager:

Basic usage or getting-started notes:
- ^^^^^^^^^^^^
- .. code:: bash
- yamllint is also packaged for all major operating systems, see installation

- Source: https://github.com/adrienverge/yamllint
- Extracted from upstream docs: https://raw.githubusercontent.com/adrienverge/yamllint/HEAD/README.rst

## Documentation

- https://yamllint.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-yaml-configs-for-syntax-duplicate-keys-and-style-drift-before-ci-or-deploy/)
