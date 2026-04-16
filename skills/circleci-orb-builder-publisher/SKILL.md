---
title: "CircleCI Orb Builder and Publisher"
description: "Creates, validates, and publishes CircleCI Orbs using the CircleCI CLI and Orb Registry API. Handles semantic versioning, namespace management, and orb dependency resolution."
verification: "security_reviewed"
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Builder and Publisher

The CircleCI Orb Builder and Publisher streamlines the creation and distribution of reusable CircleCI configuration packages. Using the CircleCI CLI and Orb Registry API, it scaffolds new orb projects with proper directory structure including commands, jobs, executors, and examples. The skill validates orb YAML against the CircleCI schema, runs orb-tools/pack for single-file compilation, and executes local testing via circleci local execute. It manages namespace registration through the CircleCI GraphQL API, handles semantic version bumping with automated changelogs, and publishes development and production orb versions. The builder resolves orb dependency trees, detects circular dependencies, and validates parameter schemas across nested orb references. It integrates with the CircleCI Insights API to track orb adoption metrics, monitors for breaking changes in upstream orb dependencies, and generates migration guides when publishing major versions. Additional features include automatic README generation from orb metadata, integration test pipeline generation, and orb usage analytics dashboards.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-builder-publisher/)
