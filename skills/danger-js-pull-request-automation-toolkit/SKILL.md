---
title: "Danger JS Pull Request Automation Toolkit"
description: "Danger JS is an open source pull request automation toolkit maintained by the Danger project. It runs in continuous integration, reads metadata from the current pull request, and executes a Dangerfile written in JavaScript or TypeScript. That lets teams codify review rules such as checking whether changelog entries were updated, verifying test coverage expectations, flagging large diffs, or reminding contributors to add screenshots for UI changes.\nThe project has an official GitHub repository, published npm package, and dedicated documentation site. In practice, Danger JS fits best when a team already uses GitHub, GitLab, or Bitbucket in CI and wants consistent review feedback without building a custom bot from scratch. A common integration flow is to install the danger package as a dev dependency, initialize a Dangerfile, and run it from GitHub Actions or another CI pipeline with an API token that can comment on pull requests.\nFor agent workflows, this skill belongs in code quality and review automation. An agent can inspect repository structure, generate or update a Dangerfile, tune rules for labels, docs, tests, migrations, or release notes, and wire the command into existing CI jobs. Because Danger JS exposes pull request context and file lists, it also works well alongside test tooling, linting, and release automation to create a more predictable review pipeline."
verification: security_reviewed
source: "https://github.com/danger/danger-js"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "danger/danger-js"
  github_stars: 5463
---

# Danger JS Pull Request Automation Toolkit

Danger JS is an open source pull request automation toolkit maintained by the Danger project. It runs in continuous integration, reads metadata from the current pull request, and executes a Dangerfile written in JavaScript or TypeScript. That lets teams codify review rules such as checking whether changelog entries were updated, verifying test coverage expectations, flagging large diffs, or reminding contributors to add screenshots for UI changes.
The project has an official GitHub repository, published npm package, and dedicated documentation site. In practice, Danger JS fits best when a team already uses GitHub, GitLab, or Bitbucket in CI and wants consistent review feedback without building a custom bot from scratch. A common integration flow is to install the danger package as a dev dependency, initialize a Dangerfile, and run it from GitHub Actions or another CI pipeline with an API token that can comment on pull requests.
For agent workflows, this skill belongs in code quality and review automation. An agent can inspect repository structure, generate or update a Dangerfile, tune rules for labels, docs, tests, migrations, or release notes, and wire the command into existing CI jobs. Because Danger JS exposes pull request context and file lists, it also works well alongside test tooling, linting, and release automation to create a more predictable review pipeline.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/danger-js-pull-request-automation-toolkit
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/danger-js-pull-request-automation-toolkit` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/danger-js-pull-request-automation-toolkit/)
