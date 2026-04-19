---
title: "CircleCI Orb Composition Engine"
description: "The CircleCI Orb Composition Engine streamlines creation and management of CircleCI Orbs for reusable CI/CD components. Using the circleci CLI, it handles the full orb lifecycle from development through publishing with orb pack for multi-file orb assembly, orb validate for schema verification, and orb publish with semantic versioning support. The engine manages reusable executors defining Docker images, resource classes, and environment variables that jobs reference by name. Parameterized commands accept typed parameters with defaults, enabling flexible step composition without duplicating configuration. Job templates combine executors and commands into complete workflow units with configurable parallelism and resource allocation. The tool supports orb development kits with local testing using circleci local execute, integration test workflows that validate orb behavior in real pipelines, and dev version publishing for pre-release testing. Pipeline parameters enable dynamic configuration where trigger metadata influences job selection and environment targeting. The composition engine generates orb documentation from inline descriptions and maintains changelogs across versions."
source: "https://github.com/circleci/circleci-docs"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Composition Engine

The CircleCI Orb Composition Engine streamlines creation and management of CircleCI Orbs for reusable CI/CD components. Using the circleci CLI, it handles the full orb lifecycle from development through publishing with orb pack for multi-file orb assembly, orb validate for schema verification, and orb publish with semantic versioning support. The engine manages reusable executors defining Docker images, resource classes, and environment variables that jobs reference by name. Parameterized commands accept typed parameters with defaults, enabling flexible step composition without duplicating configuration. Job templates combine executors and commands into complete workflow units with configurable parallelism and resource allocation. The tool supports orb development kits with local testing using circleci local execute, integration test workflows that validate orb behavior in real pipelines, and dev version publishing for pre-release testing. Pipeline parameters enable dynamic configuration where trigger metadata influences job selection and environment targeting. The composition engine generates orb documentation from inline descriptions and maintains changelogs across versions.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-composition-engine/)
