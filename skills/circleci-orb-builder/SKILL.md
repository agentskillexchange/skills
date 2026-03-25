---
name: "CircleCI Orb Builder"
description: "Creates reusable CircleCI Orbs using the CircleCI Orb SDK and circleci/orb-tools@12 pipeline. Packages commands, executors, and jobs into publishable orbs with automated semantic versioning via the CircleCI CLI."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/circleci-orb-builder/"
tool_ecosystem:
  tool: "circleci"
  github_stars: 842
  github_repo: "circleci/circleci-docs"
  maintained: true
---

# CircleCI Orb Builder

Creates reusable CircleCI Orbs using the CircleCI Orb SDK and circleci/orb-tools@12 pipeline. Packages commands, executors, and jobs into publishable orbs with automated semantic versioning via the CircleCI CLI.

## Overview

The CircleCI Orb Builder skill streamlines creation of reusable CircleCI Orbs — shareable packages of CircleCI configuration. It uses the CircleCI Orb SDK patterns and circleci/orb-tools@12 orb for development, testing, and publishing workflows.

Given a description of desired CI/CD functionality, this skill generates complete orb source directories with commands/, jobs/, executors/, and examples/ following CircleCI best practices. It creates parameterized commands with proper type annotations (string, boolean, enum, executor, steps), executor definitions with configurable resource classes, and composed jobs.

The skill generates the full orb development pipeline including: local validation using circleci orb validate, integration testing with circleci/orb-tools/test orb, automated publishing via circleci/orb-tools/publish orb, and semantic version management based on commit messages.

It handles namespace registration, dev vs production orb channels, and generates comprehensive usage examples. The skill also creates bats (Bash Automated Testing System) tests for shell-based commands and supports both Docker and machine executors.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-builder -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-orb-builder/
