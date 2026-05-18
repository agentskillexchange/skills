---
name: "Lint GitHub Actions workflows before CI runs with actionlint"
slug: "lint-github-actions-workflows-before-ci-runs-with-actionlint"
description: "Validate workflow syntax, expressions, and shell steps before broken GitHub Actions changes reach CI."
github_stars: 3787
verification: "listed"
source: "https://github.com/rhysd/actionlint"
author: "rhysd"
publisher_type: "individual"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "rhysd/actionlint"
  github_stars: 3787
---

# Lint GitHub Actions workflows before CI runs with actionlint

Validate workflow syntax, expressions, and shell steps before broken GitHub Actions changes reach CI.

## Prerequisites

actionlint binary and GitHub Actions workflow files

## Installation

Use the upstream install or setup path that matches your environment:
- go install github.com/rhysd/actionlint/cmd/actionlint@latest

Requirements and caveats from upstream:
- uses: actions/setup-node@v4
- key: ${{ matrix.platform }}-node-${{ hashFiles('**/package-lock.json') }}
- test.yaml:17:11: input "node_version" is not defined in action "actions/setup-node@v4". available inputs are "always-auth", "architecture", "cache", "cache-dependency-path", "check-latest", "node-version", "node-versi...

Basic usage or getting-started notes:
- **Actions usage check** to check that inputs at with: and outputs in steps.{id}.outputs are correct
- **[shellcheck][] and [pyflakes][] integrations** for scripts at run:
- **Example of broken workflow:**

- Source: https://github.com/rhysd/actionlint
- Extracted from upstream docs: https://raw.githubusercontent.com/rhysd/actionlint/HEAD/README.md

## Documentation

- https://github.com/rhysd/actionlint

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-github-actions-workflows-before-ci-runs-with-actionlint/)
