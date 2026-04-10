---
name: CircleCI Orb Composer
description: Composes and validates CircleCI Orbs using the circleci/circleci-cli
  and circleci/orb-tools-orb SDK. Automates orb packaging, semantic versioning with
  conventional-changelog, and publishing to the CircleCI Orb Registry.
verification: security_reviewed
source: https://agentskillexchange.com/skills/circleci-orb-composer-7/
category:
- CI/CD Integrations
framework:
- Claude Code
---
# CircleCI Orb Composer

The CircleCI Orb Composer skill streamlines the creation, validation, and publishing of CircleCI Orbs — reusable configuration packages for CircleCI pipelines. It uses the circleci/circleci-cli to validate orb source YAML and the circleci/orb-tools-orb to automate the full orb development lifecycle.
The skill handles orb structure scaffolding with proper src/ directory layouts for commands, jobs, executors, and examples. It integrates conventional-changelog for automatic semantic versioning based on commit messages, ensuring orb versions follow semver conventions.
Capabilities include generating parameterized commands with proper type validation, creating executor definitions for Docker/machine/macOS environments, building job templates with configurable steps, and producing comprehensive usage examples. The skill validates orbs against the CircleCI schema, runs integration tests using circleci local execute, and publishes to the CircleCI Orb Registry with proper namespace management. It also supports generating orb documentation using orb-tools/pack and orb-tools/review commands.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-composer-7/)
