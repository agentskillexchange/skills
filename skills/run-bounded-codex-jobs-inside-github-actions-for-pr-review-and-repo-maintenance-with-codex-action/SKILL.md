---
title: "Run bounded Codex jobs inside GitHub Actions for PR review and repo maintenance with codex-action"
description: "Use codex-action when an agent operator wants Codex to run inside GitHub Actions for PR review or scheduled repo work with explicit workflow permissions, prompts, and CI boundaries."
verification: "security_reviewed"
source: "https://github.com/openai/codex-action"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "openai/codex-action"
  github_stars: 927
---

# Run bounded Codex jobs inside GitHub Actions for PR review and repo maintenance with codex-action

Tool: codex-action. This skill gives an agent a narrow CI job: run Codex from a GitHub Actions workflow to review a pull request or perform another bounded repository task under explicit workflow permissions.

When to use it: invoke this when a repo already lives in GitHub Actions and you want Codex to execute review, maintenance, or scheduled automation steps without opening an interactive local session. Using this skill is different from using the product normally because the operator workflow is CI-shaped: define the workflow trigger, install the action, pass a bounded prompt and sandbox mode, then capture Codex output as comments, artifacts, or follow-up steps.

Scope boundary: this is not a generic Codex listing and not a broad GitHub Actions card. Its boundary is specific: run Codex as a permission-bounded GitHub Action for repository tasks.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-bounded-codex-jobs-inside-github-actions-for-pr-review-and-repo-maintenance-with-codex-action/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-bounded-codex-jobs-inside-github-actions-for-pr-review-and-repo-maintenance-with-codex-action
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-bounded-codex-jobs-inside-github-actions-for-pr-review-and-repo-maintenance-with-codex-action`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-bounded-codex-jobs-inside-github-actions-for-pr-review-and-repo-maintenance-with-codex-action/)
