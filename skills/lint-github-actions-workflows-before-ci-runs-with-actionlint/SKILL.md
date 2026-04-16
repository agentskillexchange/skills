---
title: "Lint GitHub Actions workflows before CI runs with actionlint"
description: "Validate workflow syntax, expressions, and shell steps before broken GitHub Actions changes reach CI."
verification: "listed"
source: "https://github.com/rhysd/actionlint"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "rhysd/actionlint"
  github_stars: 3787
---

# Lint GitHub Actions workflows before CI runs with actionlint

Use actionlint when an agent needs a fast correctness pass on GitHub Actions files before they are pushed or approved. The agent can catch malformed workflow syntax, bad expressions, invalid event wiring, and shell step issues early in code review. The scope is narrowly limited to workflow validation before CI execution, not a generic GitHub product or automation framework listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-github-actions-workflows-before-ci-runs-with-actionlint/)
