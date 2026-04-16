---
title: "CircleCI Orb Builder"
description: "Creates reusable CircleCI Orbs using the CircleCI Orb SDK and circleci/orb-tools@12 pipeline. Packages commands, executors, and jobs into publishable orbs with automated semantic versioning via the CircleCI CLI."
verification: "security_reviewed"
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Builder

The CircleCI Orb Builder skill streamlines creation of reusable CircleCI Orbs — shareable packages of CircleCI configuration. It uses the CircleCI Orb SDK patterns and circleci/orb-tools@12 orb for development, testing, and publishing workflows.

Given a description of desired CI/CD functionality, this skill generates complete orb source directories with commands/, jobs/, executors/, and examples/ following CircleCI best practices. It creates parameterized commands with proper type annotations (string, boolean, enum, executor, steps), executor definitions with configurable resource classes, and composed jobs.

The skill generates the full orb development pipeline including: local validation using circleci orb validate, integration testing with circleci/orb-tools/test orb, automated publishing via circleci/orb-tools/publish orb, and semantic version management based on commit messages.

It handles namespace registration, dev vs production orb channels, and generates comprehensive usage examples. The skill also creates bats (Bash Automated Testing System) tests for shell-based commands and supports both Docker and machine executors.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-builder/)
