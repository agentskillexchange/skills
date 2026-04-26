---
title: "Enforce source-controlled AI checks in CI before merging risky changes with Continue CLI"
description: "Lets an agent define repo-native AI review checks as markdown files and run them as repeatable pull request status checks in CI."
verification: "security_reviewed"
source: "https://github.com/continuedev/continue"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "continuedev/continue"
  github_stars: 32622
---

# Enforce source-controlled AI checks in CI before merging risky changes with Continue CLI

Use Continue CLI when an agent needs to codify review rules in the repository and enforce them on every pull request. It fits security review, policy checks, and repo-specific quality gates where the job is to keep AI review logic versioned alongside the codebase.

Invoke this instead of using an AI coding product normally when the agent must create or maintain source-controlled checks, run them non-interactively in CI, and return pass or fail results with suggested diffs. This is skill-shaped because the boundary is specific: repo-owned AI checks in CI. It is not a generic IDE assistant, SDK, or broad coding-agent listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/enforce-source-controlled-ai-checks-in-ci-before-merging-risky-changes-with-continue-cli/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/enforce-source-controlled-ai-checks-in-ci-before-merging-risky-changes-with-continue-cli
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/enforce-source-controlled-ai-checks-in-ci-before-merging-risky-changes-with-continue-cli`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-source-controlled-ai-checks-in-ci-before-merging-risky-changes-with-continue-cli/)
