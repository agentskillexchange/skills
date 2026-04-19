---
title: "Danger JS Pull Request Automation Toolkit"
description: "Danger JS is an open source pull request automation toolkit maintained by the Danger project. It runs in continuous integration, reads metadata from the current pull request, and executes a Dangerfile written in JavaScript or TypeScript. That lets teams codify review rules such as checking whether changelog entries were updated, verifying test coverage expectations, flagging large diffs, or reminding contributors to add screenshots for UI changes. The project has an official GitHub repository, published npm package, and dedicated documentation site. In practice, Danger JS fits best when a team already uses GitHub, GitLab, or Bitbucket in CI and wants consistent review feedback without building a custom bot from scratch. A common integration flow is to install the danger package as a dev dependency, initialize a Dangerfile , and run it from GitHub Actions or another CI pipeline with an API token that can comment on pull requests. For agent workflows, this skill belongs in code quality and review automation. An agent can inspect repository structure, generate or update a Dangerfile, tune rules for labels, docs, tests, migrations, or release notes, and wire the command into existing CI jobs. Because Danger JS exposes pull request context and file lists, it also works well alongside test tooling, linting, and release automation to create a more predictable review pipeline."
source: "https://github.com/danger/danger-js"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "danger/danger-js"
  github_stars: 5463
---

# Danger JS Pull Request Automation Toolkit

Danger JS is an open source pull request automation toolkit maintained by the Danger project. It runs in continuous integration, reads metadata from the current pull request, and executes a Dangerfile written in JavaScript or TypeScript. That lets teams codify review rules such as checking whether changelog entries were updated, verifying test coverage expectations, flagging large diffs, or reminding contributors to add screenshots for UI changes. The project has an official GitHub repository, published npm package, and dedicated documentation site. In practice, Danger JS fits best when a team already uses GitHub, GitLab, or Bitbucket in CI and wants consistent review feedback without building a custom bot from scratch. A common integration flow is to install the danger package as a dev dependency, initialize a Dangerfile , and run it from GitHub Actions or another CI pipeline with an API token that can comment on pull requests. For agent workflows, this skill belongs in code quality and review automation. An agent can inspect repository structure, generate or update a Dangerfile, tune rules for labels, docs, tests, migrations, or release notes, and wire the command into existing CI jobs. Because Danger JS exposes pull request context and file lists, it also works well alongside test tooling, linting, and release automation to create a more predictable review pipeline.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/danger-js-pull-request-automation-toolkit/)
