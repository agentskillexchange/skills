---
name: "Automate repository triage and recurring repo maintenance with guarded GitHub agent workflows"
slug: "automate-repository-triage-and-recurring-maintenance-with-github-agent-workflows"
description: "Use GitHub Agentic Workflows to let an agent triage issues, inspect CI failures, or deliver scheduled repository upkeep inside GitHub Actions with explicit workflow definitions and reviewable runs. This is for bounded, repeatable repository operations, not for listing GitHub as a general coding platform."
github_stars: 4286
verification: "listed"
source: "https://github.com/github/gh-aw"
author: "GitHub"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "github/gh-aw"
  github_stars: 4286
---

# Automate repository triage and recurring repo maintenance with guarded GitHub agent workflows

Use GitHub Agentic Workflows to let an agent triage issues, inspect CI failures, or deliver scheduled repository upkeep inside GitHub Actions with explicit workflow definitions and reviewable runs. This is for bounded, repeatable repository operations, not for listing GitHub as a general coding platform.

## Prerequisites

GitHub Actions, gh CLI

## Installation

Use the upstream install or setup path that matches your environment:
- make golint-custom builds cmd/linters and runs the custom analyzers against ./cmd/... and ./pkg/....

Requirements and caveats from upstream:
- Using agentic workflows in your repository requires careful attention to security considerations and careful human supervision, and even then things can still go wrong. Use it with caution, and at your own risk.

Basic usage or getting-started notes:
- Write agentic workflows in natural language markdown, and run them in GitHub Actions.
- [Quick Start](#quick-start)
- Ready to get your first agentic workflow running? Follow our step-by-step [Quick Start Guide](https://github.github.com/gh-aw/setup/quick-start/) to install the extension, add a sample workflow, and see it in action.

- Source: https://github.com/github/gh-aw
- Extracted from upstream docs: https://raw.githubusercontent.com/github/gh-aw/HEAD/README.md

## Documentation

- https://github.github.com/gh-aw/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/automate-repository-triage-and-recurring-maintenance-with-github-agent-workflows/)
