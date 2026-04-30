---
title: "Pin GitHub Actions and reusable workflow refs to immutable SHAs before CI changes merge with pinact"
description: "Rewrite mutable GitHub Actions refs to commit SHAs so workflow changes do not ship with drifting dependencies."
verification: "listed"
source: "https://github.com/suzuki-shunsuke/pinact"
author: "suzuki-shunsuke"
publisher_type: "individual"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "suzuki-shunsuke/pinact"
  github_stars: 917
---

# Pin GitHub Actions and reusable workflow refs to immutable SHAs before CI changes merge with pinact

Rewrite mutable GitHub Actions refs to commit SHAs so workflow changes do not ship with drifting dependencies.

## Prerequisites

pinact CLI, repository access to the target .github workflow files, and optional GitHub token access for API-backed pin resolution.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install pinact from the upstream release or package instructions, run it in the repository root to rewrite GitHub workflow or composite action refs, then review the resulting diffs and annotation checks before merging.
```

## Documentation

- https://github.com/suzuki-shunsuke/pinact

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pin-github-actions-and-reusable-workflow-refs-to-immutable-shas-before-ci-changes-merge-with-pinact/)
