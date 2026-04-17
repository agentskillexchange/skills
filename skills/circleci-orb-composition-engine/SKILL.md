---
title: "CircleCI Orb Composition Engine"
description: "The CircleCI Orb Composition Engine streamlines creation and management of CircleCI Orbs for reusable CI/CD components. Using the circleci CLI, it handles the full orb lifecycle from development through publishing with orb pack for multi-file orb assembly, orb validate for schema verification, and orb publish with semantic versioning support. The engine manages reusable executors defining Docker images, resource classes, and environment variables that jobs reference by name. Parameterized commands accept typed parameters with defaults, enabling flexible step composition without duplicating configuration. Job templates combine executors and commands into complete workflow units with configurable parallelism and resource allocation. The tool supports orb development kits with local testing using circleci local execute, integration test workflows that validate orb behavior in real pipelines, and dev version publishing for pre-release testing. Pipeline parameters enable dynamic configuration where trigger metadata influences job selection and environment targeting. The composition engine generates orb documentation from inline descriptions and maintains changelogs across versions."
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Composition Engine

The CircleCI Orb Composition Engine streamlines creation and management of CircleCI Orbs for reusable CI/CD components. Using the circleci CLI, it handles the full orb lifecycle from development through publishing with orb pack for multi-file orb assembly, orb validate for schema verification, and orb publish with semantic versioning support. The engine manages reusable executors defining Docker images, resource classes, and environment variables that jobs reference by name. Parameterized commands accept typed parameters with defaults, enabling flexible step composition without duplicating configuration. Job templates combine executors and commands into complete workflow units with configurable parallelism and resource allocation. The tool supports orb development kits with local testing using circleci local execute, integration test workflows that validate orb behavior in real pipelines, and dev version publishing for pre-release testing. Pipeline parameters enable dynamic configuration where trigger metadata influences job selection and environment targeting. The composition engine generates orb documentation from inline descriptions and maintains changelogs across versions.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/circleci-orb-composition-engine
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/circleci-orb-composition-engine` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-composition-engine/)
