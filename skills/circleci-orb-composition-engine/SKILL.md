---
name: "CircleCI Orb Composition Engine"
description: "Composes and publishes CircleCI Orbs using the circleci CLI with orb pack, orb validate, and semantic versioning. Manages reusable executors, commands, and jobs with parameterized pipeline configurations."
category: "CI/CD Integrations"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-orb-composition-engine/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "circleci"  # from ase_tool_match
  github_stars: 842  # from ase_github_stars (integer, not string)
  github_repo: "circleci/circleci-docs"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CircleCI Orb Composition Engine

Composes and publishes CircleCI Orbs using the circleci CLI with orb pack, orb validate, and semantic versioning. Manages reusable executors, commands, and jobs with parameterized pipeline configurations.

## Overview

The CircleCI Orb Composition Engine streamlines creation and management of CircleCI Orbs for reusable CI/CD components. Using the circleci CLI, it handles the full orb lifecycle from development through publishing with orb pack for multi-file orb assembly, orb validate for schema verification, and orb publish with semantic versioning support. The engine manages reusable executors defining Docker images, resource classes, and environment variables that jobs reference by name. Parameterized commands accept typed parameters with defaults, enabling flexible step composition without duplicating configuration. Job templates combine executors and commands into complete workflow units with configurable parallelism and resource allocation. The tool supports orb development kits with local testing using circleci local execute, integration test workflows that validate orb behavior in real pipelines, and dev version publishing for pre-release testing. Pipeline parameters enable dynamic configuration where trigger metadata influences job selection and environment targeting. The composition engine generates orb documentation from inline descriptions and maintains changelogs across versions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-composition-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-composition-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-composition-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-composition-engine -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-composition-engine
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-orb-composition-engine/
