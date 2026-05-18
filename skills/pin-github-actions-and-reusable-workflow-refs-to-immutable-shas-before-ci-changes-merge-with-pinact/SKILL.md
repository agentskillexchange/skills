---
name: "Pin GitHub Actions and reusable workflow refs to immutable SHAs before CI changes merge with pinact"
slug: "pin-github-actions-and-reusable-workflow-refs-to-immutable-shas-before-ci-changes-merge-with-pinact"
description: "Rewrite mutable GitHub Actions refs to commit SHAs so workflow changes do not ship with drifting dependencies."
github_stars: 917
verification: "security_reviewed"
source: "https://github.com/suzuki-shunsuke/pinact"
author: "suzuki-shunsuke"
publisher_type: "individual"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "suzuki-shunsuke/pinact"
  github_stars: 917
---

# Pin GitHub Actions and reusable workflow refs to immutable SHAs before CI changes merge with pinact

Rewrite mutable GitHub Actions refs to commit SHAs so workflow changes do not ship with drifting dependencies.

## Prerequisites

pinact CLI, repository access to the target .github workflow files, and optional GitHub token access for API-backed pin resolution.

## Installation

Requirements and caveats from upstream:
- For tags, the commit's Committer.Date is checked (requires additional API call)

Basic usage or getting-started notes:
- $ pinact run
- sh
- pinact run [<workflow file>...]

- Source: https://github.com/suzuki-shunsuke/pinact
- Extracted from upstream docs: https://raw.githubusercontent.com/suzuki-shunsuke/pinact/HEAD/README.md

## Documentation

- https://github.com/suzuki-shunsuke/pinact

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pin-github-actions-and-reusable-workflow-refs-to-immutable-shas-before-ci-changes-merge-with-pinact/)
