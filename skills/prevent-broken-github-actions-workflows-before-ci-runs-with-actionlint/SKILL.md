---
name: "Prevent broken GitHub Actions workflows before CI runs with actionlint"
slug: "prevent-broken-github-actions-workflows-before-ci-runs-with-actionlint"
description: "Use actionlint when an agent needs to inspect GitHub Actions workflow files before a push or pull request lands. The skill checks syntax, expressions, action inputs, runner labels, cron patterns, and a few security footguns so the agent can stop bad workflow changes before CI burns time."
github_stars: 3782
verification: "security_reviewed"
source: "https://github.com/rhysd/actionlint"
author: "rhysd"
publisher_type: "Open Source Project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "rhysd/actionlint"
  github_stars: 3782
---

# Prevent broken GitHub Actions workflows before CI runs with actionlint

Use actionlint when an agent needs to inspect GitHub Actions workflow files before a push or pull request lands. The skill checks syntax, expressions, action inputs, runner labels, cron patterns, and a few security footguns so the agent can stop bad workflow changes before CI burns time.

## Prerequisites

actionlint binary, plus optional shellcheck and pyflakes for deeper inline script checks

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

- https://github.com/rhysd/actionlint/blob/main/docs/usage.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prevent-broken-github-actions-workflows-before-ci-runs-with-actionlint/)
