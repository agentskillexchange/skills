---
name: "CircleCI Orb Builder and Publisher"
description: "Creates, validates, and publishes CircleCI Orbs using the CircleCI CLI and Orb Registry API. Handles semantic versioning, namespace management, and orb dependency resolution."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/circleci-orb-builder-publisher/"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
---

# CircleCI Orb Builder and Publisher

The CircleCI Orb Builder and Publisher streamlines the creation and distribution of reusable CircleCI configuration packages. Using the CircleCI CLI and Orb Registry API, it scaffolds new orb projects with proper directory structure including commands, jobs, executors, and examples. The skill validates orb YAML against the CircleCI schema, runs orb-tools/pack for single-file compilation, and executes local testing via circleci local execute. It manages namespace registration through the CircleCI GraphQL API, handles semantic version bumping with automated changelogs, and publishes development and production orb versions. The builder resolves orb dependency trees, detects circular dependencies, and validates parameter schemas across nested orb references. It integrates with the CircleCI Insights API to track orb adoption metrics, monitors for breaking changes in upstream orb dependencies, and generates migration guides when publishing major versions. Additional features include automatic README generation from orb metadata, integration test pipeline generation, and orb usage analytics dashboards.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-builder-publisher/)
