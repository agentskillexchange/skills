---
title: CircleCI Orb Builder
description: 'The CircleCI Orb Builder skill streamlines creation of reusable CircleCI
  Orbs — shareable packages of CircleCI configuration. It uses the CircleCI Orb SDK
  patterns and circleci/orb-tools@12 orb for development, testing, and publishing
  workflows. Given a description of desired CI/CD functionality, this skill generates
  complete orb source directories with commands/, jobs/, executors/, and examples/
  following CircleCI best practices. It creates parameterized commands with proper
  type annotations (string, boolean, enum, executor, steps), executor definitions
  with configurable resource classes, and composed jobs. The skill generates the full
  orb development pipeline including: local validation using circleci orb validate,
  integration testing with circleci/orb-tools/test orb, automated publishing via circleci/orb-tools/publish
  orb, and semantic version management based on commit messages. It handles namespace
  registration, dev vs production orb channels, and generates comprehensive usage
  examples. The skill also creates bats (Bash Automated Testing System) tests for
  shell-based commands and supports both Docker and machine executors.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/circleci-orb-builder/
category:
- CI/CD Integrations
framework:
- Claude Code
---

# CircleCI Orb Builder

The CircleCI Orb Builder skill streamlines creation of reusable CircleCI Orbs — shareable packages of CircleCI configuration. It uses the CircleCI Orb SDK patterns and circleci/orb-tools@12 orb for development, testing, and publishing workflows. Given a description of desired CI/CD functionality, this skill generates complete orb source directories with commands/, jobs/, executors/, and examples/ following CircleCI best practices. It creates parameterized commands with proper type annotations (string, boolean, enum, executor, steps), executor definitions with configurable resource classes, and composed jobs. The skill generates the full orb development pipeline including: local validation using circleci orb validate, integration testing with circleci/orb-tools/test orb, automated publishing via circleci/orb-tools/publish orb, and semantic version management based on commit messages. It handles namespace registration, dev vs production orb channels, and generates comprehensive usage examples. The skill also creates bats (Bash Automated Testing System) tests for shell-based commands and supports both Docker and machine executors.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-builder/)
