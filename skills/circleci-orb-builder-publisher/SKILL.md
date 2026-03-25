---
name: "CircleCI Orb Builder and Publisher"
description: "Creates, validates, and publishes CircleCI Orbs using the CircleCI CLI and Orb Registry API. Handles semantic versioning, namespace management, and orb dependency resolution."
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-orb-builder-publisher/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "circleci"  # from ase_tool_match
  github_stars: 842  # from ase_github_stars (integer, not string)
  github_repo: "circleci/circleci-docs"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CircleCI Orb Builder and Publisher

Creates, validates, and publishes CircleCI Orbs using the CircleCI CLI and Orb Registry API. Handles semantic versioning, namespace management, and orb dependency resolution.

## Overview

The CircleCI Orb Builder and Publisher streamlines the creation and distribution of reusable CircleCI configuration packages. Using the CircleCI CLI and Orb Registry API, it scaffolds new orb projects with proper directory structure including commands, jobs, executors, and examples. The skill validates orb YAML against the CircleCI schema, runs orb-tools/pack for single-file compilation, and executes local testing via circleci local execute. It manages namespace registration through the CircleCI GraphQL API, handles semantic version bumping with automated changelogs, and publishes development and production orb versions. The builder resolves orb dependency trees, detects circular dependencies, and validates parameter schemas across nested orb references. It integrates with the CircleCI Insights API to track orb adoption metrics, monitors for breaking changes in upstream orb dependencies, and generates migration guides when publishing major versions. Additional features include automatic README generation from orb metadata, integration test pipeline generation, and orb usage analytics dashboards.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-builder-publisher
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-builder-publisher -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-builder-publisher -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-builder-publisher -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-builder-publisher
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-orb-builder-publisher/
