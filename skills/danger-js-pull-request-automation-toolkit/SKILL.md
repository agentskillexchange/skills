---
title: "Danger JS Pull Request Automation Toolkit"
description: "Danger JS automates pull request review chores by running programmable checks inside CI and posting structured feedback back to GitHub, GitLab, and other code hosts. It is a strong fit for teams that want to turn review conventions into repeatable checks instead of relying on humans to catch the same issues every time."
slug: "danger-js-pull-request-automation-toolkit"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/danger/danger-js"
listed: true
---

# Danger JS Pull Request Automation Toolkit

Danger JS automates pull request review chores by running programmable checks inside CI and posting structured feedback back to GitHub, GitLab, and other code hosts. It is a strong fit for teams that want to turn review conventions into repeatable checks instead of relying on humans to catch the same issues every time.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install danger-js-pull-request-automation-toolkit
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Danger JS is an open source pull request automation toolkit maintained by the Danger project. It runs in continuous integration, reads metadata from the current pull request, and executes a Dangerfile written in JavaScript or TypeScript. That lets teams codify review rules such as checking whether changelog entries were updated, verifying test coverage expectations, flagging large diffs, or reminding contributors to add screenshots for UI changes.
The project has an official GitHub repository, published npm package, and dedicated documentation site. In practice, Danger JS fits best when a team already uses GitHub, GitLab, or Bitbucket in CI and wants consistent review feedback without building a custom bot from scratch. A common integration flow is to install the danger package as a dev dependency, initialize a Dangerfile, and run it from GitHub Actions or another CI pipeline with an API token that can comment on pull requests.
For agent workflows, this skill belongs in code quality and review automation. An agent can inspect repository structure, generate or update a Dangerfile, tune rules for labels, docs, tests, migrations, or release notes, and wire the command into existing CI jobs. Because Danger JS exposes pull request context and file lists, it also works well alongside test tooling, linting, and release automation to create a more predictable review pipeline.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/danger-js-pull-request-automation-toolkit/)
