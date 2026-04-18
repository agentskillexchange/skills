---
title: "Generate and validate conventional commits and semver release bumps with Commitizen"
description: "Standardize commit messages, validate commit history, and calculate semver-aware release bumps without hand-rolled repo rules."
verification: security_reviewed
source: "https://github.com/commitizen-tools/commitizen"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "commitizen-tools/commitizen"
  github_stars: 3382
---

# Generate and validate conventional commits and semver release bumps with Commitizen

Use Commitizen when an agent needs to create or validate Conventional Commit messages, check a repository’s commit history against an agreed convention, and drive semver-aware version bumps from those commits. It fits release prep, changelog generation, and repo-hygiene workflows where commit semantics need to stay consistent across many edits.

A user should invoke this instead of using Git or a release tool normally when the task is commit convention enforcement and release bump orchestration, not everyday branching or publishing itself. The scope boundary is narrow and skill-shaped: Commitizen governs commit structure, changelog-friendly history checks, and calculated version bumps, not generic Git hosting, CI, or package registry management.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/generate-and-validate-conventional-commits-and-semver-release-bumps-with-commitizen
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/generate-and-validate-conventional-commits-and-semver-release-bumps-with-commitizen` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-and-validate-conventional-commits-and-semver-release-bumps-with-commitizen/)
