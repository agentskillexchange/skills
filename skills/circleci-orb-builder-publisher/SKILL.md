---
title: "CircleCI Orb Builder and Publisher"
description: "Creates, validates, and publishes CircleCI Orbs using the CircleCI CLI and Orb Registry API. Handles semantic versioning, namespace management, and orb dependency resolution."
slug: "circleci-orb-builder-publisher"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/circleci-orb-builder-publisher/"
---

# CircleCI Orb Builder and Publisher

Creates, validates, and publishes CircleCI Orbs using the CircleCI CLI and Orb Registry API. Handles semantic versioning, namespace management, and orb dependency resolution.

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
clawhub install circleci-orb-builder-publisher
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CircleCI Orb Builder and Publisher streamlines the creation and distribution of reusable CircleCI configuration packages. Using the CircleCI CLI and Orb Registry API, it scaffolds new orb projects with proper directory structure including commands, jobs, executors, and examples. The skill validates orb YAML against the CircleCI schema, runs orb-tools/pack for single-file compilation, and executes local testing via circleci local execute. It manages namespace registration through the CircleCI GraphQL API, handles semantic version bumping with automated changelogs, and publishes development and production orb versions. The builder resolves orb dependency trees, detects circular dependencies, and validates parameter schemas across nested orb references. It integrates with the CircleCI Insights API to track orb adoption metrics, monitors for breaking changes in upstream orb dependencies, and generates migration guides when publishing major versions. Additional features include automatic README generation from orb metadata, integration test pipeline generation, and orb usage analytics dashboards.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-builder-publisher/)
