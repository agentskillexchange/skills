---
title: "CircleCI Orb Builder"
description: "Creates reusable CircleCI Orbs using the CircleCI Orb SDK and circleci/orb-tools@12 pipeline. Packages commands, executors, and jobs into publishable orbs with automated semantic versioning via the CircleCI CLI."
slug: "circleci-orb-builder"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/circleci-orb-builder/"
---

# CircleCI Orb Builder

Creates reusable CircleCI Orbs using the CircleCI Orb SDK and circleci/orb-tools@12 pipeline. Packages commands, executors, and jobs into publishable orbs with automated semantic versioning via the CircleCI CLI.

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
clawhub install circleci-orb-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CircleCI Orb Builder skill streamlines creation of reusable CircleCI Orbs — shareable packages of CircleCI configuration. It uses the CircleCI Orb SDK patterns and circleci/orb-tools@12 orb for development, testing, and publishing workflows.
Given a description of desired CI/CD functionality, this skill generates complete orb source directories with commands/, jobs/, executors/, and examples/ following CircleCI best practices. It creates parameterized commands with proper type annotations (string, boolean, enum, executor, steps), executor definitions with configurable resource classes, and composed jobs.
The skill generates the full orb development pipeline including: local validation using circleci orb validate, integration testing with circleci/orb-tools/test orb, automated publishing via circleci/orb-tools/publish orb, and semantic version management based on commit messages.
It handles namespace registration, dev vs production orb channels, and generates comprehensive usage examples. The skill also creates bats (Bash Automated Testing System) tests for shell-based commands and supports both Docker and machine executors.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-builder/)
