---
title: "Pin GitHub Actions and reusable workflow refs to immutable SHAs before CI changes merge with pinact"
description: "Rewrite mutable GitHub Actions refs to commit SHAs so workflow changes do not ship with drifting dependencies."
verification: listed
source: "https://github.com/suzuki-shunsuke/pinact"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "suzuki-shunsuke/pinact"
  github_stars: 917
---

# Pin GitHub Actions and reusable workflow refs to immutable SHAs before CI changes merge with pinact

Use pinact when an agent needs to harden GitHub workflow files by replacing mutable action refs with immutable commit SHAs, not when the user is just browsing Actions docs or running a generic workflow linter. The workflow is specific: inspect workflow and composite action files, pin third-party actions and reusable workflows, and optionally verify version annotations before merge. That scope boundary, automated immutable-ref enforcement for GitHub Actions files, keeps it skill-shaped and distinct from broader CI tooling.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pin-github-actions-and-reusable-workflow-refs-to-immutable-shas-before-ci-changes-merge-with-pinact
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/pin-github-actions-and-reusable-workflow-refs-to-immutable-shas-before-ci-changes-merge-with-pinact` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pin-github-actions-and-reusable-workflow-refs-to-immutable-shas-before-ci-changes-merge-with-pinact/)
