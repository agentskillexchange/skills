---
title: "CircleCI Orb Composition Engine"
description: "Composes and publishes CircleCI Orbs using the circleci CLI with orb pack, orb validate, and semantic versioning. Manages reusable executors, commands, and jobs with parameterized pipeline configurations."
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-composition-engine/)
