---
title: "Run bounded Codex jobs inside GitHub Actions for PR review and repo maintenance with codex-action"
description: "Tool: codex-action. This skill gives an agent a narrow CI job: run Codex from a GitHub Actions workflow to review a pull request or perform another bounded repository task under explicit workflow permissions. When to use it: invoke this when a repo already lives in GitHub Actions and you want Codex to execute review, maintenance, or scheduled automation steps without opening an interactive local session. Using this skill is different from using the product normally because the operator workflow is CI-shaped: define the workflow trigger, install the action, pass a bounded prompt and sandbox mode, then capture Codex output as comments, artifacts, or follow-up steps. Scope boundary: this is not a generic Codex listing and not a broad GitHub Actions card. Its boundary is specific: run Codex as a permission-bounded GitHub Action for repository tasks."
source: "https://github.com/openai/codex-action"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "openai/codex-action"
  github_stars: 927
---

# Run bounded Codex jobs inside GitHub Actions for PR review and repo maintenance with codex-action

Tool: codex-action. This skill gives an agent a narrow CI job: run Codex from a GitHub Actions workflow to review a pull request or perform another bounded repository task under explicit workflow permissions. When to use it: invoke this when a repo already lives in GitHub Actions and you want Codex to execute review, maintenance, or scheduled automation steps without opening an interactive local session. Using this skill is different from using the product normally because the operator workflow is CI-shaped: define the workflow trigger, install the action, pass a bounded prompt and sandbox mode, then capture Codex output as comments, artifacts, or follow-up steps. Scope boundary: this is not a generic Codex listing and not a broad GitHub Actions card. Its boundary is specific: run Codex as a permission-bounded GitHub Action for repository tasks.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-bounded-codex-jobs-inside-github-actions-for-pr-review-and-repo-maintenance-with-codex-action/)
